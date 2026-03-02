import pickle
import pandas as pd
import requests
from flask import Flask, render_template, request
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# --- LOAD DATA ---
movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
session = requests.Session()

# --- HELPER FUNCTIONS ---
def fetch_movie_info(movie_title):
    try:
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
        search_res = session.get(search_url, timeout=2).json()
        if not search_res['results']: return None

        movie_id = search_res['results'][0]['id']
        detail_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&append_to_response=videos"
        data = session.get(detail_url, timeout=2).json()

        trailer_key = ""
        for video in data.get('videos', {}).get('results', []):
            if video['type'] == 'Trailer' and video['site'] == 'YouTube':
                trailer_key = video['key']
                break

        poster_path = data.get('poster_path')
        return {
            'title': data.get('title'),
            'poster': f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else "https://images.unsplash.com/photo-1594909122845-11baa439b7bf?q=80&w=500",
            'link': f"https://www.themoviedb.org/movie/{movie_id}",
            'trailer': trailer_key,
            'genres': ", ".join([g['name'] for g in data.get('genres', [])[:2]])
        }
    except:
        return None

def get_movies_parallel(titles):
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetch_movie_info, titles))
    return [r for r in results if r is not None]

# --- ROUTES ---
@app.route('/')
def home():
    titles = movies.iloc[:8].original_title.tolist()
    movie_data = get_movies_parallel(titles)
    return render_template('index.html', movies=movie_data, active_page='discovery')

@app.route('/trending')
def trending():
    try:
        url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={API_KEY}"
        res = session.get(url).json()
        titles = [m['title'] for m in res.get('results', [])[:12]]
    except:
        titles = movies.sort_values(by='popularity', ascending=False).head(12).original_title.tolist()
    movie_list = get_movies_parallel(titles)
    return render_template('index.html', movies=movie_list, title="Trending Today", active_page='trending')

@app.route('/categories/<genre>')
def category_view(genre):
    titles = movies[movies['genres'].str.contains(genre, na=False, case=False)].head(12).original_title.tolist()
    movie_list = get_movies_parallel(titles)
    return render_template('index.html', movies=movie_list, title=f"{genre} Movies", active_page=genre.lower())

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form.get('movie_name')
    try:
        idx = movies[movies['original_title'].str.lower() == user_input.lower()].index[0]
        distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
        titles = [movies.iloc[i[0]].original_title for i in distances[1:13]]
        results = get_movies_parallel(titles)
        return render_template('index.html', movies=results, searched=user_input)
    except:
        return render_template('index.html', error="Movie not found.", movies=[])

if __name__ == '__main__':
    app.run(debug=True)