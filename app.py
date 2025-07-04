import streamlit as st
import joblib

# Load model & vectorizer
model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Emotion → song title and YouTube URL
songs = {
    "joy": [
        ("Pudhu Vellai Mazhai – Roja", "https://www.youtube.com/watch?v=HnU6a6bwKZc"),
        ("Anbil Avan – VTV", "https://www.youtube.com/watch?v=8A5oWvFYiyY")
    ],
    "sadness": [
        ("Kanave Kanave – David", "https://www.youtube.com/watch?v=MofM9B2NZp4"),
        ("Unakkenna Venum Sollu", "https://www.youtube.com/watch?v=9Lqe5U9rNZ4")
    ],
    "anger": [
        ("Kaththi Theme", "https://www.youtube.com/watch?v=bnE7TPZ0aN8"),
        ("Aaluma Doluma – Vedalam", "https://www.youtube.com/watch?v=cQwN8K1Av0U")
    ],
    "fear": [
        ("Yennai Arindhaal BGM", "https://www.youtube.com/watch?v=KNkULxImYwA"),
        ("Whistle Theme – Bigil", "https://www.youtube.com/watch?v=gKl1BEzlhFY")
    ],
    "love": [
        ("Munbe Vaa", "https://www.youtube.com/watch?v=UVXKFlV3Z8E"),
        ("Vaseegara", "https://www.youtube.com/watch?v=G-Q4uWCHG2k")
    ],
    "surprise": [
        ("Kannalanae", "https://www.youtube.com/watch?v=Ot1kPMt1RM4"),
        ("Enna Solla Pogirai", "https://www.youtube.com/watch?v=1yuc4BI5NWU")
    ]
}

st.title("🎧 MoodTune – Tamil Song Recommender")

user_input = st.text_area("How are you feeling?", "")
if st.button("Get Songs"):
    if not user_input.strip():
        st.warning("Please type your mood above.")
    else:
        emotion = model.predict(vectorizer.transform([user_input]))[0]
        st.success(f"Detected mood: **{emotion}** 🎶")

        for title, url in songs.get(emotion, []):
            st.markdown(f"### {title}")
            try:
                vid_id = url.split("v=")[-1]
                embed_url = f"https://www.youtube.com/embed/{vid_id}"
                st.video(embed_url)
            except:
                pass
            st.markdown(f"[▶️ Watch on YouTube]({url})")
