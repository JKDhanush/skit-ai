import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("⚙️ Settings")

        tone = st.selectbox(
            "Response Tone",
            ["Professional", "Friendly", "Apologetic"]
        )

        length = st.selectbox(
            "Response Length",
            ["Short", "Medium", "Detailed"]
        )

        st.markdown("---")

        auto_detect = st.checkbox("Auto-detect sentiment", value=True)

        st.markdown("---")

        if st.button("🧹 Clear Chat"):
            st.session_state.messages = []

        st.markdown("---")
        st.caption("RecoverAI Copilot v1.0")

    return {
        "tone": tone,
        "length": length,
        "auto_detect": auto_detect
    }