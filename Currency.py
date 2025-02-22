import streamlit as st

# Updated exchange rates as of February 22, 2025
EXCHANGE_RATES = {
    "Chinese Yuan (CNY)": 38.56,  # 1 PKR = 0.02596 CNY
    "Russian Ruble (RUB)": 3.16,   # 1 PKR = 0.302 RUB
    "British Pound (GBP)": 353.16,  # 1 PKR = 0.0043 GBP
    "Indian Rupee (INR)": 3.23,    # 1 PKR = 0.245 INR
    "Japanese Yen (JPY)": 1.88    # 1 PKR = 0.5421 JPY
}

def convert_currency(amount, target_currency):
    rate = EXCHANGE_RATES.get(target_currency)
    if rate:
        return amount * rate
    else:
        return None

# Streamlit UI
st.set_page_config(page_title="Currency Converter", page_icon="💰", layout="centered")
st.title("💰 Currency Converter")

# Input panel
st.header("Convert Pakistani Rupees (PKR)")
amount = st.number_input("Enter Amount in PKR:", min_value=0.0, step=0.1)
currency = st.selectbox("Convert To:", list(EXCHANGE_RATES.keys()))

# Perform conversion
if st.button("Convert"):
    converted_amount = convert_currency(amount, currency)
    if converted_amount is not None:
        st.success(f"💰 {amount} PKR is equal to {converted_amount:.2f} {currency}")
    else:
        st.error("Currency not supported.")

# Custom Styling
st.markdown(
    """
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(to right, #ff9a9e, #fad0c4);
            color: white;
        }
        .stButton>button {
            background-color: #ff6f61;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #ff4a3d;
        }
    </style>
    """,
    unsafe_allow_html=True
)