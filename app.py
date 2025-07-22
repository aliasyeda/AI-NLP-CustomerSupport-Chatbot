import gradio as gr
import random
import json
import pickle

# Load saved files
model = pickle.load(open("chatbot_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Load intents
with open("intents.json") as file:
    data = json.load(file)

# Chatbot logic
def chatbot_response(user_input):
    vect_input = vectorizer.transform([user_input])
    tag = model.predict(vect_input)[0]

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "Sorry, I didn't understand that."

# Create Gradio interface
interface = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="text",
    title="AI Chatbot for Customer Support"
)

# Launch the app
interface.launch()
