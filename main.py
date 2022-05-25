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

block = st.selectbox("انتخاب مجتمع و زیربلوک", ["-","A1-1", "A1-2","A1-3","A1-4","A1-5","A1-6","A2-1","A2-2","A2-3","A2-4","A2-5","A2-6","A3-1","A3-2"])
floor = st.selectbox("انتخاب طبقه",['-','اول','دوم','سوم','چهارم','پنجم','ششم','هفتم','هشتم'])
unit_num = st.text_input(' (در صورت اطلاع از شماره واحد خود لطفا دو گزینه بالا را وارد نکنید): شماره واحد خود را وارد کنید')
if st.button('Enter'):
    for i in datframe_list:
        # st.write(i[7])
        

        if i[8] == block and i[9] == floor:
            column = ['ردیف','شماره ملی','نام', 'نام خانوادگی','نام پدر','شماره شناسنامه','شماره پرونده','شماره واحد','بلوک','طبقه','مساحت','توضیحات',]
            dataframe_final = pd.DataFrame([i],columns=column)
            st.write(dataframe_final)
        elif i[7] == unit_num:
            column = ['ردیف','شماره ملی','نام', 'نام خانوادگی','نام پدر','شماره شناسنامه','شماره پرونده','شماره واحد','بلوک','طبقه','مساحت','توضیحات',]
            dataframe_final = pd.DataFrame([i],columns=column)
            st.write(dataframe_final)
st.sidebar.write('لینک های شورای حکیم')      
st.sidebar.write("[سایت پروژه حکیم](https://hakimproject.ir)")     
st.sidebar.write("[اینستاگرام پروژه حکیم](https://instagram.ir)")     
st.sidebar.write("[تلگرام پروژه حکیم](https://telegram.com)")     
