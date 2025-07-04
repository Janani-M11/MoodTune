
import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Tamil songs with YouTube links
emotion_to_songs = {
    'joy': [
        ('Malargaley Malargaley - Love Birds', 'https://www.youtube.com/watch?v=d3fsB6CKEzo'),
        ('Pudhu Vellai Mazhai - Roja', 'https://www.youtube.com/watch?v=owI7DOeO7eY')
    ],
    'sadness': [
        ('Mannipaaya - Vinnaithaandi Varuvaaya', 'https://www.youtube.com/watch?v=93KT1FG3lNg'),
        ('Kannave Kannave - David', 'https://www.youtube.com/watch?v=Kk8fS-x9L84')
    ],
    'anger': [
        ('Ding Dong - Jigarthanda', 'https://www.youtube.com/watch?v=tJYOEPJfd9Y'),
        ('Hey Mama - Sethupathi', 'https://www.youtube.com/watch?v=2gfGgTLQWZc')
    ],
    'fear': [
        ('Celebration of Love - Aayirathil Oruvan', 'https://www.youtube.com/watch?v=ck7tLIXQ2Vw'),
        ('Kaththi Theme - Kaththi', 'https://www.youtube.com/watch?v=ClCOvT_o1nE')
    ],
    'love': [
        ('Munbe Vaa - Sillunu Oru Kadhal', 'https://www.youtube.com/watch?v=cA7FX9TtJxA'),
        ('Vaseegara - Minnale', 'https://www.youtube.com/watch?v=Z_M1uEwlsU4')
    ],
    'surprise': [
        ('Idhazhin Oram - 3', 'https://www.youtube.com/watch?v=etVdpQKQZQo'),
        ('Enna Solla Pogirai - Kandukondain Kandukondain', 'https://www.youtube.com/watch?v=t6QSk0Z5opg')
    ]
}

# Streamlit UI
st.set_page_config(page_title="Tamil Mood Music Recommender", page_icon="🎧")
st.title("🎧 Tamil Mood-Based Music Recommender")

st.write("Enter how you're feeling in English (e.g., 'I’m so happy today', 'I feel low', etc.):")
user_input = st.text_area("Describe your emotion:")

if st.button("Get Song Recommendation"):
    if user_input.strip() == "":
        st.warning("Please enter some text describing your mood.")
    else:
        vectorized_input = vectorizer.transform([user_input])
        predicted_emotion = model.predict(vectorized_input)[0]

        st.success(f"🔮 Detected Emotion: **{predicted_emotion.upper()}**")
        st.write("🎶 Recommended Tamil Songs:")

        for song_title, youtube_link in emotion_to_songs.get(predicted_emotion, []):
            st.subheader(song_title)
            st.video(youtube_link)
