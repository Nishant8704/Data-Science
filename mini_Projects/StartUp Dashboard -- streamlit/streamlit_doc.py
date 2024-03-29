import streamlit as st
import pandas as pd


email = st.text_input('Enter Your Email: ')
password = st.text_input('Enter the password: ')

# Drop downs
st.selectbox('Select Gender',['Male','Female','Others'])

# file upload
# file = st.file_uploader('upload a csv file')

button = st.button('Login here')

if button:
    if email == 'thakur@gmail.com' and password =='1234':
        st.success('Login Successfull')
        st.balloons()
    else:
        st.error('login Failed')


file  = st.file_uploader('Upload a CSV file')

if file is not None:
    df= pd.read_csv(file)
    st.dataframe(df.describe())

