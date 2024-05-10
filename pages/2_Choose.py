import streamlit as st
st.header("Choose Your Food!")
option = st.selectbox(
        'Favourite Food',
        ('Indian','Mexican','Chinese','Thai','Italian','Japanese','French')
)
st.write('Your favourite food is ',option)
