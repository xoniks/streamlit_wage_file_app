import streamlit as st
import pandas as pd
import sqlite3

def calculate_wage(df):
    df['wage'] = df['hours'] * df['rate']
    return df

def save_to_sql(df):
    conn = sqlite3.connect('wage_data.db')
    df.to_sql('wage_data_all',conn, if_exists='replace', index = False)
    conn.close()

st.title('Calculate wage app')
st.write('Upload a file with columns: name, hour, rate!')

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    if st.button('Show uploaded file!'):
        st.write(data)
    if st.button('Calculate the wages!'):
        out_put_wage = calculate_wage(data)
        st.write('Calculated wage file:')
        st.write(out_put_wage)
        file_to_download = out_put_wage.to_csv().encode('utf-8')
    
    try:
        st.download_button('Download the file: ',
                    data=file_to_download,
                    file_name='wages_calculated.csv')
    except:
        st.write('Calculate wage than download')
    
    if st.button('Save to database!'):
        out_put_wage = calculate_wage(data)
        save_to_sql(out_put_wage)