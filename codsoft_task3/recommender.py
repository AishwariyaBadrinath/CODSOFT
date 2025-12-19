import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv(r"C:\Users\sakthi sony\OneDrive\movies.csv")

# Convert genres into TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(data['genre'])

# Compute cosine similarity
similarity_matrix = cosine_similarity(tfidf_matrix)

def recommend(movie_title, top_n=3):
    if movie_title not in data['title'].values:
        return "Movie not found in dataset."

    index = data[data['title'] == movie_title].index[0]
    similarity_scores = list(enumerate(similarity_matrix[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i in similarity_scores[1:top_n+1]:
        recommendations.append(data.iloc[i[0]]['title'])

    return recommendations

# User input
if __name__ == "__main__":
    movie = input("Enter a movie name: ")
    result = recommend(movie)

    print("\nRecommended Movies:")
    if isinstance(result, list):
        for r in result:
            print("-", r)
    else:
        print(result)
