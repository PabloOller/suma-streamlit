import streamlit as st

st.title('Suma 3 números')

st.write('## Usando `number_input`')

n1 = st.number_input('Primer sumando:', step =1)
n2 = st.number_input('Segundo sumando:', step =1)
n3 = st.number_input('Tercero sumando:', step =1)

st.write("La suma de los 3 números es:", n1+n2+n3)

st.divider()

st.write('## Usando `st.slider`')

a = st.slider('Primer sumando')
b = st.slider('Segundo sumando')
c = st.slider('Tercer sumando')

st.write("La suma de los 3 números es:", a+b+c)
