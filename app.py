import streamlit as st
import pandas as pd
import tensorflow as tf

# Load the trained attrition prediction model
model = tf.keras.models.load_model('model.h5')

# Define the Streamlit app
def main():
    # Set the app title and description
    st.title('Employee Attrition Prediction')
    st.write('This app predicts employee attrition based on input features.')

    # Create input fields for employee features
    age = st.slider('Age', 18, 70, 30)
    business_travel = st.selectbox('Business Travel', ['Travel_Frequently', 'Travel_Rarely', 'Non-Travel'])
    daily_rate = st.slider('Daily Rate', 0, 1500, 800)
    department = st.selectbox('Department', ['Research & Development', 'Sales'])
    distance_from_home = st.slider('Distance From Home', 0, 100, 50)
    education = st.slider('Education', 1, 5, 3)
    educationfield = st.slider('EducationField', 1, 5, 3)
    employeecount = st.slider('EmployeeCount', 1)
    environment_satisfaction = st.slider('Environment Satisfaction', 1, 4)
    gender = st.selectbox('Gender', ['Male', 'Female'])
    hourly_rate = st.slider('Hourly Rate', 1, 100, 50)
    job_involvement = st.slider('Job Involvement', 1, 4)
    job_level = st.slider('Job Level', 1, 5)
    job_role = st.slider('Job Role', 0, 10, 5)
    job_satisfaction = st.slider('Job Satisfaction', 1, 4)
    marital_status = st.selectbox('Marital Status', ['Married', 'Divorced', 'Single'])
    monthly_income = st.slider('Monthly Income', 1, 100000)
    monthly_rate = st.slider('Monthly Rate', 1, 100000)
    num_companies_worked = st.slider('Num Companies Worked', 1, 10)
    over18 = st.slider('Over18', 0, 1)
    over_time = st.selectbox('Over Time', ['No', 'Yes'])
    percent_salary_hike = st.slider('Percent Salary Hike', 1, 25)
    performance_rating = st.slider('Performance Rating', 1, 5)
    relationship_satisfaction = st.slider('Relationship Satisfaction', 1, 4)
    standard_hours = st.slider('Standard Hours', 80)
    stock_option_level = st.slider('Stock Option Level', 0, 3)
    total_working_years = st.slider('Total Working Years', 1, 50)
    training_times_last_year = st.slider('Training Times Last Year', 0, 10)
    work_life_balance = st.slider('Work Life Balance', 1, 4)
    years_at_company = st.slider('Years At Company', 1, 25)
    years_in_current_role = st.slider('Years In Current Role', 1, 15)
    years_since_last_promotion = st.slider('Years Since Last Promotion', 1, 15)
    years_with_curr_manager = st.slider('Years With Curr Manager', 1, 10)

    # Convert categorical input to numerical
    business_travel_dict = {'Travel_Frequently': 1, 'Travel_Rarely': 2, 'Non-Travel': 0}
    department_dict = {'Research & Development': 1, 'Sales': 2}
    gender_dict = {'Male': 0, 'Female': 1}
    over_time_dict = {'No': 0, 'Yes': 1}
    marital_status_dict = {'Married': 1, 'Divorced': 2, 'Single': 3}

    business_travel = business_travel_dict[business_travel]
    department = department_dict[department]
    gender = gender_dict[gender]
    over_time = over_time_dict[over_time]
    marital_status = marital_status_dict[marital_status]

    # Create a dataframe from user inputs
    
    input_data = pd.DataFrame({
        'Age': [age],
        'BusinessTravel': [business_travel],
        'DailyRate': [daily_rate],
        'Department': [department],
        'DistanceFromHome': [distance_from_home],
        'Education': [education],
        'EmployeeCount':[employeecount],
        'EducationField': [educationfield],
        'EnvironmentSatisfaction': [environment_satisfaction],
        'Gender': [gender],
        'HourlyRate': [hourly_rate],
        'JobInvolvement': [job_involvement],
        'JobLevel': [job_level],
        'JobRole': [job_role],
        'JobSatisfaction': [job_satisfaction],
        'MaritalStatus': [marital_status],
        'MonthlyIncome': [monthly_income],
        'MonthlyRate': [monthly_rate],
        'NumCompaniesWorked': [num_companies_worked],
        'Over18':[over18],
        'OverTime': [over_time],
        'PercentSalaryHike': [percent_salary_hike],
        'PerformanceRating': [performance_rating],
        'RelationshipSatisfaction': [relationship_satisfaction],
        'StandardHours': [standard_hours],
        'StockOptionLevel': [stock_option_level],
        'TotalWorkingYears': [total_working_years],
        'TrainingTimesLastYear': [training_times_last_year],
        'WorkLifeBalance': [work_life_balance],
        'YearsAtCompany': [years_at_company],
        'YearsInCurrentRole': [years_in_current_role],
        'YearsSinceLastPromotion': [years_since_last_promotion],
        'YearsWithCurrManager': [years_with_curr_manager]
    })

    # Make a prediction
    prediction = model.predict(input_data)

    # Display the prediction
    if prediction[0][0] > 0.5:
        st.write('Prediction: Employee will churn.')
    else:
        st.write('Prediction: Employee will stay.')

if __name__ == '__main__':
    main()
