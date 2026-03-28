import streamlit as st

st.title("AI Money Mentor 💰")

salary = st.number_input("Enter your monthly salary")
expenses = st.number_input("Enter your monthly expenses")

if st.button("Generate Plan"):
    savings = salary - expenses
    
    if savings <= 0:
        st.write("You are overspending! Reduce expenses.")
    else:
        st.write(f"You can save ₹{savings} per month.")
        st.write(f"Suggested SIP: ₹{savings * 0.5}")
        st.write("Invest in mutual funds and keep emergency fund.")