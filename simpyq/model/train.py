from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import pandas as pd

# Load dataset
df = pd.read_csv("D:/WORKSPACE/simpyq/simpyq/model/data/queries_dataset.csv")

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(df['Query'], df['Intent'], test_size=0.2, random_state=42)

# Vectorize the text using TF-IDF
vectorizer = TfidfVectorizer(stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a logistic regression classifier
clf = LogisticRegression(max_iter=10000000)
clf.fit(X_train_vec, y_train)

# Evaluate the classifier
accuracy = clf.score(X_test_vec, y_test)
print(f"Intent classifier accuracy: {accuracy:.4f}")

# Save the model and vectorizer
joblib.dump(clf, 'D:/WORKSPACE/simpyq/simpyq/model/intent_model_spacy.joblib')
joblib.dump(vectorizer, 'D:/WORKSPACE/simpyq/simpyq/model/vectorizer_spacy.joblib')

print("Intent classifier saved as 'intent_model_spacy.joblib' and 'vectorizer_spacy.joblib'")
