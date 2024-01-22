from app_utils import switch_page
import streamlit as st
from PIL import Image

# im = Image.open("icon.png")
im = Image.open("icon.png")
st.set_page_config(page_title="AI Interviewer", layout="centered", page_icon=im)


# lan = st.selectbox("#### Language", ["English"])
lan = "English"

if lan == "English":
    home_title = "AI Interviewer"
    home_introduction = "Welcome to AI Interviewer, empowering your interview preparation with generative AI."

    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )

    st.image(im, width=650)
    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Poc</font></span>""", unsafe_allow_html=True)
    st.markdown("""\n""")

    st.markdown("Welcome to AI Interviewer! 👏 AI Interviewer is your personal interviewer powered by generative AI "
                "that conducts mock interviews. You can upload your resume and AI"
                " Interviewer will give you customized questions.!")
    st.markdown("#### Get started!")
    st.markdown("Select one of the following screens to start your screening!")
    # selected = option_menu(
    #         menu_title= None,
    #         #options=["Professional", "Resume", "Behavioral","Customize!"],
    #         options=["Resume"],
    #         icons = ["cast", "cloud-upload", "cast"],
    #         default_index=0,
    #         orientation="horizontal",
    #     )
    # if selected == 'Professional':
    #     st.info("""
    #         📚In this session, the AI Interviewer will assess your technical skills relate to the job description.
    #         Note: The maximum length of your answer is 4097 tokens!
    #         - Each Interview will take 10 to 15 minutes.
    #         - To start a new session, just refresh the page.
    #         - Choose your favorite interaction style (chat/voice)
    #         - Start introduce yourself and enjoy！ """)
    #     if st.button("Start Interview!"):
    #         switch_page("Professional Screen")
    # if selected == 'Resume':
    st.info("""
        📚In this session, the AI Interviewer will review your resume and discuss your past experiences.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 minutes.
        - To start a new session, just refresh the page.
        - Start introduce yourself and enjoy！ """
            )
    if st.button("Upload Resume"):
        switch_page("Resume Screen")
    # if selected == 'Behavioral':
    #     st.info("""
    #     📚In this session, the AI Interviewer will assess your soft skills as they relate to the job description.
    #     Note: The maximum length of your answer is 4097 tokens!
    #     - Each Interview will take 10 to 15 mins.
    #     - To start a new session, just refresh the page.
    #     - Choose your favorite interaction style (chat/voice)
    #     - Start introduce yourself and enjoy！
    #     """)
    #     if st.button("Start Interview!"):
    #         switch_page("Behavioral Screen")
    # if selected == 'Customize!':
    #     st.info("""
    #         📚In this session, you can customize your own AI Interviewer and practice with it!
    #          - Configure AI Interviewer in different specialties.
    #          - Configure AI Interviewer in different personalities.
    #          - Different tones of voice.
    #
    #          Coming at the end of July""")
    st.markdown("""\n""")
