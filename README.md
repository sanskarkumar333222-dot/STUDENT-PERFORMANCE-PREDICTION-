# Student Performance Prediction System

AIML Summer Internship 2026
IIHMF, MNNIT Allahabad, Prayagraj

---

## About the Project

This project predicts the Final Grade of a student based on factors like attendance, study hours, previous grade, parental support and extracurricular activities.

A web application is built using Streamlit where you can enter student details and get the predicted grade instantly.

---

## Dataset

- Source: Kaggle
- File: student_performance_updated_1000.csv
- Rows: 1000
- Columns: 12

Main features used:

- Gender
- Attendance Rate
- Study Hours Per Week
- Previous Grade
- Extracurricular Activities
- Parental Support
- Online Classes Taken

Target column: FinalGrade

---

## Machine Learning Models Used

1. Linear Regression
2. Random Forest Regressor
3. XGBoost Regressor

Best model: Random Forest Regressor (highest R2 score)

---

## Evaluation Metrics

Since this is a regression problem we used:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R2 Score

---

## Project Structure

```
Student_Performance_Prediction/
│
├── Dataset/
│   └── student_performance_updated_1000.csv
│
├── Notebook/
│   └── student_performance.ipynb
│
├── Model/
│   ├── model.pkl
│   └── features.pkl
│
├── Streamlit_App/
│   └── app.py
│
├── Documentation/
│
└── README.md
```

---

## How to Run

**Step 1 - Install libraries**

```
pip install pandas numpy matplotlib seaborn scikit-learn xgboost streamlit
```

**Step 2 - Run the notebook**

Open Notebook/student_performance.ipynb and run all cells

**Step 3 - Run the Streamlit app**

```
cd Streamlit_App
streamlit run app.py
```

Open browser at http://localhost:8501

---

## Team Details

- Internship: AIML Summer Internship 2026
- Institute: IIHMF, MNNIT Allahabad
- Project: Student Performance Prediction System
