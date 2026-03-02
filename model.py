import tensorflow as tf
print(f"TensorFlow Version: {tf.__version__}")

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def build_model():
    # Your existing code below...
    df = pd.read_csv('movies.csv')

    # Data Cleaning: Create a 'tags' column by combining features
    # We replace '|' in genres with spaces
    df['genres'] = df['genres'].str.replace('|', ' ')

    # Combine relevant features into one string
    df['tags'] = df['genres'] + " " + df['overview'] + " " + df['keywords']
    df['tags'] = df['tags'].str.lower()

    # Vectorization
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vector = cv.fit_transform(df['tags']).toarray()

    # Similarity Calculation
    similarity = cosine_similarity(vector)

    # Exporting models
    pickle.dump(df, open('movies_list.pkl', 'wb'))
    pickle.dump(similarity, open('similarity.pkl', 'wb'))
    print("Model built and files (movies_list.pkl, similarity.pkl) created!")


if __name__ == "__main__":
    build_model()