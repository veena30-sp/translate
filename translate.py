import streamlit as st
from googletrans import Translator

st.header('Machine Translation Demo')
input_text = st.text_area("Please enter the text", value='')
option = st.selectbox(
    'To which language do you wish to translate this text to?',
    ('Malayalam', 'Hindi', 'Tamil')
)

if st.button('Translate'):
    translator = Translator()
    translation = translator.translate(input_text, dest=option.lower())
    st.write(translation.text)