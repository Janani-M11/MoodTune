import streamlit as st
import joblib

# Load trained model and vectorizer
model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ✅ Final Song Mapping with Search-Only Strategy
songs = {
    "joy": [
        ("Pudhu Vellai Mazhai – Roja", "Pudhu Vellai Mazhai Roja Tamil song"),
        ("Anbil Avan – Vinnaithaandi Varuvaayaa", "Anbil Avan VTV Tamil song")
    ],
    "sadness": [
        ("Kanave Kanave – David", "Kanave Kanave David Tamil song"),
        ("Kadhal Oru Aagayam – Imaikkaa Nodigal", "Kadhal Oru Aagayam Imaikkaa Nodigal Tamil song")
    ],
    "anger": [
        ("Kaththi Theme – Kaththi", "Kaththi theme Tamil song"),
        ("Hey Mama – Sethupathi", "Hey Mama Sethupathi Tamil song")
    ],
    "fear": [
        ("Celebration of Life – Aayirathil Oruvan", "Celebration of Life Aayirathil Oruvan Tamil song"),
        ("Whistle Theme – Bigil", "Whistle Theme Bigil Tamil song")
    ],
    "love": [
        ("Munbe Vaa – Sillunu Oru Kadhal", "Munbe Vaa Tamil song"),
        ("Vaseegara – Minnale", "Vaseegara Tamil song")
    ],
    "surprise": [
        ("Kannalanae – Bombay", "Kannalanae Bombay Tamil song"),
        ("Enna Solla Pogirai – Kandukondain Kandukondain", "Enna Solla Pogirai Tamil song")
    ]
}

# Streamlit UI setup
st.set_page_config(page_title="MoodTune 🎧", page_icon="🎵")
st.title("🎧 MoodTune – Tamil Song Recommender")
st.markdown("Tell me how you're feeling and get 2 Tamil songs that match your emotion 🎶")

# Text input from user
user_input = st.text_area("💬 Describe your mood in one sentence:", "")

if st.button("🎵 Detect Emotion & Recommend Songs"):
    if not user_input.strip():
        st.warning("Please type how you're feeling.")
    else:
        # Predict emotion
        vector = vectorizer.transform([user_input])
        emotion = model.predict(vector)[0]
        st.success(f"🧠 Detected Emotion: **{emotion.upper()}**")

        # Display recommended songs as clickable YouTube search links
        st.markdown("### 🎶 Recommended Tamil Songs:")
        for title, query in songs.get(emotion, []):
            search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            st.markdown(f"- 🔗 [{title}]({search_url})")
