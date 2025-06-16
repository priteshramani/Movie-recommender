import streamlit as st
import pandas as pd
import pickle


# Streamlit UI
st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pickle', 'rb'))
similarity = pickle.load(open('cosine_similarity.pickle', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

   
def recommend(title, df=movies, cosine_sim=similarity):
    try:
        idx = df[df['title'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]  # Get top 5 recommendations
        movie_indices = [i[0] for i in sim_scores]
        movie=[df['title'][i] for i in movie_indices]
        return pd.Series(movie,name="Suggested Movies")
    except IndexError:
        return "Movie not found."

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    st.write(recommended_movie_names)