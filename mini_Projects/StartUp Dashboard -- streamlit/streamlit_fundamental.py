import streamlit as st
import pandas as pd
import time

st.title('Streamlit Dashboard')
st.header('I am Learning Streamlit')
st.subheader('I am a Nishant Raj')

st.write('I want to became a best data scientist')

st.markdown("""
### List for Data Scientist
- Pandas
- numpy
- streamlit
- flask
""")

st.code("""
def foo(input):
    return foo**2
    
x = foo(5)
""")

st.write('I am using LaTex to use Equation')
st.latex('x^2  + y^2 + 4 =0')

#### Dispaly Element
st.subheader("Displaying the table")
df = pd.DataFrame({
    'Name': ['Nishant','Ravi','Ankit'],
    'Marks': [90,85,93],
    'age':[19,19,20]
})

st.dataframe(df)

st.metric('Revenue' , 'RS 3L' , '-3%')
st.metric('Stock','$ 200','5%')


st.subheader("Print dataframe as json")
st.json(
    {
    'Name': ['Nishant','Ravi','Ankit'],
    'Marks': [90,85,93],
    'age':[19,19,20]
})


st.header('Displaying Image of Parliment')
st.image('gov.jpg')

st.markdown('''
### code for display media
- st.audio('file_name')
- st.video('file_name)
''')

st.code("""
st.video('file_name')
st.audio('File_name')
""")

st.sidebar.title('title on sidebar')

# organize content side by side
col1,col2 = st.columns(2)
with col1:
    st.image('gov.jpg')

with col2:
    st.dataframe(df)


# showing status
st.header('showing status')
st.subheader('Error Message')

st.error('Login Failed')
st.success('Login Successfull')
st.info('More Information')
st.warning("Warning")



st.subheader('Progress Status')

bar = st.progress(0)
for i in range(1,101):
    # time.sleep(0.1)
    bar.progress(i)



# taking user input

st.header("Taking user input")
email = st.text_input('Enter Email')

age  = st.number_input("Enter age")

date  = st.date_input("Enter date")

# button add
