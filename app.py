import pickle
import streamlit as st
import requests
import re 
import numpy as np
def format_list_items(items):
    formatted = []
    for item in items:
        # Add space between camelCase words
        formatted_item = re.sub(r'([a-z])([A-Z])', r'\1 \2', item)
        # Join all formatted items into a single string separated by commas
        formatted.append(formatted_item)
    return ", ".join(formatted)

def format_overview(overview_list):
    return " ".join(overview_list).replace(" - ", "-")  # Fix hyphen spacing

def fetch_poster_omdb(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={st.secrets['omdb']['api_key']}"
    try:
        # Send the HTTP GET request to OMDb API
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        # Improved poster handling
        poster = data.get("Poster")
        if not poster or poster == "N/A":
            return "https://placehold.co/500x750?text=Poster+Not+Available"
        return poster
    except Exception as e:
        print("OMDb Error:", e)
        return "https://via.placeholder.com/500x750.png?text=Error+Loading+Poster"

# Find the index of the movie in the DataFrame
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    # Compute similarity scores with all other movies and sort them in descending order
    # enumerate(tfidf_similarity[index]) returns (movie_index, similarity_score) pairs

    distances = sorted(list(enumerate(tfidf_similarity[index])), reverse=True, key=lambda x: x[1])
    
    # Lists to store the names and posters of the top 5 recommended movies
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[:6]:
        movie_id = movies.iloc[i[0]].title
        recommended_movie_posters.append(fetch_poster_omdb(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    # Return both titles and posters of recommended movies
    return recommended_movie_names, recommended_movie_posters

st.header('🎬 Cine Flix')

movies = pickle.load(open('movie_list.pkl','rb'))
data = np.load('tfidf_similarity.npz')
tfidf_similarity = data['tfidf_similarity']

movie_list = movies['title'].values


selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie)
    st.session_state.recommendations = list(zip(names, posters))

# Check if recommendations are available in session state
if 'recommendations' in st.session_state:
    st.subheader("Recommended Movies")

    # Create 6 equally spaced columns for displaying 6 movie recommendations
    cols = st.columns(6)

    # Loop over the recommendations (name, poster) pairs
    for i, (name, poster) in enumerate(st.session_state.recommendations):

        # Place each recommendation in its respective column
        with cols[i]:
            st.text(name)
            st.image(poster)
            if st.button("Details", key=f"btn_{i}"):

                # Store the selected movie in session state
                # This can be used later to show detailed info
                st.session_state.selected_movie = name

if 'selected_movie' in st.session_state:
    movie = movies[movies['title'] == st.session_state.selected_movie].iloc[0]
    st.subheader("Movie Details")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(fetch_poster_omdb(movie['title']))
    
    with col2:
        st.markdown(f"**Title:** {movie['title']}")
        
        # Format Director information
        directors = format_list_items(movie['crew']) if isinstance(movie['crew'], list) else movie['crew']
        st.markdown(f"**Director:** {directors}")
        
        # Format Cast information
        cast = format_list_items(movie['cast'][:5]) if isinstance(movie['cast'], list) else movie['cast']
        st.markdown(f"**Cast:** {cast}")
        
        # Added Genres display
        genres = format_list_items(movie['genres']) if isinstance(movie['genres'], list) else movie['genres']
        st.markdown(f"**Genres:** {genres}")
        
        # Format Overview
        overview = format_overview(movie['overview']) if isinstance(movie['overview'], list) else movie['overview']
        st.markdown(f"**Overview:** {overview}")
    
    if st.button("Close Details"):
        del st.session_state.selected_movie