import streamlit as st

from cforms.contactme import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./pics/profile.png", width=280)

with col2:
    st.title("Gino Poliquit", anchor=False)
    st.write(
        """
        Hi! I'm Gino. A 1st year Computer Engineering student in Surigao Del Norte State University. 
        I am interested in programming, particularly in its ability to create innovative solutions and solve complex problems.
        I am eager to learn and explore the vast possibilities within the field of computer programming.
        """
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()

st.markdown("""
    <hr style="border: 6px solid #ffffff;"/>
""", unsafe_allow_html=True)  

# --- EDUCATIONAL ATTAINMENT ---
st.write("\n")
st.subheader("Educational Attainment", anchor=False)
st.write(
    """
    - Graduated Elementary in Surigao West Central Elementary School
    - Graduated Junior High School in Surigao City National High School
    - Graduated Senior High School in Surigao Del Norte National High School
    """
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 2 years of leadership experience in a research group
    - Good problem-solving, understanding of statistical principles, and creativity skills
    - Strong hands-on experience in copyreading and writing
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python, HTML
    - Data Visualization: MS Excel
    - Layout Designing: Canva, Picsart, Adobe Photoshop
    """
)

st.markdown("""
    <hr style="border: 1px solid #ffffff;"/>
""", unsafe_allow_html=True) 

# --- SOCIAL MEDIA ---
st.write("\n")
st.subheader("Social Media", anchor=False)
st.markdown("""
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    </head>
""", unsafe_allow_html=True)

st.markdown("""
    <a href="https://www.instagram.com/ginzxxo/" target="_blank">
        <i class="fab fa-instagram" style="font-size:24px; color:pink;"></i> Instagram
    </a><br><br>
    <a href="https://www.tiktok.com/@_ginxz" target="_blank">
        <i class="fab fa-tiktok" style="font-size:24px; color:black;"></i> TikTok
    </a><br><br>
    <a href="https://www.facebook.com/ginzpolz71" target="_blank">
        <i class="fab fa-facebook" style="font-size:24px; color:blue;"></i> Facebook
    </a>
""", unsafe_allow_html=True)