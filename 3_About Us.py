import streamlit as st
from streamlit_lottie import st_lottie
import requests
from streamlit_card import card
from PIL import Image

st.set_page_config(layout='wide')

# Custom CSS for creative styling
st.markdown("""
    <style>
    .main {
        background-color: #08090A;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #FFFFFF;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }
    .subtitle {
        color: #FFFFFF;
        font-size: 24px;
        text-align: center;
        margin-bottom: 40px;
    }
    .content-box {
        background-color: #293847;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 40px;
    }
    .content-section {
        margin-top: 30px;
    }
    .content-section h3 {
        color: #7F93A6;
        font-size: 30px;
        font-weight: bold;
    }
    .content-section p {
        font-size: 18px;
        color: #EDEDED;
    }
    .highlight {
        background-color: #EDEDED;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>About Zephyr</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='subtitle'>
    Our Story and Vision for the Future
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='content-box'>
        <h3>Who We Are</h3>
        <p>Zephyr was founded by a team of visionaries with deep expertise in synthetic aperture radar (SAR) 
        technology, data science, and software development. Our goal is to revolutionize the way industries utilize 
        SAR data by making analysis more accessible, accurate, and actionable.</p>
    </div>
""", unsafe_allow_html=True
            )

# Team section
st.markdown("""
    <div class='content-box'>
        <h3>Meet the Team</h3>
    </div>
""", unsafe_allow_html=True)


def card(title, image):
    st.image(image, caption=title, use_column_width=True)


# Create four columns for the cards
col1, col2, col3, col4 = st.columns(4)

# Card in Column 1
with col1:
    card(
        title="Vivek Manglani",
        image=r"Photos\Vivek-photoaidcom-cropped.jpg",
    )

# Card in Column 2
with col2:
    card(
        title="Gautam Prajapati",
        image=r"Photos\Gautam-photoaidcom-cropped.jpg",
    )

# Card in Column 3
with col3:
    card(
        title="Smit Prajapati",
        image=r"Photos\Smit-photoaidcom-cropped.jpg",
    )

# Card in Column 4
with col4:
    card(
        title="Het Shah",
        image=r"Photos\Het1-photoaidcom-cropped.JPG",
    )



# Vision for the Future section
st.markdown("""
    <div class='content-box'>
        <h3>Our Vision</h3>
        <p>Our vision is to become the global leader in SAR image analysis software, helping industries worldwide 
        unlock the potential of SAR data. We aim to continuously innovate and expand our offerings to meet the 
        growing demands for data-driven insights across various sectors.</p>
    </div>
""", unsafe_allow_html=True)
