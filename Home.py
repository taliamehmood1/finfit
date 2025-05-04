import streamlit as st

# This must be the very first Streamlit command


# Home UI
st.markdown("""
    <h1 style='text-align: center; color: #2E86C1;'>📊 Kragle Investment Advisor 💰</h1>
    <h3 style='text-align: center;'>Empowering Smart Financial Decisions with ML</h3>
""", unsafe_allow_html=True)



# Info box with expandable content
with st.expander("ℹ️ What is Kragle Investment Advisor?"):
    st.markdown("""
    Welcome! This app helps you choose the best investment type based on your:
    - 💵 Budget  
    - ⚠️ Risk Level  
    - 🕒 Investment Horizon  

    It uses machine learning to suggest suitable investment options.
    """)

# Navigation button
if st.button("🚀 Start Prediction"):
    st.switch_page("2_Kragle_Model.py")

# Footer or credits
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Developed with ❤️ for AF3005 – Spring 2025</p>", unsafe_allow_html=True)
