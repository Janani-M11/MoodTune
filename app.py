import streamlit as st
import joblib

# Load model & vectorizer
model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Song title and YouTube ID pairs
songs = {
    "joy": [("Pudhu Vellai Mazhai – Roja", "HnU6a6bwKZc"), ("Anbil Avan – VTV", "8A5oWvFYiyY")],
    "sadness": [("Kanave Kanave – David", "MofM9B2NZp4"), ("Unakkenna Venum Sollu", "9Lqe5U9rNZ4")],
    "anger": [("Kaththi Theme", "bnE7TPZ0aN8"), ("Aaluma Doluma – Vedalam", "cQwN8K1Av0U")],
    "fear": [("Yennai Arindhaal BGM", "KNkULxImYwA"), ("Whistle Theme – Bigil", "gKl1BEzlhFY")],
    "love": [("Munbe Vaa", "UVXKFlV3Z8E"), ("Vaseegara", "G-Q4uWCHG2k")],
    "surprise": [("Kannalanae", "Ot1kPMt1RM4"), ("Enna Solla Pogirai", "1yuc4BI5NWU")]
}

st.title("🎧 MoodTune – Tamil Song Recommender")
user_input = st.text_area("How are you feeling?")

if st.button("Get Songs"):
    if not user_input.strip():
        st.warning("Please enter some text ↑")
    else:
        emotion = model.predict(vectorizer.transform([user_input]))[0]
        st.success(f"Detected mood: **{emotion}**")
        for title, vid in songs.get(emotion, []):
            embed_url = f"https://www.youtube.com/embed/{vid}"
            st.video(embed_url)
            # Provide fallback click link
            search_link = f"https://www.youtube.com/results?search_query={title.replace(' ', '+')}"
            st.markdown(f"[🎧 Watch “{title}” on YouTube]({search_link})")
