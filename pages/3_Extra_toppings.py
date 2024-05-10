import streamlit as st
st.header('Extra Toppings!')

st.write ('What would you like to add?')

oregano = st.checkbox('Oregano')
chilliflakes = st.checkbox('Chilliflakes')
cheese = st.checkbox('Cheese')

if oregano:
     st.write("Great! Here's some more ")

if chilliflakes: 
     st.write("Okay, There you go")

if cheese:
     st.write("Here you go ")
st.header('Snacks..! ')

