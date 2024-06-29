import streamlit as st
from streamlit_option_menu import option_menu
from data import *

st.set_page_config(
    page_title="Nur Khamidah",
    page_icon="💖",
    layout='wide',
)

with open('style.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.markdown('<h1>NUR <b>KHAMIDAH</b></h1>', unsafe_allow_html=True)

pages = option_menu("", ['About', 'Experiences', 'Skills & Portfolios', 'Certificates', 'Contact Me'], 
    icons=['file-person', 'send-arrow-up', 'bag-fill', 'file-earmark-text', 'chat-left-quote'], default_index=0, orientation="horizontal")

# --------------------------- About
if pages == 'About':
    pages

# --------------------------- Experiences
if pages == 'Experiences':
    pages
    
# --------------------------- Skills & Portfolios
if pages == 'Skills & Portfolios':
    pages
    
# --------------------------- Certificates
if pages == 'Certificates':
    pages
    
# --------------------------- Contact Me
if pages == 'Contact Me':
    pages