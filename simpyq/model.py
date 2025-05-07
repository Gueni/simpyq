## model.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Placeholder for model - will later be trained with labeled queries

basic_ops = {
    'mean': ['average', 'mean'],
    'rms': ['rms'],
    'max': ['max', 'maximum'],
    'min': ['min', 'minimum'],
    'abs_max': ['absolute max', 'abs max'],
    'abs_min': ['absolute min', 'abs min'],
    'plot': ['plot', 'graph'],
    'sum': ['sum', 'add'],
    'product': ['multiply', '*'],
}


def interpret_query(query, available_signals):
    query = query.lower()
    for op, keywords in basic_ops.items():
        for kw in keywords:
            if kw in query:
                signals = [sig for sig in available_signals if sig.lower() in query]
                return {'operation': op, 'signals': signals}
    raise ValueError("Could not interpret query. Try rephrasing.")