import streamlit as st
import pandas as pd

# Utility function to save the data
def save_data(data, session_state):
    if "data_df" in session_state:
        session_state.data_df = session_state.data_df.append(data, ignore_index=True)
    else:
        session_state.data_df = pd.DataFrame(data, index=[0])

# Main app
def main():
    st.title("Mortality Review Meeting Action Log")

    session_state = st.session_state(data_df=pd.DataFrame())

    # Menu to switch between pages
    menu = ["View Log", "Fill Details"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "View Log":
        view_log(session_state)
    elif choice == "Fill Details":
        fill_details(session_state)

# Page to view the log
def view_log(session_state):
    st.subheader("Mortality Review Log")
    if "data_df" in session_state and not session_state.data_df.empty:
        st.write(session_state.data_df)
    else:
        st.write("No data available. Please fill in the details first.")

# Page to fill in the details
def fill_details(session_state):
    st.subheader("Patient Information")
    patient_id = st.text_input("Patient ID")
    patient_name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    gender = st.selectbox("Gender", options=["Male", "Female", "Other"])

    st.subheader("Mortality Information")
    cause_of_death = st.text_input("Cause of Death")
    contributing_factors = st.text_area("Contributing Factors", height=100)

    st.subheader("Actions for Improvement")
    action = st.text_input("Action")
    responsible_person = st.text_input("Responsible Person")
    due_date = st.date_input("Due Date")

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
        save_data(data, session_state)
        st.success("Data saved successfully.")

if __name__ == "__main__":
    main()

# Run the app with the following command: streamlit run app.py
