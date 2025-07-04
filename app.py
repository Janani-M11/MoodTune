import streamlit as st
import joblib

model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

emotion_options = {
    "joy": [
        ("Pudhu Vellai Mazhai – Roja", "HnU6a6bwKZc"),
        ("Anbil Avan – VTV", "8A5oWvFYiyY")
    ],
    "sadness": [
        ("Kanave Kanave – David", "MofM9B2NZp4"),
        ("Unakkenna Venum Sollu – Yennai Arindhaal", "9Lqe5U9rNZ4")
    ],
    "anger": [
        ("Kaththi Theme", "bnE7TPZ0aN8"),
        ("Aaluma Doluma – Vedalam", "cQwN8K1Av0U")
    ],
    "fear": [
        ("Yennai Arindhaal BGM", "KNkULxImYwA"),
        ("Whistle Theme – Bigil", "gKl1BEzlhFY")
    ],
    "love": [
        ("Munbe Vaa", "UVXKFlV3Z8E"),
        ("Vaseegara", "G-Q4uWCHG2k")
    ],
    "surprise": [
        ("Kannalanae", "Ot1kPMt1RM4"),
        ("Enna Solla Pogirai", "1yuc4BI5NWU")
    ]
}

st.title("🎧 MoodTune – Tamil Song Recommender")

user_input = st.text_area("How are you feeling?")

if st.button("Get Songs"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        emotion = model.predict(vectorizer.transform([user_input]))[0]
        st.success(f"Detected emotion: **{emotion}**")
        songs = emotion_options[emotion]

        for title, vid in songs:
            embed = f"https://www.youtube.com/embed/{vid}"
            st.video(embed, format="auto", start_time=0)
            st.markdown(f"🤷‍♀️ If video doesn’t play, watch it manually: [{title}](https://www.youtube.com/watch?v={vid})")
