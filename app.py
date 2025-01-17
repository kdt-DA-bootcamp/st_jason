import streamlit as st

import solve

text = solve.my_func()

st.title('Deploy App')
st.write('My First Deploy App !')
st.write(text)