import streamlit as st

st.markdown(
    """
    <style>
    .linear-title {
        white-space: nowrap; /* Prevent line wrapping */
        text-align: center;  /* Center align the text */
    }
    </style>
    """,
    unsafe_allow_html=True
)

column1, column2, column3 = st.columns([1, 2, 1])

st.markdown("""
    <hr style="border: 1px solid #ffffff;"/>
""", unsafe_allow_html=True)  

with column2:  
    st.markdown('<h1 class="linear-title">Academic Achievements</h1>', unsafe_allow_html=True)

# --- ACHIEVEMENTS ---
st.write("\n")
st.write(
    """
    - 2nd Place Soduku: School Based 2017
    - 2nd Place Scitok: School Level 2022
    - 2nd Place Collaboravideo Statistics: School Level 2022
    - 1st Place Siyensikula: School Level 2023
    - 1st Place Istoryahan Nan Statistics: School Level 2023
    - 2nd Place Istoryahan Nan Statistics: Division Level 2023
    - 2nd Place DSTF Mathematics and Computational Science Team Category 2023
    - RSTF Mathematics and Computational Science Team Category Qualifier 2023
    - 2nd Place Math Jingle in the International Pi Day School Based 2024
    - 2nd Place Scavenger's Hunt in the International Pi Day School Based 2024
    - 2nd Place Best Poster Presenter Engineering(Robotics and Intelligent Machines) in 2024 School-Based Research Congress
    - Consistent Honor student from Junior - Senior High School
    - Consistent With High Honors student in G12 (SHS)
    """
)

st.markdown("""
    <hr style="border: 10px solid #ffffff;"/>
""", unsafe_allow_html=True) 
