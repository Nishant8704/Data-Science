import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='StartUP Analysis')

df = pd.read_csv('startup_cleaned.csv')

def load_investor_detail(investor):
    st.title(investor)
    # Investment done by a investor
    inv = df[df['investor'].str.contains(investor)][['date','startup','vertical','City','round','amount']]
    st.subheader('Total Investments')
    st.dataframe(inv)
    
    # Biggest Investment detail
    st.subheader("Biggest Investment by Investor")
    col1 , col2, col3 = st.columns(3)
    big_ser = df[df['investor'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False)
    with col1:
        st.dataframe(big_ser)
    
    # Graph
    with col2:
        fig, ax = plt.subplots()
        ax.bar(big_ser.index,big_ser.values)
        st.pyplot(fig)

    with col3:
        vertical_series =df[df['investor'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sector Invested IN') 
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series, labels = vertical_series.index,autopct = "%0.01f",)
        st.pyplot(fig1)




# Main Website
st.sidebar.title('StartUp Funding Analysis')
option = st.sidebar.selectbox('Select any one',['Overall Analysis','StartUp','Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option =='StartUp':
    st.sidebar.selectbox('Select StartUp',sorted(df['startup'].unique().tolist()))
    st.sidebar.button('StartUp Detail')
    st.title('StartUp Analysis')
else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investor'].str.split(',').sum())))
    btn2 = st.sidebar.button('Investor Detail')
    if btn2:
        load_investor_detail(selected_investor)
