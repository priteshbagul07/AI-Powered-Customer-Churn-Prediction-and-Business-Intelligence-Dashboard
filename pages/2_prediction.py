import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Prediction",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS (matches the theme used on the other pages)
# --------------------------------------------------
# NOTE: color palette is unchanged from the original — every hex/rgba
# value below already existed in the source file. Only spacing,
# hierarchy, shadows, and structure were refined.

st.markdown("""
<style>

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1180px;
}

footer, #MainMenu{ visibility:hidden; }

/* ---------- page header ---------- */

.dash-header{
    padding-bottom:12px;
    margin-bottom:12px;
    border-bottom:1px solid rgba(148,163,184,0.12);
}

.dash-eyebrow{
    font-size:12px;
    font-weight:600;
    letter-spacing:0.08em;
    text-transform:uppercase;
    color:#3B82F6;
    margin-bottom:8px;
}

.dash-header h1{
    font-size:29px;
    font-weight:700;
    color:#F8FAFC;
    margin-bottom:8px;
    letter-spacing:-0.01em;
}

.dash-header p{
    font-size:14.5px;
    color:#94A3B8;
    margin-top:0;
    line-height:1.65;
    max-width:900px;
}

/* ---------- section panel ---------- */

.section-block{
    background:#111A2E;
    border:1px solid #1E293B;
    border-top:2px solid #3B82F6;
    border-radius:12px;
    padding:22px 26px 10px 26px;
    margin-top:24px;
    margin-bottom:0;
    box-shadow:0 1px 2px rgba(0,0,0,0.25);
}

.section-block .block-title{
    font-size:16.5px;
    font-weight:700;
    color:#F8FAFC;
    margin:0 0 14px 0;
    letter-spacing:-0.005em;
}

/* standalone heading, same type scale as block-title, used outside a panel */
.block-heading{
    font-size:16.5px;
    font-weight:700;
    color:#F8FAFC;
    letter-spacing:-0.005em;
    margin:24px 0 14px 0;
}

/* tighten default streamlit column/widget spacing inside panels */
.section-block div[data-testid="stSelectbox"] label,
.section-block div[data-testid="stNumberInput"] label,
.section-block div[data-testid="stSlider"] label{
    font-size:13px;
    font-weight:500;
    color:#CBD5E1;
}

/* ---------- expander ---------- */

div[data-testid="stExpander"]{
    border:1px solid #1E293B;
    border-top:2px solid #3B82F6;
    border-radius:12px;
    background:#111A2E;
    box-shadow:0 1px 2px rgba(0,0,0,0.25);
    margin-top:24px;
}

div[data-testid="stExpander"] summary{
    font-size:14.5px;
    font-weight:600;
    color:#F8FAFC;
    padding:4px 2px;
}

/* ---------- submit button ---------- */

.stButton > button, button[kind="formSubmit"]{
    background:#3B82F6 !important;
    color:#F8FAFC !important;
    border:none !important;
    border-radius:8px !important;
    font-weight:600 !important;
    padding:10px 0 !important;
    letter-spacing:0.01em;
    box-shadow:0 2px 6px rgba(59,130,246,0.25);
    transition:opacity 0.15s ease;
}

.stButton > button:hover, button[kind="formSubmit"]:hover{
    opacity:0.9;
}

/* ---------- result cards ---------- */

.result-card{
    border-radius:12px;
    padding:24px 26px;
    border:1px solid #1E293B;
    box-shadow:0 2px 6px rgba(0,0,0,0.25);
    margin-bottom:16px;
}

.result-card.churn-yes{
    background:rgba(239,68,68,0.08);
    border-color:rgba(239,68,68,0.35);
}

.result-card.churn-no{
    background:rgba(59,130,246,0.08);
    border-color:rgba(59,130,246,0.35);
}

.result-label{
    font-size:12.5px;
    font-weight:600;
    letter-spacing:0.04em;
    text-transform:uppercase;
    color:#94A3B8;
    margin-bottom:6px;
}

.result-value{
    font-size:30px;
    font-weight:700;
    color:#F8FAFC;
    line-height:1.2;
}

.risk-badge{
    display:inline-block;
    padding:5px 13px;
    border-radius:999px;
    font-size:12px;
    font-weight:700;
    letter-spacing:0.02em;
    margin-top:10px;
}

.risk-low{ background:rgba(34,197,94,0.15); color:#4ADE80; }
.risk-medium{ background:rgba(234,179,8,0.15); color:#FACC15; }
.risk-high{ background:rgba(239,68,68,0.18); color:#F87171; }

/* ---------- metric cards (reused style) ---------- */

div[data-testid="stMetric"]{
    background:#111A2E;
    border:1px solid #1E293B;
    border-radius:12px;
    padding:16px 20px 14px 20px;
    box-shadow:0 1px 2px rgba(0,0,0,0.25);
}

div[data-testid="stMetricLabel"] > div{
    color:#94A3B8;
    font-size:12.5px;
    font-weight:600;
    letter-spacing:0.02em;
}

div[data-testid="stMetricValue"]{
    color:#F8FAFC;
    font-size:26px;
    font-weight:700;
}

/* ---------- recommendations panel ---------- */

.reco-panel{
    background:#111A2E;
    border:1px solid #1E293B;
    border-top:2px solid #3B82F6;
    border-radius:12px;
    padding:20px 24px 20px 24px;
    box-shadow:0 2px 6px rgba(0,0,0,0.25);
    height:100%;
}

.reco-title{
    font-size:13px;
    font-weight:600;
    letter-spacing:0.04em;
    text-transform:uppercase;
    color:#94A3B8;
    margin-bottom:14px;
}

.reco-item{
    display:flex;
    align-items:flex-start;
    gap:10px;
    padding:11px 0;
    border-bottom:1px solid rgba(148,163,184,0.10);
    font-size:14px;
    color:#E2E8F0;
    line-height:1.55;
}

.reco-item:last-child{
    border-bottom:none;
    padding-bottom:0;
}

.reco-dot{
    width:7px;
    height:7px;
    border-radius:50%;
    margin-top:6px;
    flex-shrink:0;
}

.reco-dot.high{ background:#F87171; }
.reco-dot.medium{ background:#FACC15; }
.reco-dot.low{ background:#4ADE80; }

hr{
    border-color:rgba(148,163,184,0.12) !important;
    margin-top:14px !important;
    margin-bottom:14px !important;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="dash-header">
    <div class="dash-eyebrow">Prediction Tool</div>
    <h1>AI-Powered Customer Churn Prediction and Business Intelligence Dashboard</h1>
    <p>Enter the customer's information to estimate churn risk and receive business
    recommendations for improving customer retention.</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

MODEL_PATH = "model/churn_prediction_model.pkl"

@st.cache_resource
def load_model(path):
    return joblib.load(path)

try:
    model = load_model(MODEL_PATH)
except Exception as e:
    st.error(
        f"Couldn't load the model from `{MODEL_PATH}`. "
        f"Make sure churn_prediction_model.pkl is placed at that path.\n\nError: {e}"
    )
    st.stop()

# Pull the exact categories the model was trained on directly from the
# fitted pipeline, so the form options always match the model.

preprocessor = model.named_steps["preprocessor"]
cat_cols = preprocessor.transformers_[1][2]
ohe = preprocessor.named_transformers_["cat"].named_steps["encoder"]
CATEGORIES = {col: list(cats) for col, cats in zip(cat_cols, ohe.categories_)}

num_cols = preprocessor.transformers_[0][2]
scaler = preprocessor.named_transformers_["num"].named_steps["scaler"]
NUM_DEFAULTS = {col: float(mean) for col, mean in zip(num_cols, scaler.mean_)}


def yn(col, label, default="No", key=None):
    options = CATEGORIES[col]
    return st.selectbox(label, options, index=options.index(default) if default in options else 0, key=key)


# --------------------------------------------------
# DEFAULTS FOR EVERYTHING NOT SHOWN IN THE MAIN FORM
# --------------------------------------------------
# City is intentionally left out of the UI entirely and set to a value
# the encoder has never seen — OneHotEncoder(handle_unknown="ignore")
# then contributes nothing for that feature, instead of unfairly
# weighting the prediction toward one specific city.

DEFAULTS = {
    "senior_citizen": "No",
    "number_of_dependents": int(round(NUM_DEFAULTS["number_of_dependents"])),
    "City": "__not_in_training_data__",
    "Population": int(NUM_DEFAULTS["Population"]),
    "referred_a_friend": "No",
    "number_of_referrals": int(round(NUM_DEFAULTS["number_of_referrals"])),
    "avg_monthly_long_distance_charges": round(NUM_DEFAULTS["avg_monthly_long_distance_charges"], 2),
    "multiple_lines": "No",
    "internet_service": "Yes",
    "avg_monthly_gb_download": int(round(NUM_DEFAULTS["avg_monthly_gb_download"])),
    "online_backup": "No",
    "device_protection_plan": "No",
    "premium_tech_support": "No",
    "streaming_movies": "No",
    "streaming_music": "No",
    "unlimited_data": "Yes",
    "paperless_billing": "Yes",
    "total_refunds": round(NUM_DEFAULTS["total_refunds"], 2),
    "total_extra_data_charges": round(NUM_DEFAULTS["total_extra_data_charges"], 2),
    "total_long_distance_charges": round(NUM_DEFAULTS["total_long_distance_charges"], 2),
    "total_revenue": round(NUM_DEFAULTS["total_revenue"], 2),
}

# --------------------------------------------------
# FORM — key factors only
# --------------------------------------------------

with st.form("prediction_form"):

    # ---------- Customer Profile ----------
    st.markdown(
        '<div class="section-block"><h4 class="block-title">Customer Information</h4>',
        unsafe_allow_html=True
    )
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        gender = st.selectbox("Gender", CATEGORIES["Gender"])
    with p2:
        age = st.number_input("Age", min_value=18, max_value=100, value=int(NUM_DEFAULTS["Age"]))
    with p3:
        married = yn("Married", "Married")
    with p4:
        dependents = yn("Dependents", "Dependents")
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- Account & Contract ----------
    st.markdown(
        '<div class="section-block"><h4 class="block-title">Subscription Details</h4>',
        unsafe_allow_html=True
    )
    a1, a2, a3, a4 = st.columns(4)
    with a1:
        tenure_in_months = st.slider("Tenure (Months)", 0, 72, value=int(round(NUM_DEFAULTS["tenure_in_months"])))
    with a2:
        contract = st.selectbox("Contract", CATEGORIES["Contract"])
    with a3:
        payment_method = st.selectbox("Payment Method", CATEGORIES["payment_method"])
    with a4:
        offer = st.selectbox("Offer", CATEGORIES["Offer"])
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- Services ----------
    st.markdown(
        '<div class="section-block"><h4 class="block-title">Service Preferences</h4>',
        unsafe_allow_html=True
    )
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        internet_type = st.selectbox("Internet Type", CATEGORIES["internet_type"])
    with s2:
        phone_service = yn("phone_service", "Phone Service", default="Yes")
    with s3:
        online_security = yn("online_security", "Online Security")
    with s4:
        streaming_tv = yn("streaming_tv", "Streaming TV")
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- Billing ----------
    st.markdown(
        '<div class="section-block"><h4 class="block-title">Billing Information</h4>',
        unsafe_allow_html=True
    )
    b1, b2 = st.columns(2)
    with b1:
        monthly_charge = st.number_input(
            "Monthly Charge ($)", min_value=0.0, max_value=200.0,
            value=round(NUM_DEFAULTS["monthly_charge"], 2), step=0.5
        )
    with b2:
        satisfaction_score = st.slider("Satisfaction Score", 1, 5, value=int(round(NUM_DEFAULTS["satisfaction_score"])))
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- optional advanced fields ----------
    with st.expander("Additional details (optional — sensible defaults are already filled in)"):

        st.markdown("**More Profile Details**")
        e1, e2, e3 = st.columns(3)
        with e1:
            senior_citizen = yn("senior_citizen", "Senior Citizen", default=DEFAULTS["senior_citizen"])
        with e2:
            number_of_dependents = st.number_input(
                "Number of Dependents", min_value=0, max_value=10,
                value=DEFAULTS["number_of_dependents"]
            )
        with e3:
            population = st.number_input(
                "City Population", min_value=0, max_value=200000,
                value=DEFAULTS["Population"], step=100
            )

        st.markdown("**More Account Details**")
        e4, e5 = st.columns(2)
        with e4:
            referred_a_friend = yn("referred_a_friend", "Referred a Friend", default=DEFAULTS["referred_a_friend"])
        with e5:
            number_of_referrals = st.number_input(
                "Number of Referrals", min_value=0, max_value=20,
                value=DEFAULTS["number_of_referrals"]
            )

        st.markdown("**More Services**")
        e6, e7, e8, e9 = st.columns(4)
        with e6:
            internet_service = yn("internet_service", "Internet Service", default=DEFAULTS["internet_service"])
        with e7:
            multiple_lines = yn("multiple_lines", "Multiple Lines", default=DEFAULTS["multiple_lines"])
        with e8:
            online_backup = yn("online_backup", "Online Backup", default=DEFAULTS["online_backup"])
        with e9:
            device_protection_plan = yn("device_protection_plan", "Device Protection", default=DEFAULTS["device_protection_plan"])

        e10, e11, e12, e13 = st.columns(4)
        with e10:
            premium_tech_support = yn("premium_tech_support", "Premium Tech Support", default=DEFAULTS["premium_tech_support"])
        with e11:
            streaming_movies = yn("streaming_movies", "Streaming Movies", default=DEFAULTS["streaming_movies"])
        with e12:
            streaming_music = yn("streaming_music", "Streaming Music", default=DEFAULTS["streaming_music"])
        with e13:
            unlimited_data = yn("unlimited_data", "Unlimited Data", default=DEFAULTS["unlimited_data"])

        avg_monthly_gb_download = st.number_input(
            "Avg Monthly GB Download", min_value=0, max_value=200,
            value=DEFAULTS["avg_monthly_gb_download"]
        )

        st.markdown("**More Billing Details**")
        e14, e15, e16 = st.columns(3)
        with e14:
            paperless_billing = yn("paperless_billing", "Paperless Billing", default=DEFAULTS["paperless_billing"])
        with e15:
            avg_monthly_long_distance_charges = st.number_input(
                "Avg Monthly Long Distance Charges ($)", min_value=0.0, max_value=100.0,
                value=DEFAULTS["avg_monthly_long_distance_charges"], step=0.5
            )
        with e16:
            total_long_distance_charges = st.number_input(
                "Total Long Distance Charges ($)", min_value=0.0, max_value=10000.0,
                value=DEFAULTS["total_long_distance_charges"], step=10.0
            )

        e17, e18, e19 = st.columns(3)
        with e17:
            total_refunds = st.number_input(
                "Total Refunds ($)", min_value=0.0, max_value=500.0,
                value=DEFAULTS["total_refunds"], step=1.0
            )
        with e18:
            total_extra_data_charges = st.number_input(
                "Total Extra Data Charges ($)", min_value=0.0, max_value=500.0,
                value=DEFAULTS["total_extra_data_charges"], step=1.0
            )
        with e19:
            total_revenue = st.number_input(
                "Total Revenue ($)", min_value=0.0, max_value=20000.0,
                value=DEFAULTS["total_revenue"], step=10.0
            )

    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    submitted = st.form_submit_button("Predict Churn", use_container_width=True)

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if submitted:

    age_group = pd.cut(
        [age], bins=[18, 30, 45, 60, 100],
        labels=["18-30", "31-45", "46-60", "60+"]
    )[0]

    tenure_group = pd.cut(
        [tenure_in_months], bins=[0, 12, 36, 72],
        labels=["New", "Regular", "Loyal"], include_lowest=True
    )[0]

    input_row = pd.DataFrame([{
        "Gender": gender,
        "Age": age,
        "senior_citizen": senior_citizen,
        "Married": married,
        "Dependents": dependents,
        "number_of_dependents": number_of_dependents,
        "City": DEFAULTS["City"],
        "Population": population,
        "referred_a_friend": referred_a_friend,
        "number_of_referrals": number_of_referrals,
        "tenure_in_months": tenure_in_months,
        "Offer": offer,
        "phone_service": phone_service,
        "avg_monthly_long_distance_charges": avg_monthly_long_distance_charges,
        "multiple_lines": multiple_lines,
        "internet_service": internet_service,
        "internet_type": internet_type,
        "avg_monthly_gb_download": avg_monthly_gb_download,
        "online_security": online_security,
        "online_backup": online_backup,
        "device_protection_plan": device_protection_plan,
        "premium_tech_support": premium_tech_support,
        "streaming_tv": streaming_tv,
        "streaming_movies": streaming_movies,
        "streaming_music": streaming_music,
        "unlimited_data": unlimited_data,
        "Contract": contract,
        "paperless_billing": paperless_billing,
        "payment_method": payment_method,
        "monthly_charge": monthly_charge,
        "total_refunds": total_refunds,
        "total_extra_data_charges": total_extra_data_charges,
        "total_long_distance_charges": total_long_distance_charges,
        "total_revenue": total_revenue,
        "satisfaction_score": satisfaction_score,
        "age_group": age_group,
        "tenure_group": tenure_group,
    }])

    prediction = model.predict(input_row)[0]
    probability = model.predict_proba(input_row)[0][1]  # probability of "Yes" (churn)

    if probability <= 0.30:
        risk_level, risk_class = "Low", "risk-low"
    elif probability <= 0.70:
        risk_level, risk_class = "Medium", "risk-medium"
    else:
        risk_level, risk_class = "High", "risk-high"

    churn_class = "churn-yes" if prediction == "Yes" else "churn-no"

    st.markdown('<p class="block-heading">Prediction</p>', unsafe_allow_html=True)

    result_col, gauge_col = st.columns([1, 1])

    with result_col:
        st.markdown(f"""
        <div class="result-card {churn_class}">
            <div class="result-label">Predicted Outcome</div>
            <div class="result-value">{"Likely to Churn" if prediction == "Yes" else "Likely to Stay"}</div>
            <span class="risk-badge {risk_class}">{risk_level} Risk</span>
        </div>
        """, unsafe_allow_html=True)

        m1, m2 = st.columns(2)
        m1.metric("Churn Probability", f"{probability*100:.1f}%")
        m2.metric("Retention Probability", f"{(1-probability)*100:.1f}%")

    with gauge_col:
        recommendations = []

        # 1. Satisfaction Score
        if satisfaction_score <= 2:
            recommendations.append(
                "Schedule a customer support follow-up to address customer concerns."
            )

        # 2. Contract
        if contract.lower() == "month-to-month":
            recommendations.append(
                "Recommend upgrading to a One-Year or Two-Year contract to improve customer retention."
            )

        # 3. Monthly Charge
        if monthly_charge >= 80:
            recommendations.append(
                "Offer a loyalty discount or suggest a more cost-effective pricing plan."
            )

        # 4. Tenure
        if tenure_in_months < 12:
            recommendations.append(
                "Provide a welcome retention offer or onboarding support."
            )

        # 5. Online Security
        if online_security == "No":
            recommendations.append(
                "Recommend adding Online Security services to increase customer value."
            )

        # 6. Premium Tech Support
        if premium_tech_support == "No":
            recommendations.append(
                "Suggest upgrading to Premium Tech Support for improved customer experience."
            )

        # 7. Entertainment bundle
        if streaming_tv == "No" and streaming_movies == "No":
            recommendations.append(
                "Consider offering bundled entertainment services to increase customer engagement."
            )

        # Fallback messaging by risk tier
        if not recommendations:
            if risk_level == "Low":
                recommendations.append(
                    "No major risk factors detected — maintain standard engagement and monitor at the next billing cycle."
                )
            else:
                recommendations.append(
                    "Risk is elevated based on the model's overall assessment — a general retention check-in is recommended."
                )

        risk_dot_class = risk_class.replace("risk-", "")
        items_html = "".join(
            f'<div class="reco-item"><span class="reco-dot {risk_dot_class}"></span><span>{rec}</span></div>'
            for rec in recommendations
        )

        st.markdown(f"""
        <div class="reco-panel">
            <div class="reco-title">Recommended Actions</div>
            {items_html}
        </div>
        """, unsafe_allow_html=True)
