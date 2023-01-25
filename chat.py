import json
import openai
import requests

config = json.load(open("./config.json", "r"))

def generate_text(prompt, max_tokens=30):
    openai.api_key = config["ChatGPT_API_KEY"]
    response_text = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0
    )

    return response_text['choices'][0]['text'].strip()