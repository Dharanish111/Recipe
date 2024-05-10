import streamlit as st
st.subheader('Milkshake')
with st.form('my_form'):
    st.subheader('**Make your Shake**')
    milk_type_val = st.selectbox('Milk Type',['Toned','Cream'])
    milk_temp_val = st.selectbox('Milk Temp',['Hot','Medium','Cold'])
    shake_type_val = st.selectbox('Shake Type',['Regular','Medium','Standard'])
    milk_val = st.select_slider('Milk Intensity',['Low','Medium','High'])
    own_cup_val = st.checkbox('Bring own cup')

    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        You have ordered:
        - Milk Type: '{milk_type_val}'
        - Milk Temp: '{milk_temp_val}'
        - Shake Type: '{shake_type_val}'
        - Milk Intesity: '{milk_val}'
        - Bring own cup: '{own_cup_val}'
        ''')
else:
    st.write('Make your Shake!')

st.subheader('Coffee')
form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ',selected_val)
