import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")


# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(
    open(
        f"C:/Users/srida/OneDrive/Desktop/saved models/diabetes_model.sav",
        "rb",
    )
)

heart_disease_model = pickle.load(
    open(
        f"C:/Users/srida/OneDrive/Desktop/saved models/heartdisease.sav",
        "rb",
    )
)

breast_model = pickle.load(
    open(
        f"C:/Users/srida/OneDrive/Desktop/saved models/breastcancer_model.sav",
        "rb",
    )
)
lung_cancer = pickle.load(
    open(
        f"C:/Users/srida/OneDrive/Desktop/saved models/lungcancer.sav",
        "rb",
    )
)

# sidebar for navigation
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction System",
        [
            "Diabetes Prediction",
            "Heart Disease Prediction",
            "Breast Cancer Detection",
            "Lung Cancer Detection",
        ],
        menu_icon="hospital-fill",
        icons=["activity", "heartbreak", "person", "heart", "lungs"],
        default_index=0,
    )


# Diabetes Prediction Page
if selected == "Diabetes Prediction":

    # page title
    st.title("Diabetes Prediction using ML")

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")

    with col2:
        Glucose = st.text_input("Glucose Level")

    with col3:
        BloodPressure = st.text_input("Blood Pressure value")

    with col1:
        SkinThickness = st.text_input("Skin Thickness value")

    with col2:
        Insulin = st.text_input("Insulin Level")

    with col3:
        BMI = st.text_input("BMI value")

    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")

    with col2:
        Age = st.text_input("Age of the Person")

    # code for Prediction
    diab_diagnosis = ""

    # creating a button for Prediction

    if st.button("Diabetes Test Result"):

        user_input = [
            Pregnancies,
            Glucose,
            BloodPressure,
            SkinThickness,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age,
        ]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = "The person is diabetic"
        else:
            diab_diagnosis = "The person is not diabetic"

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":

    # page title
    st.title("Heart Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")

    with col2:
        sex = st.text_input("Sex")

    with col3:
        cp = st.text_input("Chest Pain types")

    with col1:
        trestbps = st.text_input("Resting Blood Pressure")

    with col2:
        chol = st.text_input("Serum Cholestoral in mg/dl")

    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl")

    with col1:
        restecg = st.text_input("Resting Electrocardiographic results")

    with col2:
        thalach = st.text_input("Maximum Heart Rate achieved")

    with col3:
        exang = st.text_input("Exercise Induced Angina")

    with col1:
        oldpeak = st.text_input("ST depression induced by exercise")

    with col2:
        slope = st.text_input("Slope of the peak exercise ST segment")

    with col3:
        ca = st.text_input("Major vessels colored by flourosopy")

    with col1:
        thal = st.text_input(
            "thal: 0 = normal; 1 = fixed defect; 2 = reversable defect"
        )

    # code for Prediction
    heart_diagnosis = ""

    # creating a button for Prediction

    if st.button("Heart Disease Test Result"):

        user_input = [
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal,
        ]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = "The person is having heart disease"
        else:
            heart_diagnosis = "The person does not have any heart disease"

    st.success(heart_diagnosis)

if selected == "Breast Cancer Detection":

    # page title
    st.title("Breast Cancer Detection using ML")

    # Input fields for user data
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        mean_radius = st.text_input("Mean radius")

    with col2:
        mean_texture = st.text_input("Mean texture")

    with col3:
        mean_perimeter = st.text_input("Mean perimeter")

    with col4:
        mean_area = st.text_input("Mean area")

    with col5:
        mean_smoothness = st.text_input("Mean smoothness")

    with col1:
        mean_compactness = st.text_input("Mean compactness")

    with col2:
        mean_concavity = st.text_input("Mean concavity")

    with col3:
        mean_concave_points = st.text_input("Mean concave points")

    with col4:
        mean_symmetry = st.text_input("Mean symmetry")

    with col5:
        mean_fractal_dimension = st.text_input("Mean fractal dimension")

    with col1:
        radius_error = st.text_input("Radius error")

    with col2:
        texture_error = st.text_input("Texture error")

    with col3:
        perimeter_error = st.text_input("Perimeter error")

    with col4:
        area_error = st.text_input("Area error")

    with col5:
        smoothness_error = st.text_input("Smoothness error")

    with col1:
        compactness_error = st.text_input("Compactness error")

    with col2:
        concavity_error = st.text_input("Concavity error")

    with col3:
        concave_points_error = st.text_input("Concave points error")

    with col4:
        symmetry_error = st.text_input("Symmetry error")

    with col5:
        fractal_dimension_error = st.text_input("Fractal dimension error")

    with col1:
        worst_radius = st.text_input("Worst radius")

    with col2:
        worst_texture = st.text_input("Worst texture")

    with col3:
        worst_perimeter = st.text_input("Worst perimeter")

    with col4:
        worst_area = st.text_input("Worst area")

    with col5:
        worst_smoothness = st.text_input("Worst smoothness")

    with col1:
        worst_compactness = st.text_input("Worst compactness")

    with col2:
        worst_concavity = st.text_input("Worst concavity")

    with col3:
        worst_concave_points = st.text_input("Worst concave points")

    with col4:
        worst_symmetry = st.text_input("Worst symmetry")

    with col5:
        worst_fractal_dimension = st.text_input("Worst fractal dimension")

    # code for Prediction
    breast_cancer_diagnosis = ""

    # creating a button for Prediction
    if st.button("Breast Cancer Test Result"):

        user_input = [
            mean_radius,
            mean_texture,
            mean_perimeter,
            mean_area,
            mean_smoothness,
            mean_compactness,
            mean_concavity,
            mean_concave_points,
            mean_symmetry,
            mean_fractal_dimension,
            radius_error,
            texture_error,
            perimeter_error,
            area_error,
            smoothness_error,
            compactness_error,
            concavity_error,
            concave_points_error,
            symmetry_error,
            fractal_dimension_error,
            worst_radius,
            worst_texture,
            worst_perimeter,
            worst_area,
            worst_smoothness,
            worst_compactness,
            worst_concavity,
            worst_concave_points,
            worst_symmetry,
            worst_fractal_dimension,
        ]

        user_input = [float(x) for x in user_input]

        breast_cancer_prediction = breast_model.predict([user_input])

        if breast_cancer_prediction[0] == 1:
            breast_cancer_diagnosis = "The person has Breast cancer"
        else:
            breast_cancer_diagnosis = "The person does not have Breast cancer"

    st.success(breast_cancer_diagnosis)
if selected == "Lung Cancer Detection":

    # Page title
    st.title("Lung Cancer Detection using ML")

    # Input fields for user data
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        age = st.text_input("Age")

    with col2:
        smoking = st.selectbox("Smoking", [1, 2])

    with col3:
        yellow_fingers = st.selectbox("Yellow Fingers", [1, 2])

    with col4:
        anxiety = st.selectbox("Anxiety", [1, 2])

    with col5:
        peer_pressure = st.selectbox("Peer Pressure", [1, 2])

    with col1:
        chronic_disease = st.selectbox("Chronic Disease", [1, 2])

    with col2:
        fatigue = st.selectbox("Fatigue", [1, 2])

    with col3:
        allergy = st.selectbox("Allergy", [1, 2])

    with col4:
        wheezing = st.selectbox("Wheezing", [1, 2])

    with col5:
        alcohol_consuming = st.selectbox("Alcohol Consuming", [1, 2])

    with col1:
        coughing = st.selectbox("Coughing", [1, 2])

    with col2:
        shortness_of_breath = st.selectbox("Shortness of Breath", [1, 2])

    with col3:
        swallowing_difficulty = st.selectbox("Swallowing Difficulty", [1, 2])

    with col4:
        chest_pain = st.selectbox("Chest Pain", [1, 2])

    # Code for Prediction
    lung_cancer_diagnosis = ""

    # Creating a button for Prediction
    if st.button("Lung Cancer Test Result"):

        user_input = [
            age,
            smoking,
            yellow_fingers,
            anxiety,
            peer_pressure,
            chronic_disease,
            fatigue,
            allergy,
            wheezing,
            alcohol_consuming,
            coughing,
            shortness_of_breath,
            swallowing_difficulty,
            chest_pain,
        ]

        user_input = [int(x) for x in user_input]

        lung_cancer_prediction = lung_cancer.predict([user_input])

        if lung_cancer_prediction[0] == 1:
            lung_cancer_diagnosis = "The person has Lung cancer"
        else:
            lung_cancer_diagnosis = "The person does not have Lung cancer"

    st.success(lung_cancer_diagnosis)
