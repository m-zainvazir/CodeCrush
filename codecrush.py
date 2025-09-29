import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# ===== [BG STYLING INJECTION] =====
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnMwMmF0azF3NWZpd25wMTZlNHY3dTNlMXQ1ZjdlajV0aXJzdWxvayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xTiTnxpQ3ghPiB2Hp6/giphy.gif");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        animation: fadeOutBg 2s ease-in-out 10s forwards;
    }

    @keyframes fadeOutBg {
        to {
            background-image: none;
            background-color: #0d1117; /* fallback background after fade */
        }
    }

    .block-container {
        background-color: rgba(0, 0, 0, 0.65);  /* dark overlay for readability */
        padding: 2rem;
        border-radius: 10px;
    }

    h1, h2, h3, p {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# ===== [1] HERO SECTION – Title, Subtitle, Branding =====
st.markdown("""
    <div style="display:flex; align-items:center;">
        <h1 style="font-size:46px; margin-right:10px;">👨‍💻 CodeCrush</h1>
        <span style="color:gold; font-size:18px;">~ By Muhammad Zain Vazir</span>
    </div>
""", unsafe_allow_html=True)

st.subheader("🚀 Your AI-Powered FAANG Interview Coach")
#st.markdown("Prepare smarter for technical interviews at **FAANG, Microsoft, Uber, and more** using an AI trained on real-world coding, behavioral, and system design scenarios.")

# ===== [2] MODE SELECTOR – Lets users pick interview style =====
# Mode selection
interview_mode = st.selectbox("Choose Interview Type:", [
    "General", "Coding", "Behavioral", "System Design"
])

mode_prompt = {
    "General": "Act like a helpful FAANG interview coach.",
    "Coding": "Act like a strict technical interviewer. Ask coding questions and evaluate answers.",
    "Behavioral": "Act like a behavioral interviewer from a top tech company.",
    "System Design": "Act like a senior engineer conducting a system design interview."
}[interview_mode]

# ===== Start New Session Button =====
if st.button("Start " + interview_mode + " Interview"):
#if st.selectbox:
    st.session_state.messages = [SystemMessage(mode_prompt)]

# ===== Initialize session (fallback only) =====
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(mode_prompt)]

# ===== [3] USAGE INSTRUCTIONS – Expandable help =====
with st.expander("How to use this bot"):
    st.markdown("""
    - 👨‍💻 Type your responses or questions below.
    - 💡 You can ask *mock questions*, or respond to them as if you're in a real interview.
    - 🎯 Change the interview type using the dropdown above.
    - 🤖 The AI will adapt based on your selection.
    """)

# ===== [4] INIT CHAT HISTORY =====
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(SystemMessage(content=mode_prompt))  # changed to use mode_prompt

# ===== [5] DISPLAY CHAT HISTORY =====
for message in st.session_state.messages:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)

# ===== [6] CHAT INPUT & LLM RESPONSE HANDLING =====
prompt = st.chat_input("💬 Start your mock interview...")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append(HumanMessage(prompt))

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                llm = ChatGroq(
                    model="llama-3.1-8b-instant",  # Still free (via Groq)
                    temperature=1.5,
                    api_key=st.secrets["GROQ_API_KEY"]
                )
                result = llm.invoke(st.session_state.messages).content
                st.markdown(result)
                st.session_state.messages.append(AIMessage(result))
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
                st.info("Please try again later.")

# ===== [7] FOOTER – Subtle credits =====
st.markdown("---")
with st.sidebar:
    st.markdown("""
    <div style="display:flex; align-items:center;">
        <h1 style="font-size:46px; margin-right:10px;">👨‍💻 CodeCrush</h1>
    </div>
""", unsafe_allow_html=True)
    st.subheader("🚀 Your AI-Powered FAANG Interview Coach")
    #st.markdown("---")
    st.markdown("💬Prepare smarter for technical interviews at **FAANG, Microsoft, Uber, and more** using an AI trained on real-world coding, behavioral, and system design scenarios.")
    st.markdown("---")
    st.markdown(
    #"Credits: [Muhammad Zain Vazir](https://www.linkedin.com/in/muhammad-zain-vazir) | GitHub![GitHub](https://img.icons8.com/ios-glyphs/30/000000/github.png)[m-zainvazir](https://github.com/m-zainvazir) | LinkedIn![LinkedIn](https://img.icons8.com/ios-glyphs/30/000000/linkedin.png)[muhammad-zain-vazir](https://www.linkedin.com/in/m-zainvazir/) | Kaggle![Kaggle](https://img.icons8.com/?size=30&id=1iP83OYM1FL-&format=png&color=000000)[mzainvazir](https://www.kaggle.com/mzainvazir) | Email![Email](https://img.icons8.com/ios-glyphs/30/000000/email.png) | Contact![Email](https://img.icons8.com/ios-glyphs/30/000000/email.png)[Email](mailto:zainvazir1@gmail.com)",
    """
    <div style="text-align:center;">
        <span style="font-size:20px; color:white;">
            Credits: <a href="https://www.linkedin.com/in/m-zainvazir" target="_blank" style="color:#66ccff; text-decoration:underline; font-weight:bold;">Muhammad Zain Vazir</a>
        </span>
        <br>
        <a href="https://www.linkedin.com/in/m-zainvazir" target="_blank" title="LinkedIn">
            <img src="https://img.icons8.com/ios-glyphs/30/0A66C2/linkedin.png" style="margin:0 5px;"/>
        </a>
        <a href="https://github.com/m-zainvazir" target="_blank" title="GitHub">
            <img src="https://img.icons8.com/ios-glyphs/30/ffffff/github.png" style="margin:0 5px; background:#000; border-radius:50%;"/>
        </a>
        <a href="https://www.kaggle.com/mzainvazir" target="_blank" title="Kaggle">
            <img src="https://img.icons8.com/?size=30&id=1iP83OYM1FL-&format=png&color=20BEFF" style="margin:0 5px;"/>
        </a>
        <a href="mailto:zainvazir1@gmail.com" target="_blank" title="Email">
            <img src="https://img.icons8.com/ios-glyphs/30/ffffff/email.png" style="margin:0 5px; background:#0d1117; border-radius:50%;"/>
        </a>
        <div style="margin-top:10px; color:lightgray; font-size:16px;">
        Please share and show support ❤️
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
