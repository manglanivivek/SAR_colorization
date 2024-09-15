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

st.markdown("<div class='title'>Why Choose Zephyr?</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='subtitle'>
    Discover the Unique Advantages of Working with Us
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='content-box'>
        <h3>Our Competitive Edge</h3>
        <ul>
            <li><strong>Industry Expertise:</strong> With years of experience in SAR image analysis, Zephyr leads 
            the field in developing advanced software solutions.</li>
            <li><strong>Innovation:</strong> We constantly innovate to provide our clients with the most advanced 
            tools for SAR image colonization.</li>
            <li><strong>Client Focus:</strong> We work closely with each client to understand their specific needs, 
            delivering custom solutions that meet their exact requirements.</li>
            <li><strong>Cost-Effective:</strong> Our software is designed to offer high performance while keeping 
            costs low, ensuring great value for your investment.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)


def card(title, image):
    st.image(image, caption=title, use_column_width=True)


st.markdown("<h3>Comparison</h3>", unsafe_allow_html=True)

# Create columns
col1, col2, col3, col4 = st.columns(4)

# Card in Column 1
with col1:
    card(
        title="Original",
        image=r"Photos\ORG1.jpg"
    )

# Card in Column 2
with col2:
    card(
        title="Zephyr",
        image=r"Photos\Col1.jpg"
    )

# Card in Column 3
with col3:
    card(
        title="Other Websites",
        image=r"Photos\WhatsApp Image 2024-09-15 at 08.57.09_50347210.png"
    )

# Card in Column 4
with col4:
    card(
        title="Other Websites",
        image=r"Photos\WhatsApp Image 2024-09-15 at 08.56.25_2d6e7d56 (1).jpg.jpg"
    )

col5, col6, col7, col8 = st.columns(4)

# Card in Column 5
with col5:
    card(
        title="Original",
        image=r"Photos\ORG2.jpg"
    )

# Card in Column 5
with col6:
    card(
        title="Zephyr",
        image=r"Photos\col2.jpg"
    )

# Card in Column 7
with col7:
    card(
        title="Other Websites",
        image=r"Photos\WhatsApp Image 2024-09-15 at 08.57.10_ce4fb45e.png"
    )

# Card in Column 8
with col8:
    card(
        title="Other Websites",
        image=r"Photos\WhatsApp Image 2024-09-15 at 08.56.26_7a1fb543 (1).jpg.jpg"
    )

col9, col10, col11, col12 = st.columns(4)

# Card in Column 1
with col9:
    card(
        title="Original",
        image=r"Photos\ORG3.jpg"
    )

# Card in Column 2
with col10:
    card(
        title="Zephyr",
        image=r"Photos\col3.jpg"
    )

# Card in Column 3
with col11:
    card(
        title="Other Websites",
        image=r"Photos\WhatsApp Image 2024-09-15 at 08.57.09_e6384477.png"
    )

# Card in Column 4
with col12:
    card(
        title="Other Websites",
        image=r"Photos\WhatsApp Image 2024-09-15 at 08.56.25_4bab26ec (1).jpg.jpg"
    )

