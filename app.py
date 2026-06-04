import streamlit as st
import pickle
import numpy as np

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Salary Prediction System",
    page_icon="💰",
    layout="wide"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#1f4e79;
}

.subtitle {
    text-align:center;
    color:gray;
    font-size:18px;
}

.prediction-box {
    background: linear-gradient(to right, #4facfe, #00f2fe);
    padding:20px;
    border-radius:15px;
    color:white;
    text-align:center;
    box-shadow:0px 4px 10px rgba(0,0,0,0.2);
}

.info-box {
    background-color:white;
    padding:15px;
    border-radius:12px;
    box-shadow:0px 4px 8px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Load Model
# ----------------------------
with open("salary_pred1.pkl", "rb") as file:
    model = pickle.load(file)

# ----------------------------
# Header
# ----------------------------
st.markdown(
    "<div class='title'>💰 Salary Prediction System</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Predict Employee Salary using Machine Learning</div>",
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
    width=150
)

st.sidebar.title("👤 Employee Profile")

name = st.sidebar.text_input("Name")
age = st.sidebar.number_input("Age", 18, 100, 25)
occupation = st.sidebar.text_input("Occupation")

# ----------------------------
# Main Section
# ----------------------------
col1, col2 = st.columns(2)

with col1:

    st.markdown("### 📊 Input Details")

    experience = st.slider(
        "Years of Experience",
        0.0,
        20.0,
        1.0,
        0.5
    )

    st.write(f"Selected Experience: **{experience} Years**")

    predict = st.button(
        "🚀 Predict Salary",
        use_container_width=True
    )

with col2:

    st.markdown("### ℹ Employee Information")

    st.markdown(f"""
    <div class='info-box'>
    <h4>👤 Name: {name}</h4>
    <h4>🎂 Age: {age}</h4>
    <h4>💼 Occupation: {occupation}</h4>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------
# Prediction
# ----------------------------
if predict:

    if not name or not occupation:
        st.warning("Please fill all employee details.")
    else:

        salary = model.predict(
            np.array([[experience]])
        )[0]

        st.balloons()

        st.markdown("## 🎯 Prediction Result")

        st.markdown(
            f"""
            <div class='prediction-box'>
                <h2>Predicted Salary</h2>
                <h1>₹ {salary:,.2f}</h1>
                <p>Based on {experience} years of experience</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success(
            f"{name}'s estimated salary is ₹ {salary:,.2f}"
        )

# Footer
st.markdown("---")
st.caption(
    "Developed using Machine Learning, Scikit-Learn and Streamlit"
)