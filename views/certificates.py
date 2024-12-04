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
    st.markdown('<h1 class="linear-title">Certificates</h1>', unsafe_allow_html=True)

# --- FIRST THREE COLUMNS 
col1, col2, col3 = st.columns(3, gap="small")

with col1:
    st.image("./pics/sys.jpg", caption="1st Place Siyensikula School Based - September 2023: Surigao Del Norte National High School, Surigao City, Surigao Del Norte", width=230)

with col2:
    st.image("./pics/slsts.jpg", caption="1st Place Istoryahan Nan Statistics School Based - October 2023: Surigao Del Norte National High School, Surigao City, Surigao Del Norte", width=230)

with col3:
    st.image("./pics/dsts.jpg", caption="2nd Place Istoryahan Nan Statistics Division Level - October 2023: Taganaan Municipal Gymnasium, Taganaan, Surigao Del Norte", width=220)

# --- SECOND TWWO COLUMNS
col4, col5 = st.columns([1,2])
with col4:
    st.image("./pics/dstf.jpg", caption="2nd Place DSTF Mathematics and Computational Science Team Category - November 2023(Via Zoom): Surigao Del Norte National High School, Surigao City, Surigao Del Norte", width=220)

with col5:
    st.image("./pics/poster.jpg", caption="2nd Place Best Poster Presenter Engineering(Robotics and Intelligent Machines) in School-Based Research Congress - April 2024: Surigao Del Norte National High School, Surigao City, Surigao Del Norte", width=220)

st.write("These certificates are a testament to my hard work, dedication, and commitment to achieving my goals. They represent the culmination of countless hours of study, practice, and perseverance. Each certificate is a tangible reminder of the skills and knowledge I have gained, and the milestones I have reached along the way. They serve as a source of pride and motivation, inspiring me to continue learning and growing in my chosen field.")

st.markdown("""
    <hr style="border: 10px solid #ffffff;"/>
""", unsafe_allow_html=True) 