import streamlit as st

# ---- Page Config ----
st.set_page_config(
    page_title="waver",
    page_icon="🎧",
    layout="centered",
)

# ---- Custom CSS ----
st.markdown("""
<style>
body {
    background-color: #0e0e0e;
    color: #f2f2f2;
    font-family: 'Helvetica Neue', sans-serif;
}
h1 {
    font-weight: 700;
    letter-spacing: -0.02em;
}
.subtext {
    color: #a6a6a6;
    font-size: 1.1em;
    margin-bottom: 2em;
}
.button {
    background-color: #1DB954;
    color: white;
    border-radius: 2em;
    padding: 0.6em 1.4em;
    border: none;
    cursor: pointer;
    font-weight: 600;
    font-size: 1em;
}
.button:hover {
    background-color: #17a84b;
}
.footer {
    margin-top: 6em;
    font-size: 0.8em;
    color: #555;
}
</style>
""", unsafe_allow_html=True)

# ---- Main Content ----
st.markdown("<h1>waver</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>feel the resonance — music that lingers beyond sound.</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎵 Explore Music", key="explore"):
        st.success("Coming soon — personalized waves of sound 🌊")

st.markdown("<div class='footer'>© 2025 waver. all rights reserved.</div>", unsafe_allow_html=True)
