import pickle
import streamlit as st

# Load the model and scaler using pickle from the saved .sav file
with open('heart_model_with_scaler.sav', 'rb') as file:
    saved_data = pickle.load(file)

model = saved_data['model']
scaler = saved_data['scaler']

# Example of using the model and scaler for predictions
def predict(features):
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)
    return prediction

# Streamlit UI for getting user input
st.title("Heart Disease Prediction")
age = st.number_input("Age")
sex = st.selectbox("Sex", [0, 1])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])

# Example feature input and prediction
if st.button('Predict'):
    features = [age, sex, cp]  # Add more feature inputs here
    result = predict(features)
    st.write(f"Prediction: {'Disease' if result[0] == 1 else 'No Disease'}")
