import streamlit as st
st.title("Welcome In Python Web World")
age=st.slider("Age",18,80)
diet=st.selectbox("Diet Quality",['Poor','Avg','Good','Excelent'])
exercise=st.slider("Exersice Day Per Week",0,7,3)
stress=st.selectbox("Stress Lavel",["Low","Medium","High"])
bmi=st.number_input("BMI",10.0,40.0,22.0)
alcohol=st.selectbox("Alcohol Consumption",['Low','Medium','High'])
smoking=st.selectbox("Smoking",['Low','Medium','High'])
family_history=st.selectbox("Family History",["Yes","No"])
if st.button("Predict Risk"):
       input_data=[age,diet,exercise,stress,bmi,alcohol,smoking,family_history]
       st.success(input_data)
