import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS (polish only — no background/color changes)
# --------------------------------------------------

st.markdown("""
<style>

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

footer, #MainMenu{ visibility:hidden; }

/* ---------- page header ---------- */

.dash-header{
    padding-bottom:10px;
    margin-bottom:10px;
}

.dash-header h1{
    font-size:28px;
    font-weight:700;
    margin-bottom:6px;
}

.dash-header p{
    font-size:15px;
    color:#94A3B8;
    margin-top:0;
    line-height:1.6;
}

/* ---------- sidebar ---------- */

section[data-testid="stSidebar"] .stMultiSelect label{
    font-weight:600;
    font-size:13.5px;
    letter-spacing:0.2px;
}

/* ---------- metric cards ---------- */
/* Targets Streamlit's native st.metric container so no logic changes are needed */

div[data-testid="stMetric"]{
    background:#111A2E;
    border:1px solid #1E293B;
    border-radius:10px;
    padding:16px 20px 14px 20px;
    box-shadow:0 1px 2px rgba(0,0,0,0.15);
}

div[data-testid="stMetricLabel"] > div{
    color:#94A3B8;
    font-size:13px;
    font-weight:500;
}

div[data-testid="stMetricValue"]{
    color:#F8FAFC;
    font-size:26px;
    font-weight:700;
}

/* ---------- chart cards ---------- */
/* Wraps each Plotly chart in a card frame without touching the chart's own colors */

div[data-testid="stPlotlyChart"]{
    background:#111A2E;
    border:1px solid #1E293B;
    border-radius:10px;
    padding:12px 14px 4px 14px;
    box-shadow:0 1px 2px rgba(0,0,0,0.15);
}

/* ---------- section dividers ---------- */

hr{
    border-color:rgba(148,163,184,0.12) !important;
    margin-top:10px !important;
    margin-bottom:10px !important;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="dash-header">
    <h1>Customer Churn Analytics</h1>
    <p>Interactive dashboard for monitoring customer churn, retention trends, and business insights</p>
</div>
""", unsafe_allow_html=True)

df = pd.read_csv("data/customer_churn_predictions.csv")

# ==========================
# SIDEBAR FILTERS
# ==========================

st.sidebar.header("Filters")

gender = st.sidebar.multiselect(
    "Gender",
    options=sorted(df["Gender"].unique())
)

contract = st.sidebar.multiselect(
    "Contract",
    options=sorted(df["Contract"].unique())
)

internet = st.sidebar.multiselect(
    "Internet Service",
    options=sorted(df["internet_service"].unique())
)

payment = st.sidebar.multiselect(
    "Payment Method",
    options=sorted(df["payment_method"].unique())
)

if not gender:
    gender = df["Gender"].unique()

if not contract:
    contract = df["Contract"].unique()

if not internet:
    internet = df["internet_service"].unique()

if not payment:
    payment = df["payment_method"].unique()


filtered_df = df[
    (df["Gender"].isin(gender)) &
    (df["Contract"].isin(contract)) &
    (df["internet_service"].isin(internet)) &
    (df["payment_method"].isin(payment))
]

total_customers = len(filtered_df)

churn_rate = (
    filtered_df["churn_label"]
    .value_counts(normalize=True)
    .get("Yes", 0) * 100
)

avg_monthly_charge = (
    filtered_df["monthly_charge"].mean()
    if total_customers > 0
    else 0
)

avg_tenure = (
    filtered_df["tenure_in_months"].mean()
    if total_customers > 0
    else 0
)



st.divider()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Customers",
    f"{total_customers:,}"
)

col2.metric(
    "Churn Rate",
    f"{churn_rate:.1f}%"
)

col3.metric(
    "Avg Monthly Charge",
    f"${avg_monthly_charge:.2f}"
)

col4.metric(
    "Avg Tenure",
    f"{avg_tenure:.1f} Months"
)

st.divider()

chart1, chart2 = st.columns(2)

# ==========================================
# CHART 1 - CUSTOMER CHURN DISTRIBUTION
# ==========================================

with chart1:

    churn_counts = (
        filtered_df["churn_label"]
        .value_counts()
        .reset_index()
    )

    churn_counts.columns = ["Status", "Customers"]

    fig = px.pie(
        churn_counts,
        names="Status",
        values="Customers",
        hole=0.60,
        color="Status",
        color_discrete_map={
            "Yes": "#EF4444",
            "No": "#3B82F6"
        }
    )

    fig.update_layout(
        template="plotly_dark",
        height=380,
        showlegend=False,

        title={
            "text": "Customer Churn Distribution",
            "x": 0.5,
            "xanchor": "center"
        },

        legend_title="",
        margin=dict(l=20, r=20, t=60, b=20),
        paper_bgcolor="#0B1220",
        plot_bgcolor="#0B1220"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# CHART 2 - CUSTOMERS BY CONTRACT
# ==========================================

with chart2:

    contract_data = (
    filtered_df
    .groupby("Contract")
    .size()
    .reset_index(name="Customers")
    .sort_values(by="Customers", ascending=False)
)

    fig2 = px.bar(
    contract_data,
    x="Contract",
    y="Customers",
    color_discrete_sequence=["#3B82F6"]
)

    fig2.update_layout(
        template="plotly_dark",
        height=420,
        showlegend=False,

        title={
            "text": "Customers by Contract Type",
            "x": 0.5,
            "xanchor": "center"
        },

        xaxis_title="",
        yaxis_title="Customers",

        margin=dict(l=20, r=20, t=60, b=20),

        paper_bgcolor="#0B1220",
        plot_bgcolor="#0B1220"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.divider()

chart3, chart4 = st.columns(2)

with chart3:
    payment_churn = (
    filtered_df
    .groupby("payment_method")["churn_label"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="Churn Rate")
    .sort_values(by="Churn Rate", ascending=False)
)
    fig3 = px.bar(
    payment_churn,
    x="payment_method",
    y="Churn Rate",
    color_discrete_sequence=["#3B82F6"]
)
    
    fig3.update_layout(
    template="plotly_dark",
    height=420,

    title={
        "text": "Churn Rate by Payment Method",
        "x": 0.5,
        "xanchor": "center"
    },

    xaxis_title="",
    yaxis_title="Churn Rate (%)",

    coloraxis_showscale=False,

    margin=dict(
        l=20,
        r=20,
        t=60,
        b=20
    ),

    paper_bgcolor="#0B1220",
    plot_bgcolor="#0B1220"
)
    st.plotly_chart(
    fig3,
    use_container_width=True
)

with chart4:

    age_churn = (
        filtered_df
        .groupby("age_group")["churn_label"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index(name="Churn Rate")
        .sort_values("Churn Rate", ascending=False)
    )
    fig4 = px.bar(
        age_churn,
        x="age_group",
        y="Churn Rate",
        color_discrete_sequence=["#3B82F6"]
    )
    fig4.update_layout(
        template="plotly_dark",
        height=420,

        title={
            "text": "Churn Rate by Age Group",
            "x":0.5,
            "xanchor":"center"
        },

        xaxis_title="",
        yaxis_title="Churn Rate (%)",

        showlegend=False,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        paper_bgcolor="#0B1220",
        plot_bgcolor="#0B1220"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

st.divider()

chart5, chart6 = st.columns(2)

with chart5:

    plot_df = filtered_df.copy()

    plot_df["churn_status"] = plot_df["churn_label"].replace({
        "Yes": "Churned",
        "No": "Retained"
    })

    fig5 = px.box(
        plot_df,
        x="churn_status",
        y="monthly_charge",
        color="churn_status",
        color_discrete_map={
            "Churned": "#EF4444",
            "Retained": "#3B82F6"
        },
        points="outliers"
    )

    fig5.update_layout(
        template="plotly_dark",
        height=420,

        title={
            "text": "Monthly Charges by Churn Status",
            "x": 0.5,
            "xanchor": "center"
        },

        title_font=dict(size=18),

        xaxis_title="",
        yaxis_title="Monthly Charge ($)",

        showlegend=False,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        paper_bgcolor="#0B1220",
        plot_bgcolor="#0B1220"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )


with chart6:

    plot_df = filtered_df.copy()

    plot_df["churn_status"] = plot_df["churn_label"].replace({
        "Yes": "Churned",
        "No": "Retained"
    })


    fig6 = px.box(
    plot_df,
    x="churn_status",
    y="tenure_in_months",
    color="churn_status",
    color_discrete_map={
        "Churned": "#EF4444",
        "Retained": "#3B82F6"
    },
    points="outliers"
)

    fig6.update_layout(
        template="plotly_dark",
        height=420,

        title={
            "text": "Tenure by Churn Status",
            "x": 0.5,
            "xanchor": "center"
        },

        title_font=dict(size=18),

        xaxis_title="",
        yaxis_title="Tenure (Months)",

        showlegend=False,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        paper_bgcolor="#0B1220",
        plot_bgcolor="#0B1220"
    )

    st.plotly_chart(
        fig6,
        use_container_width=True
    )
