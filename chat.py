import json
import openai
import requests

config = json.load(open("./config.json", "r"))


def generate_text(prompt):
    openai.api_key = config["ChatGPT_API_KEY"]
    response_text = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, n=3, temperature=1
    )

    commit_messages = []
    for response in response_text["choices"]:
        commit_messages.append(response["text"].strip())
    return commit_messages
