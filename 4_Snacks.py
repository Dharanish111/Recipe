import streamlit as st 
options = st.multiselect(
     'Your most favorite snacks',
     ['Samosa', 'Bajji', 'Puff', 'Sweets'],
     ['Samosa', 'Sweets'])
st.write('You selected:', options)

if st.button('Start'):
     st.header('Gonna,have a wonderful cooking experience')
else:
     st.write('wanna cook')
