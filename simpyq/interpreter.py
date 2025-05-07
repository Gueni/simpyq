import torch
import difflib
import os
from transformers import BertTokenizer, BertForSequenceClassification
import json

# Correct paths
TOKENIZER_PATH = r"D:\WORKSPACE\simpyq\simpyq\models\tokenizer"
INTENT_MODEL_PATH = r'D:\WORKSPACE\simpyq\simpyq\models\intent_model'
LABELS_PATH = r'D:\WORKSPACE\simpyq\simpyq\models\intent_labels.json'

# Load model, tokenizer, and labels
# tokenizer = BertTokenizer.from_pretrained(TOKENIZER_PATH)
tokenizer = BertTokenizer.from_pretrained(TOKENIZER_PATH, local_files_only=True)

model = BertForSequenceClassification.from_pretrained(INTENT_MODEL_PATH)
with open(LABELS_PATH, 'r') as f:
    label_map = json.load(f)


def predict_intent(query: str):
    if not isinstance(query, str):
        raise TypeError("query must be a string")
    inputs = tokenizer([query], return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    pred = torch.argmax(outputs.logits, dim=1)
    return label_map[pred.item()]


def interpret_query(query, available_signals):
    intent = predict_intent(query)

    print(f"→ Intent: {intent}")


    matched_signals = []
    for word in query.split():
        matches = difflib.get_close_matches(word, available_signals, n=1, cutoff=0.7)
        if matches:
            matched_signals.append(matches[0])

    if not matched_signals:
        print("Error: Could not match any signals to CSV columns")
        return {"operation": None, "signals": []}
    print(f"→ Intent: {intent}")
    print(f"→ Matched signals: {matched_signals}")

    return {"operation": intent, "signals": matched_signals}
