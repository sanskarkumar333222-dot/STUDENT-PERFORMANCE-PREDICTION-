import streamlit as st
import pickle
import numpy as np

st.title("Student Performance Prediction")
st.write("Enter student details to predict the Final Grade")

# load model and feature list
with open('../Model/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('../Model/features.pkl', 'rb') as f:
    feature_cols = pickle.load(f)

# input fields
gender = st.selectbox("Gender", ["Male", "Female"])
attendance = st.slider("Attendance Rate (%)", 0, 100, 80)
study_hours = st.slider("Study Hours Per Week", 0, 20, 5)
previous_grade = st.number_input("Previous Grade", min_value=0, max_value=100, value=70)
extracurricular = st.slider("Extracurricular Activities (count)", 0, 5, 1)
parental_support = st.selectbox("Parental Support", ["Low", "Medium", "High"])
online_classes = st.selectbox("Took Online Classes?", ["Yes", "No"])

# encode inputs same way as training
gender_enc = 1 if gender == "Male" else 0
parental_enc = {"Low": 0, "Medium": 1, "High": 2}[parental_support]
online_enc = 1 if online_classes == "Yes" else 0
academic_index = attendance + study_hours

# make prediction
if st.button("Predict"):
    input_data = [gender_enc, attendance, study_hours, previous_grade,
                  extracurricular, parental_enc, online_enc, academic_index]
    
    input_array = np.array([input_data])
    prediction = model.predict(input_array)[0]
    
    st.success(f"Predicted Final Grade: {round(prediction, 1)}")
    
    if prediction >= 80:
        st.write("Performance: Good")
    elif prediction >= 60:
        st.write("Performance: Average")
    else:
        st.write("Performance: Needs Improvement")
