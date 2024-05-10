import streamlit as st

st.title('Chicken Boneless')

def mg_to_kg():
  st.session_state.kg = st.session_state.mg/1000
def kg_to_mg():
  st.session_state.mg = st.session_state.kg*1000

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  Milligrams = st.number_input("Milligrams:", key = "mg", on_change = mg_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_mg)

st.header('Output')
st.write("st.session_state object:", st.session_state)
