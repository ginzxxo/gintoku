import streamlit as st
import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
about_2_page = st.Page(
    page="views/acad_a.py",
    title="Academic Achievements",
    icon=":material/wysiwyg:",
)
about_3_page = st.Page(
    page="views/certificates.py",
    title="Certificates",
    icon=":material/collections_bookmark:",
)
# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pgs = st.navigation(pages=[about_page, about_2_page, about_3_page])

# --- NAVIIGATION SETUP [WITH SECTIONS]
pgs = st.navigation(
    {
        "Info": [about_page],
        "Addtional Info": [about_2_page, about_3_page],
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("pics/weblogo.png")
st.sidebar.text("Made by Gino.")

# --- RUN NAVIGATION ---
pgs.run()