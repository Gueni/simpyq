from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import pandas as pd
import os

base_dir                         = os.path.dirname(os.path.abspath(__file__))
dataset_path                     = base_dir+ "/queries_dataset.csv"
df                               = pd.read_csv(dataset_path)
X_train, X_test, y_train, y_test = train_test_split(df['Query'], df['Intent'], test_size=0.2, random_state=42)
vectorizer                       = TfidfVectorizer(stop_words="english")
X_train_vec                      = vectorizer.fit_transform(X_train)
X_test_vec                       = vectorizer.transform(X_test)
clf                              = LogisticRegression(max_iter=100000000, solver='saga', random_state=42, n_jobs=-1) 
clf.fit(X_train_vec, y_train)
accuracy                         = clf.score(X_test_vec, y_test)
print(f"Intent classifier accuracy: {accuracy:.10f}")
joblib.dump(clf, base_dir+ "/intent_model_spacy.joblib")
joblib.dump(vectorizer, base_dir+ "/vectorizer_spacy.joblib")
print("Intent classifier saved as 'intent_model_spacy.joblib' and 'vectorizer_spacy.joblib'")