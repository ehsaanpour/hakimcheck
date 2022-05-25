# hakimcheck
import streamlit as st
import pandas as pd
# ***************************************
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
# *****************************************

original_title = '<p style="font-family:Tahoma; color:red; font-size: 40px;">سامانه جستجو  واحد های پروژه حکیم</p>'
st.markdown(original_title, unsafe_allow_html=True)

hakim_excel = pd.read_excel('south.xlsx')
hakim_dataframe = pd.DataFrame(hakim_excel)
datframe_list = hakim_dataframe.values.tolist()
col1,col2,col3 = st.columns(3)
col2.image('logohakim.jpeg')
original_title = '<p style="font-family:arial; color:red; font-size: 25px;"> : شماره واحد خود را وارد کنید</p>'
st.markdown(original_title, unsafe_allow_html=True)
unit_num = st.text_input('')

if st.button('Enter'):
    for i in datframe_list:
        # st.write(i[7])
        if i[7] == unit_num:
            column = ['ردیف','شماره ملی','نام', 'نام خانوادگی','نام پدر','شماره شناسنامه','شماره پرونده','شماره واحد','بلوک','طبقه','مساحت','توضیحات',]
            dataframe_final = pd.DataFrame([i],columns=column)
            st.write(dataframe_final)


st.sidebar.write('لینک های شورای حکیم')      
st.sidebar.write("[سایت پروژه حکیم](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")     
