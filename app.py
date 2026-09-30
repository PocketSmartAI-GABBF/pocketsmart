import streamlit as st

# Page Configuration
st.set_page_config(page_title="Pocket Smart AI", page_icon="💰", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; background-color: #4CAF50; color: white; font-size: 16px; border-radius: 8px; }
    .metric-card { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("💰 Pocket Smart AI")
st.subheader("Your Smart Budget & Recommendations Assistant")
st.write("Welcome! Manage your monthly expenses and get smart financial recommendations instantly.")

# Sidebar for User Inputs
st.sidebar.header("📊 Input Your Details")
monthly_income = st.sidebar.number_input("Monthly Income (₹)", min_value=0.0, value=30000.0, step=1000.0)
rent_expense = st.sidebar.number_input("Rent / Housing (₹)", min_value=0.0, value=8000.0, step=500.0)
food_expense = st.sidebar.number_input("Food & Groceries (₹)", min_value=0.0, value=6000.0, step=500.0)
utilities_expense = st.sidebar.number_input("Utilities & Bills (₹)", min_value=0.0, value=2000.0, step=100.0)
entertainment_expense = st.sidebar.number_input("Entertainment & Shopping (₹)", min_value=0.0, value=3000.0, step=100.0)

# Calculate Totals
total_expenses = rent_expense + food_expense + utilities_expense + entertainment_expense
savings = monthly_income - total_expenses
savings_percentage = (savings / monthly_income) * 100 if monthly_income > 0 else 0

# Main Dashboard
st.markdown("---")
col1, col2, col3 = st.columns(3)

col1.metric("Total Income", f"₹{monthly_income:,.2f}")
col2.metric("Total Expenses", f"₹{total_expenses:,.2f}")
col3.metric("Net Savings", f"₹{savings:,.2f}", delta=f"{savings_percentage:.1f}%")

st.markdown("---")

# Smart Recommendations Engine
st.infotable = st.header("🤖 AI Smart Recommendations")

if st.button("Generate Smart Analysis"):
    if monthly_income <= 0:
        st.error("Please enter a valid monthly income.")
    else:
        # Budget breakdown advice
        if savings < 0:
            st.error("⚠️ **Alert:** Your expenses are exceeding your income! You need to cut down non-essential spending immediately.")
        elif savings_percentage < 20:
            st.warning("⚠️ **Warning:** Your savings rate is below 20%. Try to follow the 50/30/20 rule (50% Needs, 30% Wants, 20% Savings).")
        else:
            st.success("🎉 **Great Job!** You have a healthy savings rate. Keep maintaining your budget!")
            
        # Specific category insights
        st.subheader("💡 Personalized Tips:")
        if food_expense > (monthly_income * 0.3):
            st.write("- **Food Spending:** Your food and grocery expenses are quite high relative to your income. Consider cooking at home more often.")
        if entertainment_expense > (monthly_income * 0.2):
            st.write("- **Entertainment:** You are spending a lot on entertainment. Try setting a stricter weekly limit.")
        if savings > 0:
            st.write(f"- **Investment Tip:** Since you are saving ₹{savings:,.2f} this month, consider investing a portion of it in Mutual Funds or a Fixed Deposit.")
            
        st.balloons()