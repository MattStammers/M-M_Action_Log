import streamlit as st
import pandas as pd

# Create a function to save the data to a CSV file
def save_data_to_csv(data):
    data.to_csv("patient_mdt_data.csv", index=False)

# Load existing data or create a new DataFrame
try:
    patient_mdt_data = pd.read_csv("patient_mdt_data.csv")
except FileNotFoundError:
    patient_mdt_data = pd.DataFrame(columns=["Patient ID", "Name", "DOB", "Action", "Timestamp"])

st.set_page_config(page_title="Patient Mortality MDT Tracker", layout="wide")
st.title("Patient Mortality MDT Tracker")

# Create a multi-page app
page = st.sidebar.selectbox("Choose a page", ["Action Log", "Enter Patient Details"])

if page == "Action Log":
    st.header("Action Log")
    st.write(patient_mdt_data)
elif page == "Enter Patient Details":
    st.header("Enter Patient Details")
    with st.form("patient_form"):
        patient_id = st.text_input("Patient ID")
        patient_name = st.text_input("Name")
        patient_dob = st.date_input("Date of Birth")
        patient_action = st.text_input("Action")
        patient_timestamp = st.date_input("Timestamp")

        submit_button = st.form_submit_button("Submit")
        
        if submit_button and patient_id and patient_name and patient_dob and patient_action and patient_timestamp:
            new_data = {"Patient ID": patient_id, "Name": patient_name, "DOB": patient_dob,
                        "Action": patient_action, "Timestamp": patient_timestamp}
            patient_mdt_data = patient_mdt_data.append(new_data, ignore_index=True)
            save_data_to_csv(patient_mdt_data)
            st.success("Data successfully saved.")
