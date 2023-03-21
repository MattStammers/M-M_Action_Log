import streamlit as st
import pandas as pd
import plotly.express as px

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

    # Create a bar chart showing the number of actions per patient
    actions_by_patient = patient_mdt_data["Patient ID"].value_counts().reset_index()
    actions_by_patient.columns = ["Patient ID", "Count"]
    fig1 = px.bar(actions_by_patient, x="Patient ID", y="Count", title="Number of Actions by Patient")
    st.plotly_chart(fig1)

    # Create a line chart showing the number of actions per date
    actions_by_date = patient_mdt_data["Timestamp"].value_counts().reset_index()
    actions_by_date.columns = ["Timestamp", "Count"]
    actions_by_date["Timestamp"] = pd.to_datetime(actions_by_date["Timestamp"])
    actions_by_date = actions_by_date.sort_values("Timestamp")
    fig2 = px.line(actions_by_date, x="Timestamp", y="Count", title="Number of Actions by Date")
    st.plotly_chart(fig2)

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