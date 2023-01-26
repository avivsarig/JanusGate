import json
import openai
import requests

config = json.load(open("./config.json", "r"))

def generate_text(prompt):
    openai.api_key = config["ChatGPT_API_KEY"]
    response_text = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt
        )

    return response_text['choices'][0]['text'].strip()