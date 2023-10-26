import streamlit as st
import pickle
import pandas as pd
import requests as re
print(pickle.format_version)

def fetch_poster(movie_id):
   response = re.get('https://api.themoviedb.org/3/movie/{}?api_key=78b9708f460a7d941240668345f9d77b&language=en-US'.format(movie_id))
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

movies = pickle.load(open('movies.pkl','rb'))
movies_list = movies['title'].values.tolist()
# movies_list = movies_list.tolist()

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
  movie_index = movies[movies['title']==movie].index[0]
  distance=similarity[movie_index]
  movies_list = sorted(list(enumerate(distance)),reverse = True, key =lambda x: x[1])[1:6]
  recommended_movies = []
  recommended_poster = []

  for i in movies_list:
    movie_id = movies.iloc[i[0]].movie_id
    recommended_movies.append(movies.iloc[i[0]].title)
    #fetch poster from movie_id
    recommended_poster.append(fetch_poster(movie_id))

  return recommended_movies,recommended_poster

st.title('Movie Recommender System')
selected_movie_name = st.selectbox('How would you like to be contacted', movies_list)

if st.button('Recommend'):
    recommendation,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendation[0])
        st.image(posters[0])

    with col2:
        st.text(recommendation[1])
        st.image(posters[1])

    with col3:
        st.text(recommendation[2])
        st.image(posters[2])
    with col4:
        st.text(recommendation[3])
        st.image(posters[3])
    with col5:
        st.text(recommendation[4])
        st.image(posters[4])


    # poster = st.columns(5)
    # for i,r,p in poster,recommendation,posters:
    #    with i:
    #       st.text(r)
    #       st.image(p)
    # for i in recommendation:
    #     st.write(i)
  
