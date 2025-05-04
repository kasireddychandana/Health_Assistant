import streamlit as st
import pickle
import numpy as np
import base64

# Function to set background image
def add_bg_image(img123):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    
    bg_image = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)

# Load all models
heart_model = pickle.load(open('Heart_model.sav', 'rb'))
hiv_model = pickle.load(open('HIV_model.sav', 'rb'))
skin_model = pickle.load(open('Skin_model.sav', 'rb'))
breast_model = pickle.load(open('Breast_model.sav', 'rb'))
corona_model = pickle.load(open('Corona_model.sav', 'rb'))
lung_model = pickle.load(open('Lung_model.sav', 'rb'))
obesity_model = pickle.load(open('obesity_model.sav', 'rb'))
prostate_model = pickle.load(open('Prostate_model.sav', 'rb'))
malaria_model = pickle.load(open('Malaria_model.sav', 'rb'))
diabetes_model = pickle.load(open('Diabetes_model.sav', 'rb'))

# UI styling
st.markdown("""
    <style>
        .stApp {
            padding: 2rem;
        }
        h1, h2, h3 {
            color: #ffffff;
            margin-bottom: 1.5rem;
            text-shadow: 2px 2px 4px #000000;
        }
        .sidebar .sidebar-content {
            background-color:  #ffffff;
        }
        .sidebar .sidebar-section {
            margin-bottom: 1.5rem;
        }
        .sidebar .sidebar-section h3 {
            color: #003366;
            font-size: 1rem;
            margin-bottom: 0.5rem;
            padding-bottom: 0.3rem;
            border-bottom: 1px solid #b3c6ff;
        }
        .stNumberInput, .stSelectbox, .stSlider, .stRadio {
            margin-bottom: 1.5rem;
        }
        .stButton button {
            background-color: #003366;
            color: white;
            padding: 0.75rem 2rem;
            border-radius: 0.5rem;
            font-weight: bold;
            margin-top: 1.5rem;
        }
        .stButton button:hover {
            background-color: #002244;
        }
        [data-testid="column"] {
            gap: 1.5rem;
        }
        .stAlert {
            margin-top: 1.5rem;
        }
        label {
            font-size: 1rem;
            font-weight: 500;
            margin-bottom: 0.5rem;
            display: block;
        }
        .input-section {
            margin-bottom: 2rem;
            padding: 1.5rem;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 0.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .home-card {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            margin-bottom: 2rem;
        }
        .home-card h1 {
            color: #003366;
            text-shadow: none;
        }
        .home-card p {
            color: #333;
            font-size: 1.1rem;
            line-height: 1.6;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 2rem;
        }
        .feature-card {
            background-color: rgba(0, 51, 102, 0.8);
            color: white;
            padding: 1.5rem;
            border-radius: 0.5rem;
            text-align: center;
            transition: transform 0.3s ease;
        }
        .feature-card:hover {
            transform: translateY(-5px);
        }
        .feature-card h3 {
            margin-top: 0;
            font-size: 1.2rem;
            color: white;
        }
        .get-started-btn {
            background-color: #ff6b6b;
            color: white;
            padding: 1rem 2rem;
            font-size: 1.2rem;
            border: none;
            border-radius: 0.5rem;
            cursor: pointer;
            margin-top: 2rem;
            display: inline-block;
            text-align: center;
            transition: background-color 0.3s ease;
        }
        .get-started-btn:hover {
            background-color: #ff5252;
        }
        /* Sidebar collapsible style */
        .css-1d391kg {
            padding-top: 3.5rem;
        }
        .sidebar-toggle {
            position: fixed;
            top: 0.5rem;
            left: 1rem;
            z-index: 999;
            padding: 0.5rem 1rem;
            background-color: #003366;
            color: white;
            border-radius: 0.5rem;
            font-weight: bold;
            cursor: pointer;
        }
        /* Button grid layout */
        .sidebar-buttons {
            display: grid;
            grid-template-columns: 1fr;
            gap: 0.5rem;
        }
        .sidebar-buttons button {
            width: 100%;
            margin-top: 0.25rem !important;
            margin-bottom: 0.25rem !important;
        }
        /* For two-column button layout */
        .sidebar-buttons-2col {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.5rem;
        }
        .sidebar-buttons-2col button {
            width: 100%;
            margin-top: 0.25rem !important;
            margin-bottom: 0.25rem !important;
            padding: 0.5rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'disease' not in st.session_state:
    st.session_state.disease = "Home"
if 'sidebar_visible' not in st.session_state:
    st.session_state.sidebar_visible = True

# Add sidebar toggle button
if st.button("☰", key="toggle_sidebar"):
    st.session_state.sidebar_visible = not st.session_state.sidebar_visible

# Enhanced Home Page
def home_page():
    # Set background image (you need to have the image file in your project directory)
    # Add background image (when you have the actual file)
    # add_bg_image("background.jpg")  # Uncomment this when you have the image file
    
    # Alternative: Add a placeholder colored background if image isn't available
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #0a2239 0%, #1d4e89 100%);
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="home-card">
            <h1>Welcome to the Disease Prediction System</h1>
            <p>This advanced AI-powered system helps healthcare professionals and individuals predict the likelihood of various diseases based on symptoms and medical data. Early detection can save lives - start exploring now!</p>
            
            <div class="feature-grid">
                <div class="feature-card">
                    <h3>Heart Disease</h3>
                    <p>Predict cardiovascular conditions based on patient data</p>
                </div>
                <div class="feature-card">
                    <h3>Diabetes</h3>
                    <p>Early detection of diabetes risk factors</p>
                </div>
                <div class="feature-card">
                    <h3>Cancer Screening</h3>
                    <p>Risk assessment for various types of cancer</p>
                </div>
                <div class="feature-card">
                    <h3>Infectious Diseases</h3>
                    <p>COVID-19, Malaria, HIV prediction models</p>
                </div>
            </div>
            
            <p style="margin-top:2rem;">Select a disease from the sidebar to begin your prediction journey.</p>
            
            <p style="font-size:0.9rem; margin-top:3rem; color:#666;">
                <b>Note:</b> This tool is for educational purposes and does not replace professional medical advice. Always consult healthcare professionals for diagnosis and treatment.
            </p>
        </div>
    """, unsafe_allow_html=True)

# Sidebar Disease Selection with Categories
if st.session_state.sidebar_visible:
    with st.sidebar:
        st.markdown("""
            <style>
                .sidebar-section {
                    margin-bottom: 1.5rem;
                }
                .sidebar-section h3 {
                    color: #003366;
                    font-size: 1rem;
                    margin-bottom: 0.5rem;
                    padding-bottom: 0.3rem;
                    border-bottom: 1px solid #b3c6ff;
                }
            </style>
        """, unsafe_allow_html=True)
        
        # Home button
        if st.button("🏠 Home"):
            st.session_state.disease = "Home"
            
        # Cardiovascular Diseases
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('### Cardiovascular Diseases')
        st.markdown('<div class="sidebar-buttons">', unsafe_allow_html=True)
        if st.button("Heart Disease"):
            st.session_state.disease = "Heart Disease"
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Metabolic & Endocrine Disorders
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('### Metabolic & Endocrine Disorders')
        st.markdown('<div class="sidebar-buttons-2col">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Diabetes"):
                st.session_state.disease = "Diabetes"
        with col2:
            if st.button("Obesity"):
                st.session_state.disease = "Obesity"
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Respiratory Diseases
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('### Respiratory Diseases')
        st.markdown('<div class="sidebar-buttons-2col">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Lung "):
                st.session_state.disease = "Lung Disease"
        with col2:
            if st.button("COVID-19"):
                st.session_state.disease = "COVID-19"
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Infectious Diseases
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('### Infectious Diseases')
        st.markdown('<div class="sidebar-buttons-2col">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("HIV/AIDS"):
                st.session_state.disease = "HIV"
        with col2:
            if st.button("Malaria"):
                st.session_state.disease = "Malaria"
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Cancers
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('### Cancers')
        st.markdown('<div class="sidebar-buttons">', unsafe_allow_html=True)
        if st.button("Breast Cancer"):
            st.session_state.disease = "Breast Cancer"
        if st.button("Prostate Cancer"):
            st.session_state.disease = "Prostate Cancer"
        if st.button("Skin Cancer"):
            st.session_state.disease = "Skin Disease"  # Using Skin Disease model for Skin Cancer
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Dermatological Conditions
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown('### Dermatological Conditions')
        st.markdown('<div class="sidebar-buttons">', unsafe_allow_html=True)
        if st.button("Skin Disease"):
            st.session_state.disease = "Skin Disease"
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Show home page or disease prediction page
if st.session_state.disease == "Home":
    home_page()
else:
    # Display selected disease
    st.subheader(f"{st.session_state.disease} Prediction")

    # Your existing check_inputs function
    def check_inputs(inputs):
        # Define default values: 0, 0.0, "No", "False", "", None
        default_values = [0, 0.0, "No", "False", "", None]
        
        # Check if all fields have the default values
        if all(val in default_values for val in inputs):
            return True
        
        # If only one value is entered (e.g., age) and others are default values, trigger an error
        non_default_inputs = [val for val in inputs if val not in default_values]
        if len(non_default_inputs) == 1:
            return False  # Only one input entered (partial input case)
        
        return False  # All required fields are filled or a combination of them is filled

    def show_popup_error(message):
        st.error("⚠️ " + message)

    # Rest of your existing disease prediction code blocks would follow...
    # (Heart Disease, Diabetes, Obesity, etc. prediction code sections remain the same)

# # For testing/debugging
# if __name__ == "__main__":
#     home_page()
# ==========================
# Heart Disease
# ==========================
# Heart Disease
if st.session_state.disease == "Heart Disease":
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.slider('Age', 1, 100, key='heart_age')
        with col2:
            cp = st.selectbox('Chest Pain Type (0-3)', [0, 1, 2, 3], key='heart_cp')
        with col3:
            trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=80, max_value=200, key='heart_trestbps')
            
        col1, col2, col3 = st.columns(3)
        with col1:
            chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=100, max_value=600, key='heart_chol')
        with col2:
            fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1], 
                              format_func=lambda x: "True" if x == 1 else "False", key='heart_fbs')
        with col3:
            thalach = st.number_input('Max Heart Rate Achieved', min_value=60, max_value=220, key='heart_thalach')

        col1, col2, col3 = st.columns(3)
        with col1:
            gender = st.radio("Gender", ["Female", "Male"], key='heart_gender')
            gender = 0 if gender == "Female" else 1
        with col2:
            restecg = st.selectbox('Resting ECG Results', [0, 1, 2], 
                                 format_func=lambda x: ["Normal", "ST-T abnormality", "Left ventricular hypertrophy"][x], 
                                 key='heart_restecg')
        with col3:
            exang = st.selectbox('Exercise Induced Angina', [0, 1], 
                               format_func=lambda x: "Yes" if x == 1 else "No", key='heart_exang')

        col1, col2, col3 = st.columns(3)
        with col1:
            oldpeak = st.number_input('ST Depression', min_value=0.0, max_value=6.0, step=0.1, key='heart_oldpeak')
        with col2:
            slope = st.selectbox('Slope of Peak Exercise ST', [0, 1, 2], 
                               format_func=lambda x: ["Upsloping", "Flat", "Downsloping"][x], key='heart_slope')
        with col3:
            ca = st.selectbox('Number of Major Vessels', [0, 1, 2, 3], key='heart_ca')

        col1, col2 = st.columns(2)
        with col1:
            thal = st.selectbox('Thalassemia', [0, 1, 2], 
                              format_func=lambda x: ["Normal", "Fixed Defect", "Reversible Defect"][x], key='heart_thal')
        
    # Only show the Heart Disease Prediction button for this section
    if st.button("Predict Heart Disease", key='heart_button'):
        inputs = [age, gender, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        if check_inputs(inputs):
            show_popup_error("Please change the values according to you.")
        else:
             if (cp == 0 or cp == 1) or age < 15:
                st.success("No Heart Disease Detected")   
             else:
                data = np.array([inputs])
                prediction = heart_model.predict(data)
                st.success("Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease Detected")

                                                                 

# ==========================
# Diabetes
elif st.session_state.disease == "Diabetes":
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.slider('Age', 1, 100, key='diabetes_age')
        with col2:
            bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1, key='diabetes_bmi')
        with col3:
            blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=60, max_value=200, key='diabetes_bp')
        
        col1, col2 = st.columns(2)
        with col1:
            glucose_level = st.number_input("Glucose Level (mg/dL)", min_value=50, max_value=300, key='diabetes_glucose')
        with col2:
            family_history = st.selectbox("Family History", [0, 1], 
                                        format_func=lambda x: "Yes" if x == 1 else "No", key='diabetes_family')

        with col1:
            gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Male" if x == 0 else "Female", key='diabetes_gender')
        with col2:
            physical_activity = st.selectbox("Physical Activity", [0, 1], format_func=lambda x: "None" if x == 0 else "Regular", key='diabetes_activity')
        with col1:
            diet = st.selectbox("Diet", [0, 1], format_func=lambda x: "Unhealthy" if x == 0 else "Healthy", key='diabetes_diet')

    # ✅ Move the button and logic inside the Diabetes block
    if st.button("Predict Diabetes", key='diabetes_button'):
        inputs = [age, bmi, blood_pressure, glucose_level, family_history, gender, physical_activity, diet]
        if check_inputs(inputs):  # If any input is missing
            show_popup_error("Please enter all values before prediction.")
        else:
            # Custom logic based on family history and age
            if family_history == 1:
                st.success("Diabetes Detected")
            elif age < 10:
                st.success("No Diabetes Detected")
            elif glucose_level < 80:
                st.success("No Diabetes Detected")
            else:
                result = diabetes_model.predict(np.array([inputs]))
                st.success("Diabetes Detected" if result[0] == 1 else "No Diabetes")

# ==========================
# Obesity
elif st.session_state.disease == "Obesity":
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.slider('Age', 1, 100, key='obesity_age')
        with col2:
            height = st.number_input("Height (m)", min_value=1.0, max_value=2.5, step=0.01, key='obesity_height')
        with col3:
            weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, step=0.1, key='obesity_weight')

        col1, col2, col3 = st.columns(3)
        with col1:
            physical_activity = st.slider("Physical Activity Level (0-10)", 0, 10, key='obesity_activity')
        with col2:
            junk_food_intake = st.slider("Junk Food Intake (0-10)", 0, 10, key='obesity_junkfood')
        with col3:
            bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, step=0.1, key='obesity_bmi')

    # ✅ Obesity button placed INSIDE the block
    if st.button("Predict Obesity", key='obesity_button'):
        inputs = [age, height, weight, physical_activity, junk_food_intake, bmi]
        if check_inputs(inputs):
            show_popup_error("Please enter all values before prediction.")
        else:
            # 🔍 Rule-based shortcuts
            if age < 5:
                st.success("No Obesity Detected")
            elif weight < 80:
                st.success("No Obesity Detected")
            elif junk_food_intake > 5:
                st.success("Obesity Detected")
            else:
                result = obesity_model.predict(np.array([inputs]))
                st.success("No Obesity" if result[0] == 1 else "Obesity Detected")


# ==========================
# Lung Disease
elif st.session_state.disease == "Lung Disease":
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            pains = st.selectbox("Body Pains", [0, 1], format_func=lambda x: "Yes" if x else "No", key='lung_pains')
        with col2:
            nasal_congestion = st.selectbox("Nasal Congestion", [0, 1], format_func=lambda x: "Yes" if x else "No", key='lung_nasal')
        with col3:
            runny_nose = st.selectbox("Runny Nose", [0, 1], format_func=lambda x: "Yes" if x else "No", key='lung_runny')

        col1, col2, col3 = st.columns(3)
        with col1:
            none_experiencing = st.selectbox("No Symptoms", [0, 1], format_func=lambda x: "Yes" if x else "No", key='lung_none')
        with col2:
            age = st.slider('Age', 1, 100, key='lung_age')
        with col3:
            gender = st.radio("Gender", ["Female", "Male"], key='lung_gender')
            gender = 0 if gender == "Female" else 1

        if st.button("Predict Lung Disease", key='lung_button'):
            inputs = [pains, nasal_congestion, runny_nose, none_experiencing, age, gender]
            if age < 10:
                st.success("No Lung Disease Detected")
            elif nasal_congestion == 0:
                st.success("No Lung Disease Detected")
            elif none_experiencing == 0:
                st.success("No Lung Disease Detected")
            else:
                result = lung_model.predict(np.array([inputs]))
                st.success("No Lung Disease" if result[0] == 1 else "Lung Disease Detected")

# ==========================
# COVID-19
elif st.session_state.disease == "COVID-19":
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            fever = st.radio("Fever", ["Yes", "No"], key='covid_fever') == "Yes"
            dry_cough = st.radio("Dry Cough", ["Yes", "No"], key='covid_cough') == "Yes"
            tiredness = st.radio("Tiredness", ["Yes", "No"], key='covid_tired') == "Yes"
        with col2:
            difficulty_breathing = st.radio("Difficulty Breathing", ["Yes", "No"], key='covid_breath') == "Yes"
            sore_throat = st.radio("Sore Throat", ["Yes", "No"], key='covid_throat') == "Yes"
        
        if st.button("Predict COVID-19", key='covid_button'):
            result = corona_model.predict(np.array([[fever, dry_cough, tiredness, difficulty_breathing, sore_throat]]))
            st.success("COVID-19 Detected" if result[0] == 1 else "No COVID-19")

# ==========================
# HIV
elif st.session_state.disease == "HIV":
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.slider("Age", 1, 100, key="hiv_age")
        with col2:
            gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Male" if x == 0 else "Female", key="hiv_gender")
        with col3:
            sexual_partners = st.number_input("Number of Sexual Partners", min_value=0, max_value=100, key="hiv_partners")

        col1, col2, col3 = st.columns(3)
        with col1:
            num_stds = st.number_input("Number of STDs Diagnosed", min_value=0, max_value=20, key="hiv_stds")
        with col2:
            cd4_count = st.number_input("CD4 Count", min_value=0, max_value=2000, key="hiv_cd4")
        with col3:
            viral_load = st.number_input("Viral Load", min_value=0, max_value=1000000, key="hiv_viral")

        if st.button('Predict HIV', key='hiv_button'):
            try:
                input_data = [age, gender, sexual_partners, num_stds, cd4_count, viral_load]

                # 🛑 Rule-based shortcuts
                if age < 15 and sexual_partners < 3:
                    st.success("HIV Negative")
                # elif age > 15:
                #     st.success("HIV Positive")
                elif sexual_partners > 3:
                    st.success("HIV Positive")
                else:
                    # 🧪 Fallback to ML model
                    result = hiv_model.predict(np.array([input_data]))
                    st.success("HIV Negative" if result[0] == 1 else "HIV Positive")

            except Exception as e:
                show_popup_error("An error occurred during prediction. Please check your inputs.")



# ==========================
# Malaria
elif st.session_state.disease == "Malaria":
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input("Age", min_value=0, max_value=120, key='malaria_age')
        with col2:
            gender = st.selectbox("Gender", ["Male", "Female"], key='malaria_gender')
            gender = 1 if gender == "Male" else 0
        with col3:
            fever = st.selectbox("Fever", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", key='malaria_fever')
        
        col1, col2, col3 = st.columns(3)
        with col1:
            headache = st.selectbox("Headache", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", key='malaria_headache')
        with col2:
            chills = st.selectbox("Chills", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", key='malaria_chills')
        with col3:
            sweats = st.selectbox("Sweats", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", key='malaria_sweats')

        col1, col2, col3 = st.columns(3)
        with col1:
            fatigue = st.selectbox("Fatigue", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", key='malaria_fatigue')
        with col2:
            hemoglobin = st.number_input("Hemoglobin (g/dL)", min_value=0.0, max_value=25.0, key='malaria_hemoglobin')
        with col3:
            platelet = st.number_input("Platelet (cells/μL)", min_value=0.0, step=100.0, key='malaria_platelet')

        col1, col2 = st.columns(2)
        with col1:
            wbc = st.number_input("WBC (cells/μL)", min_value=0.0, step=100.0, key='malaria_wbc')
        with col2:
            parasite = st.selectbox("Parasite Detected", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", key='malaria_parasite')

        # 🔘 Button only appears inside Malaria block
        if st.button("Predict Malaria", key='malaria_button'):
            if age == 0 and fever == 0 and headache == 0 and fatigue == 0:
                st.success("❌ No Malaria")
            else:
                inputs = [age, gender, fever, headache, chills, sweats, fatigue, hemoglobin, platelet, wbc, parasite]
                result = malaria_model.predict(np.array([inputs]))
                st.success("❌ No Malaria" if result[0] == 1 else "✅ Malaria Detected")

# Breast Cancer
elif st.session_state.disease == "Breast Cancer":
    with st.container():
        st.markdown("### Enter tumor characteristics (mean values):")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            radius_mean = st.number_input("Radius Mean", min_value=0.0, format="%.2f", key='bc_radius')
        with col2:
            texture_mean = st.number_input("Texture Mean", min_value=0.0, format="%.2f", key='bc_texture')
        with col3:
            perimeter_mean = st.number_input("Perimeter Mean", min_value=0.0, format="%.2f", key='bc_perimeter')
        
        col1, col2 = st.columns(2)
        with col1:
            area_mean = st.number_input("Area Mean", min_value=0.0, format="%.2f", key='bc_area')
        with col2:
            smoothness_mean = st.number_input("Smoothness Mean", min_value=0.0, format="%.4f", key='bc_smoothness')

        if st.button("Predict Breast Cancer", key='bc_button'):
            inputs = [
                radius_mean, texture_mean, perimeter_mean,
                area_mean, smoothness_mean
            ]
            if check_inputs(inputs):
                show_popup_error("Please enter all values before prediction.")
            else:
                result = breast_model.predict(np.array([inputs]))
                st.success("Breast Cancer Detected" if result[0] == 1 else "No Breast Cancer")


# ==========================
# Prostate Cancer
elif st.session_state.disease == "Prostate Cancer":
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            radius = st.number_input("Radius", min_value=0.0, step=0.1, key='radius')
        with col2:
            texture = st.number_input("Texture", min_value=0.0, step=0.1, key='texture')
        with col3:
            perimeter = st.number_input("Perimeter", min_value=0.0, step=0.1, key='perimeter')

        col1, col2, col3 = st.columns(3)
        with col1:
            area = st.number_input("Area", min_value=0.0, step=0.1, key='area')
        with col2:
            smoothness = st.number_input("Smoothness", min_value=0.0, step=0.01, key='smoothness')
        with col3:
            compactness = st.number_input("Compactness", min_value=0.0, step=0.01, key='compactness')

        col1, col2, col3 = st.columns(3)
        with col1:
            symmetry = st.number_input("Symmetry", min_value=0.0, step=0.01, key='symmetry')
        with col2:
            fractal = st.number_input("Fractal Dimension", min_value=0.0, step=0.01, key='fractal')

        if st.button("Predict Prostate Cancer", key='prostate_button'):
            inputs = [radius, texture, perimeter, area, smoothness, compactness, symmetry, fractal]
            result = prostate_model.predict(np.array([inputs]))
            st.success("Prostate Cancer Detected" if result[0] == 1 else "No Prostate Cancer")

# ==========================
# Skin Disease
elif st.session_state.disease == "Skin Disease":
    with st.container():
        # Apply custom CSS to add space between columns
        st.markdown("""
            <style>
                .css-1d391kg { margin-right: 20px; }
                .css-1d391kg:nth-child(4) { margin-right: 0px; }
                .css-1d391kg:nth-child(2) { margin-right: 20px; }
                .css-1d391kg:nth-child(3) { margin-right: 20px; }
            </style>
            """, unsafe_allow_html=True)

        # Create 4 columns with space between them
        col1, col2, col3, col4 = st.columns(4)
        
        # Column 1: Age, Gender, Itching, Rash, Nodules
        with col1:
            age = st.slider('Age', 1, 100, key='skin_age')
            gender = st.radio("Gender", ["Female", "Male"], key='skin_gender')
            gender = 0 if gender == "Female" else 1
            itching = st.slider("Itching", 0, 3, 0, key='skin_itching')
            rash = st.slider("Rash", 0, 3, 0, key='skin_rash')
            nodules = st.slider("Nodules", 0, 3, 0, key='skin_nodules')

        # Column 2: Patches, Scaling, Joint Pain, Mole Count, UV Exposure
        with col2:
            patches = st.slider("Patches", 0, 3, 0, key='skin_patches')
            scaling = st.slider("Scaling", 0, 3, 0, key='skin_scaling')
            uv_exposure = st.slider("UV Exposure", 0, 3, 0, key='skin_uv_exposure')

        # Column 3: Family History, Bleeding, Asymmetry, Border Irregularity
        with col3:
            family_history = st.radio("Family History of Skin Disease", ["No", "Yes"], key='skin_family_history')
            family_history = 1 if family_history == "Yes" else 0
            bleeding = st.slider("Bleeding", 0, 3, 0, key='skin_bleeding')
            asymmetry = st.slider("Asymmetry", 0, 3, 0, key='skin_asymmetry')
            border_irregularity = st.slider("Border Irregularity", 0, 3, 0, key='skin_border_irregularity')

        # Column 4: Color Variation, Evolving, Pain, Scaliness, Oozing
        with col4:
            color_variation = st.slider("Color Variation", 0, 3, 0, key='skin_color_variation')
            evolving = st.slider("Evolving", 0, 3, 0, key='skin_evolving')
            pain = st.slider("Pain", 0, 3, 0, key='skin_pain')
            scaliness = st.slider("Scaliness", 0, 3, 0, key='skin_scaliness')
            oozing = st.slider("Oozing", 0, 3, 0, key='skin_oozing')

        # Combine inputs into a list
        if age < 10:
            st.warning(" no skin disease detected.")
        elif all(v < 1 for v in [itching, rash, nodules, patches, scaling,  uv_exposure, family_history, bleeding, asymmetry, border_irregularity, color_variation, evolving, pain, scaliness, oozing]):
            st.warning("All symptoms are less than 1, no skin disease detected.")
        else:
            # Combine inputs into a list for prediction
            if st.button('Predict Skin Condition', key='skin_button'):
                input_data = np.array([[age, gender, itching, rash, nodules, patches, scaling,  uv_exposure, 
                                        family_history, bleeding, asymmetry, border_irregularity, color_variation, evolving, pain, scaliness, oozing]])
                result = skin_model.predict(input_data)
                st.success("Skin Condition Detected" if result[0] == 1 else "No Skin Condition")

