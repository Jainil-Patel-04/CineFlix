# 🎬CineFlix

A content-based movie recommendation system built using NLP techniques (Bag of Words, TF-IDF, and Word2Vec), trained on the TMDB 5000 Movies Dataset, and deployed using **Streamlit**.

---

### 🔍 Overview

This project recommends similar movies based on the content of a selected movie. It uses NLP techniques to process metadata such as:

* Genres
* Cast
* Crew
* Keywords
* Overview

There are three NLP models:

* **Bag of Words**
* **TF-IDF**
* **Word2Vec** (for semantic similarity)

---

### 🚀 Features

* 🧠 Recommends top 5 similar movies using content-based filtering
* 🎭 Uses metadata like cast, crew, and genre
* 🧾 Fetches movie posters via **OMDb API**
* 💡 Clean, responsive UI built with **Streamlit**
* 🔍 Movie Details on demand (cast, crew, genres, overview)

---

### 🧰 Tech Stack

| Category     | Tools/Libs Used                    |
| ------------ | ---------------------------------- |
| Language     | Python                             |
| Data         | Pandas, NumPy, Gensim              |
| NLP          | Scikit-learn, NLTK, Word2Vec       |
| UI           | Streamlit                          |
| External API | OMDb API for movie posters         |
| Data Source  | TMDB 5000 Movies & Credits Dataset |

---

### ⚙️ How It Works

#### 🔹 Data Preprocessing

* Merged `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`
* Extracted relevant fields: `genres`, `keywords`, `cast`, `crew`, `overview`
* Cleaned, lemmatized, and tokenized text
* Created a combined `tags` column for each movie

#### 🔹 Vectorization Models

1. **Bag of Words** using `CountVectorizer`
2. **TF-IDF** using `TfidfVectorizer`
3. **Word2Vec** model trained using Gensim

#### 🔹 Recommendation

* Cosine similarity used to find most similar movies
* Poster fetched using OMDb API
* Top 5 recommendations displayed in a horizontal layout

## License

This project is licensed under the [MIT License](LICENSE).


---

- Kaggle Dataset Link
[Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

- Demo
[CineFlix](https://cineflix.streamlit.app/)

- <img width="1859" height="852" alt="image" src="https://github.com/user-attachments/assets/d7032e43-bce0-4772-999c-050f8845e78f" />
- <img width="1794" height="847" alt="image" src="https://github.com/user-attachments/assets/29132fce-09d2-4d91-af83-a99455f6bd18" />


