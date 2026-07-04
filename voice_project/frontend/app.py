import streamlit as st
import requests
import speech_recognition as sr

st.title("Restaurant Voice Order assitant")

st.write("Type or Speak your order below")

# =========================
# SESSION STORAGE
# =========================
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# =========================
# TEXT INPUT
# =========================
text_input = st.text_input("Enter order:", st.session_state.user_input)
st.session_state.user_input = text_input

# =========================
# VOICE INPUT
# =========================
if st.button("🎤 Speak Order"):

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Listening... Speak now")
        audio = recognizer.listen(source)

        try:
            voice_text = recognizer.recognize_google(audio)
            st.session_state.user_input = voice_text
            st.success("You said: " + voice_text)

        except:
            st.error("Could not understand audio")

# =========================
# SUBMIT ORDER
# =========================
if st.button("Submit Order"):

    if st.session_state.user_input.strip():

        response = requests.post(
            "http://127.0.0.1:8000/order",
            json={"text": st.session_state.user_input}
        )

        st.success("Order Placed Successfully")
        st.json(response.json())

    else:
        st.error("Please enter or speak something")

# =========================
# HISTORY BUTTON
# =========================
if st.button("📜 Show History"):

    res = requests.get("http://127.0.0.1:8000/history")
    st.subheader("Order History")
    st.json(res.json())

# =========================
# REPORT BUTTON
# =========================
if st.button("📊 Show Report"):

    res = requests.get("http://127.0.0.1:8000/report")
    st.subheader("System Report")
    st.json(res.json())


