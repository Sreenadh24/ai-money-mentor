import streamlit as st
import pandas as pd

# 🎨 Background Style
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #dbeafe, #f0f9ff);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🏷️ Title
st.markdown("<h1 style='text-align: center;'>💰 AI Money Mentor</h1>", unsafe_allow_html=True)

# 📥 Input Section
col1, col2 = st.columns(2)

with col1:
    salary = st.number_input("Enter your monthly salary", min_value=0.0)

with col2:
    expenses = st.number_input("Enter your monthly expenses", min_value=0.0)

# 🚀 Button Action
if st.button("Generate Plan"):

    savings = salary - expenses

    st.subheader("📊 Results")

    # 💡 Savings Status
    if savings > 0:
        st.success(f"You can save ₹{savings:.2f} per month")
        sip = savings * 0.5
        st.info(f"Suggested SIP: ₹{sip:.2f}")
        st.write("💡 Invest in mutual funds and maintain an emergency fund.")

    elif savings == 0:
        st.warning("😐 No savings. Try reducing expenses.")

    else:
        st.error("⚠️ You are overspending! Please control expenses.")

    # 📊 Chart
    data = pd.DataFrame({
        'Category': ['Salary', 'Expenses'],
        'Amount': [salary, expenses]
    })

    st.bar_chart(data.set_index('Category'))
