import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# 🎧 Verified embeddable Tamil song links
emotion_videos = {
    "joy": [
        "https://www.youtube.com/embed/8A5oWvFYiyY",  # Anbil Avan
        "https://www.youtube.com/embed/HnU6a6bwKZc",  # Pudhu Vellai Mazhai
    ],
    "sadness": [
        "https://www.youtube.com/embed/l4ZrsBLv-Pc",  # ✅ Kanave Kanave – David
        "https://www.youtube.com/embed/9Lqe5U9rNZ4",  # Unakkenna Venum Sollu
    ],
    "anger": [
        "https://www.youtube.com/embed/bnE7TPZ0aN8",  # Kaththi Theme
        "https://www.youtube.com/embed/cQwN8K1Av0U",  # Aaluma Doluma
    ],
    "fear": [
        "https://www.youtube.com/embed/KNkULxImYwA",  # Yennai Arindhaal Suspense BGM
        "https://www.youtube.com/embed/gKl1BEzlhFY",  # Whistle Theme – Bigil
    ],
    "love": [
        "https://www.youtube.com/embed/UVXKFlV3Z8E",  # Munbe Vaa
        "https://www.youtube.com/embed/G-Q4uWCHG2k",  # Vaseegara
    ],
    "surprise": [
        "https://www.youtube.com/embed/Ot1kPMt1RM4",  # Kannalanae
        "https://www.youtube.com/embed/1yuc4BI5NWU",  # Enna Solla Pogirai
    ],
}

# Streamlit UI
st.set_page_config(page_title="MoodTune 🎧", page_icon="🎵")
st.title("🎧 MoodTune - Tamil Emotion-Based Song Recommender")
st.markdown("Tell us how you feel, and we'll play **2 matching Tamil songs** for your mood 🎶")

# User input
user_input = st.text_area("💬 How are you feeling right now?", "")

if st.button("🎵 Detect Mood & Play Songs"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence to detect your emotion.")
    else:
        # Predict emotion
        vec = vectorizer.transform([user_input])
        emotion = model.predict(vec)[0]
        st.success(f"🧠 Detected Emotion: **{emotion.upper()}**")

        # Show 2 songs side-by-side
        videos = emotion_videos.get(emotion)
        if videos:
            col1, col2 = st.columns(2)
            with col1:
                st.video(videos[0])
            with col2:
                st.video(videos[1])
        else:
            st.info("No songs found for this emotion.")
