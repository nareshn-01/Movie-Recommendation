# 🎬 Movie Recommendation System

A machine learning-based Movie Recommendation Web Application that suggests similar movies based on user selection.  
The system uses **content-based filtering** and **cosine similarity** to generate accurate movie recommendations.

---

## 🚀 Features

-  Select a movie and get similar recommendations
-  Content-Based Filtering
- Cosine Similarity Model
-  Fast predictions using precomputed similarity matrix
-  Interactive Web Interface (Flask + HTML/CSS)
- Lightweight and easy to deploy

---

## How It Works

1. Movie dataset is cleaned and preprocessed.
2. Important features (genres, keywords, cast, crew) are combined.
3. Text vectorization is performed using:
   - CountVectorizer / TF-IDF
4. Cosine similarity is computed between movies.
5. When a user selects a movie:
   - The system finds the most similar movies
   - Returns Top 5 recommended movies

---

## 🛠️ Tech Stack

| Layer        | Technology Used |
|-------------|------------------|
| Backend     | Python, Flask |
| ML Library  | Scikit-learn |
| Data        | Pandas, NumPy |
| Frontend    | HTML, CSS |
| Model Save  | Pickle (.pkl) |

---

## Project Structure

```
Movie-Recommendation-System/
│
├── app.py                     # Main Flask application
├── model.py                   # Model building & recommendation logic
├── requirements.txt           # Project dependencies
├── README.md                  # Documentation
├── .gitignore
│
├── data/
│   └── movies.csv             # Raw dataset
│
├── models/
│   ├── similarity.pkl         # Precomputed similarity matrix
│   └── movies_list.pkl        # Processed movie list
│
├── templates/
│   └── index.html             # Frontend HTML file
│
├── static/
 ├── style.css              # CSS styling
  └── images/                # Optional images/posters

```

---

## ⚙️ Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3️ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️ Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📊 Example

**Input:**
```
Avatar
```

**Output:**
```
1. Guardians of the Galaxy
2. John Carter
3. Star Trek
4. The Avengers
5. Jupiter Ascending
```

---

## 📦 Example requirements.txt

```
flask
pandas
numpy
scikit-learn
pickle-mixin
```

---

##  Future Improvements

-  Integrate TMDB API for live posters
-  Add user authentication
-  Implement collaborative filtering
-  Improve UI responsiveness
-  Deploy to AWS / Render / Railway
-  Add Docker support

---

##  Contributing

Contributions are welcome!  
If you'd like to improve this project, feel free to fork the repository and submit a pull request.

---

##  License

This project is licensed under the MIT License.

---

##  Show Your Support

If you like this project, please give it a ⭐ on GitHub!
