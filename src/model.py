import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("data/flipkart_products.csv")

# Keep required columns
df = df[['product_name', 'category', 'description', 'price', 'rating']]
df = df.dropna()

# Clean price column
df['price'] = df['price'].replace('[₹,]', '', regex=True).astype(float)

# Combine text features
df['combined'] = df['category'] + " " + df['description']

# Convert text to vectors
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])

# Compute similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create index mapping
indices = pd.Series(df.index, index=df['product_name']).drop_duplicates()

# Recommendation function
def recommend(product_name, budget=None):
    if product_name not in indices:
        return [{"error": "Product not found"}]

    idx = indices[product_name]

    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:20]

    product_indices = [i[0] for i in sim_scores]
    recs = df.iloc[product_indices]

    # 🔥 Bias-aware: mix popular & less popular
    popular = recs[recs['rating'] >= 4].head(3)
    less_popular = recs[recs['rating'] < 4].head(2)
    final = pd.concat([popular, less_popular])

    results = []

    for _, row in final.iterrows():
        reason = []

        # 🔍 Explainable logic
        if row['category'] == df.iloc[idx]['category']:
            reason.append("same category")

        if budget and row['price'] <= budget:
            reason.append("within budget")

        if row['rating'] >= 4:
            reason.append("highly rated")
        else:
            reason.append("less explored")

        results.append({
            "product": row['product_name'],
            "price": row['price'],
            "rating": row['rating'],
            "reason": ", ".join(reason)
        })

    return results
