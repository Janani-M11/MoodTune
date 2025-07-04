import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Tamil emotion → YouTube embed URLs (2 per emotion)
emotion_videos = {
    "joy": [
        "https://www.youtube.com/embed/MjtpM8L_3qE",  # Malargaley Malargaley
        "https://www.youtube.com/embed/HnU6a6bwKZc",  # Pudhu Vellai Mazhai
    ],
    "sadness": [
        "https://www.youtube.com/embed/X31O_dkEdeE",  # Mannipaya
        "https://www.youtube.com/embed/l4ZrsBLv-Pc",  # Kannave Kannave
    ],
    "anger": [
        "https://www.youtube.com/embed/NV4rK9TjE64",  # Ding Dong
        "https://www.youtube.com/embed/kwMNRA-BpRg",  # Hey Mama
    ],
    "fear": [
        "https://www.youtube.com/embed/RQxkCI74ySA",  # Celebration of Love
        "https://www.youtube.com/embed/bnE7TPZ0aN8",  # Kaththi Theme
    ],
    "love": [
        "https://www.youtube.com/embed/UVXKFlV3Z8E",  # Munbe Vaa
        "https://www.youtube.com/embed/v5sQ0V1NN7Y",  # Vaseegara
    ],
    "surprise": [
        "https://www.youtube.com/embed/7ppEazL9FNs",  # Idhazhin Oram
        "https://www.youtube.com/embed/1yuc4BI5NWU",  # Enna Solla Pogirai
    ],
}

# UI
st.set_page_config(page_title="MoodTune 🎶", page_icon="🎧")
st.title("🎧 MoodTune - Tamil Emotion-Based Song Recommender")
st.markdown("Tell us how you feel, and we'll match your mood with two beautiful Tamil songs!")

# Input
user_input = st.text_area("💬 How are you feeling?", "")

if st.button("🎵 Detect Emotion & Show Songs"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence to detect your mood.")
    else:
        # Predict emotion
        vec = vectorizer.transform([user_input])
        emotion = model.predict(vec)[0]

        st.success(f"🧠 Detected Emotion: **{emotion.upper()}**")

        # Get songs
        video_links = emotion_videos.get(emotion)
        if video_links:
            col1, col2 = st.columns(2)
            with col1:
                st.video(video_links[0])
            with col2:
                st.video(video_links[1])
        else:
            st.info("No songs found for this mood.")
