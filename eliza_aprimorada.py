# # eliza_aprimorada.py
 
import json
import random
import difflib

class Eliza():

    def __init__(self):
        # Parse JSON content as dictionary
        with open('intents.json', 'r') as file:
            json_data = json.load(file)
        self.intents = json_data['intents']

    def respond(self, message):
        best_match = None
        highest_similarity = 0.0

        for intent in self.intents:
            for pattern in intent['patterns']:
                similarity = self.calculate_similarity(message.lower(), pattern.lower())
                if similarity > highest_similarity:
                    best_match = intent
                    highest_similarity = similarity

        if best_match is not None:
            return random.choice(best_match['responses'])
        else:
            return "I'm sorry, I don't understand."

    def calculate_similarity(self, text1, text2):
        return difflib.SequenceMatcher(None, text1, text2).ratio()