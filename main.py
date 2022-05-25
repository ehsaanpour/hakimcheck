import streamlit as st
import pandas as pd
col1, col2, col3 = st.columns(3)
hakim_excel = pd.read_excel('south.xlsx')
hakim_dataframe = pd.DataFrame(hakim_excel)
col2.image('logoHakim.jpeg')
col2.write('سامانه جستجو  واحد های پروژه حکیم')