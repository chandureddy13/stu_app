import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load model, scaler, and label encoder
def load_model():
    with open("Linear_one", 'rb') as file:
        model, scalar, le = pickle.load(file)

        # Ensure LabelEncoder has predefined classes
        if not hasattr(le, "classes_"):
            le.classes_ = np.array(['no', 'yes'])  # Set known labels

        return model, scalar, le

# Preprocess user input data
def preprocessing_input_data(data, scalar, le):
    # Handle unseen labels in LabelEncoder
    if data['Extracurricular Activities'] not in le.classes_:
        le.classes_ = np.append(le.classes_, data['Extracurricular Activities'])

    # Transform categorical data
    data['Extracurricular Activities'] = le.transform([data['Extracurricular Activities']])[0]

    # Convert to DataFrame
    df = pd.DataFrame([data])
    
    # Standardize numerical values
    df_transformed = scalar.transform(df)
    
    return df_transformed

# Make predictions
def predict_data(data):
    model, scalar, le = load_model()
    processed_data = preprocessing_input_data(data, scalar, le)
    pred = model.predict(processed_data)
    return pred

# Streamlit UI
def main():
    st.title("Chandu's First Project")
    st.write("Enter your details below:")

    # User Inputs
    hours_studied = st.number_input("Hours Studied", min_value=1, max_value=10, value=5)
    previous_score = st.number_input("Previous Score", min_value=40, max_value=100, value=45)
    extra_curricular = st.selectbox("Extracurricular Activity", ['yes', 'no'])
    sleep_hours = st.number_input("Sleeping Hours", min_value=1, max_value=10, value=3)
    question_papers_solved = st.number_input("No of Question Papers Solved", min_value=1, max_value=10, value=5)

    # Prediction Button
    if st.button('Predict'):
        user_data = {
            "Hours Studied": hours_studied,
            "Previous Scores": previous_score,
            "Extracurricular Activities": extra_curricular,
            "Sleep Hours": sleep_hours,
            "Sample Question Papers Practiced": question_papers_solved,
        }

        prediction = predict_data(user_data)
        st.success(f"Your predicted score is: {prediction[0]:.2f}")

# Run the app
if __name__ == "__main__":
    main()
