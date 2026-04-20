
import streamlit as st
import pandas as pd
import joblib

# Load the best model
# Ensure the model file (Random_Forest_Regressor.pkl) is in the same directory as this app.py when deploying.
best_model = joblib.load('Random_Forest_Regressor.pkl')

# Set the title of the Streamlit app
st.title('Salary Prediction App')

st.write("Enter the employee's details to predict their salary.")

# Create input widgets for the features
age = st.slider('Age', 20, 60, 30)
gender_options = {'Male': 1, 'Female': 0}
gender = st.selectbox('Gender', list(gender_options.keys()))
education_level_options = {"Bachelor's": 0, "Master's": 1, "PhD": 2}
education_level = st.selectbox('Education Level', list(education_level_options.keys()))
job_title_dummy = st.number_input('Job Title (Encoded - 0 to 160)', min_value=0, max_value=160, value=70) # Using a dummy for now
years_of_experience = st.slider('Years of Experience', 0.0, 30.0, 5.0)

# Map selected values to numerical representation
gender_encoded = gender_options[gender]
education_level_encoded = education_level_options[education_level]

# Create a DataFrame for the input features
input_data = pd.DataFrame([[age, gender_encoded, education_level_encoded, job_title_dummy, years_of_experience]],
                            columns=['Age', 'Gender', 'Education Level', 'Job Title', 'Years of Experience'])

# Make prediction when button is clicked
if st.button('Predict Salary'):
    prediction = best_model.predict(input_data)[0]
    st.success(f'Predicted Salary: ${prediction:,.2f}')
