# Need to install pip install pytest pytest-streamlit streamlit-hello

import pytest
import pandas as pd
from streamlit_hello import st_hello
from app import save_data_to_csv

@pytest.fixture(scope="module")
def test_data():
    data = pd.DataFrame(columns=["Patient ID", "Name", "DOB", "Action", "Timestamp"])
    new_data = {"Patient ID": "P01", "Name": "John Doe", "DOB": "1990-01-01",
                "Action": "Review", "Timestamp": "2023-03-21"}
    data = data.append(new_data, ignore_index=True)
    return data

def test_save_data_to_csv(test_data):
    save_data_to_csv(test_data)
    loaded_data = pd.read_csv("patient_mdt_data.csv")
    assert loaded_data.equals(test_data), "Data not saved or loaded correctly"

@st_hello
def test_form_submission():
    # Import Streamlit and your app
    import streamlit as st
    from app import app

    # Set up the test
    with st.beta_container():
        st.subheader("Test Form Submission")

        with st.form("test_form"):
            patient_id = st.text_input("Patient ID", "P02")
            patient_name = st.text_input("Name", "Jane Doe")
            patient_dob = st.date_input("Date of Birth", "1992-02-02")
            patient_action = st.text_input("Action", "Assess")
            patient_timestamp = st.date_input("Timestamp", "2023-03-22")

            submit_button = st.form_submit_button("Submit Test")

        if submit_button:
            new_data = {"Patient ID": patient_id, "Name": patient_name, "DOB": patient_dob,
                        "Action": patient_action, "Timestamp": patient_timestamp}
            test_data = pd.read_csv("patient_mdt_data.csv")
            test_data = test_data.append(new_data, ignore_index=True)
            save_data_to_csv(test_data)
            st.success("Test data successfully saved.")
