# AI-NLP-CustomerSupport-Chatbot

AI-NLP-CustomerSupport-Chatbot
📌 Project Overview
This project is a smart AI-based chatbot designed for customer support using Natural Language Processing (NLP). The chatbot understands user queries and responds with relevant information using pre-defined intents and a trained machine learning model.

It’s built using Python and libraries like NLTK, Scikit-learn, and Gradio to provide a simple and interactive interface for end users.

## ✅ Key Features

Understands customer queries using NLP

Provides relevant, automated responses

Simple and user-friendly Gradio interface

Pretrained model for fast response time

Easily extendable with new intents and responses

## 🧠 Technologies Used

Python

Natural Language Toolkit (NLTK)

Scikit-learn (Machine Learning)

JSON for intent data

Gradio (for UI)

Pickle (to save model and vectorizer)

## 📁 Project Structure

intents.json – Contains the training data (user intents and responses)

chatbot.py – NLP preprocessing and model training code

vectorizer.pkl – Saved CountVectorizer for transforming user input

chatbot_model.pkl – Trained ML model (Multinomial Naive Bayes)

app.py – Gradio web interface for the chatbot

## ⚙️ How It Works

The chatbot is trained on predefined intents using intents.json.

NLTK is used for text preprocessing like tokenization, stemming, and stopword removal.

CountVectorizer converts text into numerical form.

A Multinomial Naive Bayes classifier is trained on this vectorized data.

The trained model and vectorizer are saved using pickle.

app.py launches a Gradio interface where users can chat with the bot in real-time.

## 🚀 How to Run the Project

Install required packages:

pip install nltk scikit-learn gradio

Download NLTK data (only once):

import nltk
nltk.download('punkt')
nltk.download('stopwords')

Train the model by running:

python chatbot.py

Start the chatbot web app:

python app.py

Open the link shown in the terminal (e.g., http://127.0.0.1:7860) in your browser.


## 📸 Screenshots

screenshot1.png – Terminal Output (app.py execution showing the local Gradio server link)

screenshot2.png – Chatbot Interface opened in the browser (Gradio UI view)

screenshot3.png – Chatbot Conversation (User queries and chatbot responses)

## ✍️ Author

This project was created as part of an AI-based learning journey to explore how Natural Language Processing can be used in real-world applications like customer support chatbots.


## 👨‍💻 Author

Developed by
**Syeda Alia Samia**  
GitHub:[Syeda Alia Samia](https://github.com/your-github-username)

## 📄 License

This project is licensed for educational and demonstration purposes only.


