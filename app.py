import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

# Set Streamlit page settings
st.set_page_config(page_title="Kragle Investment Advisor 💰", layout="centered")
st.title("Kragle Investment Advisor 💰")

# File uploader
uploaded_file = st.file_uploader("Upload Kragle Dataset CSV", type=["csv"])

if uploaded_file is not None:
    # Load CSV
    df = pd.read_csv(uploaded_file)
    st.success("CSV file loaded successfully!")
    st.dataframe(df.head())

    # Show column names to debug
    st.write("Detected columns:", df.columns.tolist())

    required_columns = ['Budget (USD)', 'Risk_Level', 'Investment_Horizon (Years)', 'Investment_Type']

    # Validate required columns
    if all(col in df.columns for col in required_columns):
        # Label encoders
        le_risk = LabelEncoder()
        le_type = LabelEncoder()

        df['Risk_Level'] = le_risk.fit_transform(df['Risk_Level'])
        df['Investment_Type'] = le_type.fit_transform(df['Investment_Type'])

        # Split into features and label
        X = df[['Budget (USD)', 'Risk_Level', 'Investment_Horizon (Years)']]
        y = df['Investment_Type']

        # Train model
        model = LogisticRegression(max_iter=200)
        model.fit(X, y)

        # Sidebar Inputs
        st.sidebar.header("Input Features")

        budget = st.sidebar.selectbox("Select Budget (USD)", sorted(df['Budget (USD)'].unique()))
        risk = st.sidebar.selectbox("Select Risk Level", le_risk.classes_)
        horizon = st.sidebar.selectbox("Select Investment Horizon (Years)", sorted(df['Investment_Horizon (Years)'].unique()))

        # Create prediction input
        input_data = pd.DataFrame({
            'Budget (USD)': [budget],
            'Risk_Level': le_risk.transform([risk]),
            'Investment_Horizon (Years)': [horizon]
        })

        # Predict
        prediction = model.predict(input_data)
        predicted_label = le_type.inverse_transform(prediction)

        # Show result
        st.subheader("Predicted Investment Type:")
        st.success(predicted_label[0])
    else:
        st.error("❌ Your CSV is missing one or more required columns:")
        for col in required_columns:
            if col not in df.columns:
                st.markdown(f"- `{col}` is missing.")
else:
    st.warning("📂 Please upload a Kragle dataset CSV to proceed.")
