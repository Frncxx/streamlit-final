import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data from uploaded file
@st.cache_data
def load_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    else:
        return None

# Streamlit app
st.title("Heart Failure Dataset Visualization")

st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a view:", ["Overview", "Demographics", "Health Indicators", "Outcomes"])

uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    if df is not None:
        if options == "Overview":
            st.header("Data Overview")
            st.write("This app provides insights into a heart failure dataset, including demographics, health indicators, and outcomes.")
            st.write(df)
            st.write("Below are some visual insights from the data.")

            # Show dataset info
            st.subheader("Dataset Information")
            st.write(df.describe())

            # Show correlation matrix
            st.subheader("Correlation Matrix")
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

        elif options == "Demographics":
            st.header("Demographics")
            
            # Age distribution
            st.subheader("Age Distribution")
            fig, ax = plt.subplots()
            sns.histplot(df['age'], bins=20, kde=True, ax=ax)
            st.pyplot(fig)

            # Gender distribution
            st.subheader("Gender Distribution")
            gender_dist = df['sex'].value_counts()
            st.bar_chart(gender_dist)

        elif options == "Health Indicators":
            st.header("Health Indicators")
            
            # Ejection Fraction distribution
            st.subheader("Ejection Fraction Distribution")
            fig, ax = plt.subplots()
            sns.histplot(df['ejection_fraction'], bins=20, kde=True, ax=ax)
            st.pyplot(fig)

            # Serum Creatinine distribution
            st.subheader("Serum Creatinine Distribution")
            fig, ax = plt.subplots()
            sns.histplot(df['serum_creatinine'], bins=20, kde=True, ax=ax)
            st.pyplot(fig)

            # Serum Sodium distribution
            st.subheader("Serum Sodium Distribution")
            fig, ax = plt.subplots()
            sns.histplot(df['serum_sodium'], bins=20, kde=True, ax=ax)
            st.pyplot(fig)

        elif options == "Outcomes":
            st.header("Outcomes")
            
            # Death Event distribution
            st.subheader("Death Event Distribution")
            death_event_dist = df['DEATH_EVENT'].value_counts()
            st.bar_chart(death_event_dist)

            # Boxplot of ejection fraction by death event
            st.subheader("Ejection Fraction by Death Event")
            fig, ax = plt.subplots()
            sns.boxplot(data=df, x='DEATH_EVENT', y='ejection_fraction', ax=ax)
            st.pyplot(fig)

            # Boxplot of serum creatinine by death event
            st.subheader("Serum Creatinine by Death Event")
            fig, ax = plt.subplots()
            sns.boxplot(data=df, x='DEATH_EVENT', y='serum_creatinine', ax=ax)
            st.pyplot(fig)

        # Adding explanations
        st.sidebar.title("About the Data")
        st.sidebar.write("""
        This dataset includes various features related to patients' health indicators and outcomes for heart failure.
        The data is used to analyze trends and patterns to understand the factors affecting heart failure outcomes.
        """)

        st.sidebar.write("**Columns:**")
        st.sidebar.write("""
        - **age**: Age of the patient
        - **anaemia**: Decrease of red blood cells or hemoglobin (boolean)
        - **creatinine_phosphokinase**: Level of the CPK enzyme in the blood (mcg/L)
        - **diabetes**: If the patient has diabetes (boolean)
        - **ejection_fraction**: Percentage of blood leaving the heart at each contraction (percentage)
        - **high_blood_pressure**: If the patient has hypertension (boolean)
        - **platelets**: Platelets in the blood (kiloplatelets/mL)
        - **serum_creatinine**: Level of serum creatinine in the blood (mg/dL)
        - **serum_sodium**: Level of serum sodium in the blood (mEq/L)
        - **sex**: Gender of the patient (1 = male, 0 = female)
        - **smoking**: If the patient smokes (boolean)
        - **time**: Follow-up period (days)
        - **DEATH_EVENT**: If the patient deceased during the follow-up period (boolean)
        """)

    else:
        st.write("Please upload a valid CSV file.")

else:
    st.write("Please upload a CSV file to get started.")
