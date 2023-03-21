import streamlit as st
import pandas as pd

# App title
st.title("Mortality Review Meeting Action Log")

# Input patient information
st.subheader("Patient Information")
patient_id = st.text_input("Patient ID")
patient_name = st.text_input("Patient Name")
age = st.number_input("Age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Gender", options=["Male", "Female", "Other"])

# Input mortality information
st.subheader("Mortality Information")
cause_of_death = st.text_input("Cause of Death")
contributing_factors = st.text_area("Contributing Factors", height=100)

# Input actions for improvement
st.subheader("Actions for Improvement")
action = st.text_input("Action")
responsible_person = st.text_input("Responsible Person")
due_date = st.date_input("Due Date")

# Save the input data
if st.button("Save"):
    data = {
        "Patient ID": patient_id,
        "Patient Name": patient_name,
        "Age": age,
        "Gender": gender,
        "Cause of Death": cause_of_death,
        "Contributing Factors": contributing_factors,
        "Action": action,
        "Responsible Person": responsible_person,
        "Due Date": due_date,
    }
    df = pd.DataFrame(data, index=[0])

    # Display the saved data
    st.write("Saved Data:")
    st.write(df)

# Run the app with the following command: streamlit run app.py
