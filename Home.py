import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(layout='wide')


# Function to load Lottie animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Lottie animations
lottie_home = load_lottieurl("https://lottie.host/cbc9cc07-c1d9-47a3-8bba-6aef49829975/h9tseSLz9s.json")
lottie_why_us = load_lottieurl("https://lottie.host/cbc9cc07-c1d9-47a3-8bba-6aef49829975/h9tseSLz9s.json")
lottie_about_us = load_lottieurl("https://lottie.host/cbc9cc07-c1d9-47a3-8bba-6aef49829975/h9tseSLz9s.json")

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

st.markdown("<div class='title'>Welcome to Zephyr</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='subtitle'>
    Revolutionizing SAR Image Analysis through Innovative Software Solutions.
    </div>
""", unsafe_allow_html=True)

# Lottie animation
st_lottie(lottie_home, height=300, key="home")

st.markdown("<div class='title'>Our Core Mission</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='content-box'>
        <p>Zephyr is at the forefront of providing state-of-the-art software solutions for the colonization of SAR 
        (Synthetic Aperture Radar) images, helping private companies and institutions to extract valuable insights 
        from complex SAR data. Our mission is to simplify SAR image analysis and make it more actionable.</p>
    </div>
""", unsafe_allow_html=True)

# Service offerings in a collapsible section
st.markdown("<div class='title'>Our Service</div>", unsafe_allow_html=True)
st.markdown("""
<div class='content-box'>
<div class='content-section'>
    <h3>1. Advanced SAR Image Processing</h3>
    <p>Our software leverages cutting-edge technology to process SAR images quickly and accurately, enabling you to 
    analyze large datasets efficiently.</p>

<div class='content-section'>
    <h3>2. Custom Solutions for Industry Needs</h3>
    <p>We tailor our solutions to meet the needs of various industries such as defense, agriculture, and 
    environmental monitoring, ensuring accurate analysis of SAR data.</p>

""", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 2, 1, 1, 1])

with col1:
    pass

with col2:
    pass

with col3:
    pass

with col4:
    try_btn = st.button("Try Now", type="primary")
    st.markdown(f"""
        <style>
            div[data-testid="stButton"] > button {{
                display: block;
                margin: 0 auto;
            }}
        </style>
    """, unsafe_allow_html=True)

with col5:
    pass

with col6:
    pass

with col7:
    pass

if try_btn:
    st.switch_page("pages/1_Project Overview.py")
