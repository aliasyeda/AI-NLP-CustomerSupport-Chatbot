import json
import random
import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load intents.json
with open("intents.json") as file:
    data = json.load(file)

# Preprocess
X = []  # patterns (user questions)
y = []  # tags (categories)
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        X.append(pattern)
        y.append(intent["tag"])

# Convert text to numbers
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vectorized, y)

# Save model and vectorizer
pickle.dump(model, open("chatbot_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained and saved.")
