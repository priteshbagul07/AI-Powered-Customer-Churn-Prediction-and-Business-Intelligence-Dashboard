import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction System",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
# Plain, restrained palette. One accent color, used sparingly.
# No gradients, no glow, no decorative motifs — just clean structure.

st.markdown("""
<style>

.stApp{
    background:#0B1220;
}

.block-container{
    padding-top:1.5rem;
    padding-left:3rem;
    padding-right:3rem;
    max-width:1140px;
}

html, body, [class*="css"]{
    font-family:-apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color:#E2E8F0;
}

footer, #MainMenu{ visibility:hidden; }

/* ---------- header ---------- */

.page-header{
    border-bottom:1px solid #1E293B;
    padding-bottom:24px;
    margin-bottom:28px;
}

.page-header h1{
    font-size:30px;
    font-weight:700;
    color:#F8FAFC;
    margin-bottom:8px;
}

.page-header p{
    font-size:15px;
    color:#94A3B8;
    max-width:720px;
    line-height:1.6;
    margin-bottom:0;
}

/* ---------- metric cards ---------- */

.metric-card{
    background:#111A2E;
    border:1px solid #1E293B;
    border-radius:8px;
    padding:18px 20px;
    height:100%;
}

.metric-label{
    font-size:13px;
    color:#94A3B8;
    margin-bottom:6px;
}

.metric-value{
    font-size:26px;
    font-weight:700;
    color:#F8FAFC;
}

/* ---------- section ---------- */

/* ---------- section block wrapper ---------- */

.section-title{
    font-size:19px;
    font-weight:700;
    color:#F8FAFC;
    margin-top:0;
    margin-bottom:20px;
}

.section-sub{
    font-size:14px;
    color:#7C93C4;
    margin-bottom:16px;
}

.body-text{
    font-size:16px;
    color:#A8B7D4;
    line-height:1.8;
    font-weight:400;
    margin-bottom:18px;
}

/* ---------- tech list ---------- */

.tech-item{
    display:flex;
    align-items:center;
    gap:10px;
    background:#111A2E;
    border:1px solid #1E293B;
    border-radius:6px;
    padding:10px 14px;
    font-size:14px;
    color:#E2E8F0;
    margin-bottom:8px;
}

.tech-item .dot{
    width:6px;
    height:6px;
    border-radius:50%;
    background:#60A5FA;
    flex-shrink:0;
}

/* ---------- feature cards ---------- */

.feature-card{
    background:#111A2E;
    border:1px solid #1E293B;
    border-left:3px solid #60A5FA;
    border-radius:6px;
    padding:18px 20px;
    height:100%;
    min-height:128px;
    margin-bottom:14px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    box-sizing:border-box;
}

.feature-card h3{
    font-size:15.5px;
    font-weight:600;
    color:#F8FAFC;
    margin-bottom:6px;
}

.feature-card p{
    font-size:14px;
    color:#94A3B8;
    line-height:1.6;
    margin-bottom:0;
}

/* ---------- footer ---------- */

.footer-note{
    color:#64748B;
    font-size:12.5px;
    text-align:center;
    padding:24px 0 8px 0;
    border-top:1px solid #1E293B;
    margin-top:32px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="page-header">
    <h1>Customer Churn Prediction System</h1>
    <p>
An end-to-end machine learning application for customer churn prediction, interactive analytics, and data-driven retention strategies for telecom businesses.    </p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# MODEL METRICS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

metrics = [
    ("Accuracy", "96.45%"),
    ("Precision", "96.0%"),
    ("Recall", "90.0%"),
    ("ROC-AUC", "99.2%"),
]

for col, (label, value) in zip([col1, col2, col3, col4], metrics):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

# --------------------------------------------------
# ABOUT PROJECT
# --------------------------------------------------

st.divider()

st.markdown(
    '<p class="section-title">About the Project</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div style="max-width:850px;">

<p class="body-text">
Customer churn is a major challenge for telecom companies because acquiring new customers is more expensive than retaining existing ones.</p>

<p class="body-text">
This project uses a machine learning model trained on customer demographic and service usage data to predict churn risk. The application also provides interactive dashboards and business insights to help organizations identify high-risk customers and support data-driven retention decisions.</p>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TECHNOLOGY STACK
# --------------------------------------------------

st.divider()

st.markdown(
    '<p class="section-title">Technology Stack & Tools</p>',
    unsafe_allow_html=True
)

tech_col1, tech_col2 = st.columns(2)

with tech_col1:
    st.markdown(
        '<div class="tech-item"><span class="dot"></span><b>Programming:</b> Python</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="tech-item"><span class="dot"></span><b>Database:</b> SQL</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="tech-item"><span class="dot"></span><b>Machine Learning:</b> Scikit-Learn</div>',
        unsafe_allow_html=True
    )

with tech_col2:
    st.markdown(
        '<div class="tech-item"><span class="dot"></span><b>Web Framework:</b> Streamlit</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="tech-item"><span class="dot"></span><b>Visualization:</b> Plotly</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="tech-item"><span class="dot"></span><b>Model:</b> Logistic Regression</div>',
        unsafe_allow_html=True
    )

# --------------------------------------------------
# FEATURES
# --------------------------------------------------

st.divider()

st.markdown(
    '<p class="section-title">Application Features</p>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
<div class="feature-card">
    <h3>Interactive Dashboard</h3>
    <p>
    Analyze customer behavior using interactive KPIs, charts, and filters.
    </p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">
    <h3>Customer Churn Prediction</h3>
    <p>
    Predict whether a customer is likely to churn using the trained machine learning model.
    </p>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="feature-card">
    <h3>High-Risk Customer Detection</h3>
    <p>
    Identify customers with a high probability of churn for proactive retention.
    </p>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">
    <h3>Business Insights</h3>
    <p>
    Support business decisions with customer analytics and churn insights.
    </p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    '<div class="footer-note">Developed by Paras — Customer Churn Prediction System</div>',
    unsafe_allow_html=True
)