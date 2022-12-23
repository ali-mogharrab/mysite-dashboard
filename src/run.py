import streamlit as st
import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO
from PIL import Image

# Login
login_option = st.sidebar.radio('Login/Signup', ('Login', 'Signup'))

if login_option == 'Login':
    with st.sidebar.form("Login"):
        st.write("Login Here")
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')

        # Every form must have a submit button.
        submitted = st.form_submit_button("login")
        if submitted:
            pass

else:
    with st.sidebar.form("signup"):
        st.write("Signup Here")
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        email = st.text_input('Email')

        # Every form must have a submit button.
        submitted = st.form_submit_button("Signup")
        if submitted:
            pass

# Banner
banner = Image.open('./data/banner.jpg')
st.image(banner)
st.title(':zap: Mysite Dashboard')

# Metrics
col1, col2 = st.columns(2)
col1.metric("Telegram Members", "3043", "+100")
col2.metric("Website Members", "2432", "+43")

# Statistics
with st.expander('Statistics'):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        data = json.loads(string_data)
        st.json(data)

# Visualization
with st.expander('Visualization'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(100), ax=ax)
    st.pyplot(fig)

# User Info
with st.expander('User Profile'):
    col1, col2 = st.columns(2)
    col1.text_input('Name:')
    col2.text_input('Location:')
    st.camera_input('Camera Input', key='camera_input')
    
