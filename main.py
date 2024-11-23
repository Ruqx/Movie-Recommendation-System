import pickle
import streamlit as st 
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/" + poster_path
    
    return full_path

def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key= lambda x: x[1])
    rec_mov_name = []
    rec_mov_poster = []
    for i in distances[1:6]:
        mov_id = movies.iloc[i[0]].movie_id
        rec_mov_poster.append(fetch_poster(mov_id))
        rec_mov_name.append(movies.iloc[i[0]].title)
    return rec_mov_name, rec_mov_poster

st.header("Movie Recommendation System")
movies = pickle.load(open("artifacts/movies_list.pkl", "rb"))
similarity = pickle.load(open("artifacts/similarity.pkl", "rb"))

movie_list = movies["title"].values
selected_movie = st.selectbox(
    "Type or select a movie to get recommendation",
    movie_list
)

if st.button("Show Recommendation"):
    rec_mov_name, rec_mov_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(rec_mov_name[0])
        st.image(rec_mov_poster[0])
        
    with col2:
        st.text(rec_mov_name[1])
        st.image(rec_mov_poster[1])
        
    with col3:
        st.text(rec_mov_name[2])
        st.image(rec_mov_poster[2])
        
    with col4:
        st.text(rec_mov_name[3])
        st.image(rec_mov_poster[3])
        
    with col5:
        st.text(rec_mov_name[4])
        st.image(rec_mov_poster[4])