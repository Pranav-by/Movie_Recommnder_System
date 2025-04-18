import streamlit as st
import pickle
import requests
import os

# Function to fetch poster from TMDb API
def fetch_poster(movie_id):
    TMDB_API_KEY = os.getenv("TMDB_API_KEY")
    if not TMDB_API_KEY:
        st.error("TMDB_API_KEY is not set. Please add it in Streamlit secrets or environment variables.")
        return ""

    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US'
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data.get('poster_path', '')

# Recommender function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # Ensure your DataFrame has 'movie_id'
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title('🎬 Movie Recommender System')

movies_list = movies['title'].values
selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies_list
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    # Create 5 columns for horizontal layout
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(posters[idx])
            st.caption(names[idx])
