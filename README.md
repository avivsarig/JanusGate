# JanusGate

JanusGate sends the staged changes to ChatGPT's API and returns 3 different suggestions for a commit message.

How to setup:

1. Log into https://beta.openai.com/overview
2. Create new API key at: https://beta.openai.com/account/api-keys

3. Create a configuration file in root directory and name it "config.json"

4. Save your API key in config.json as: { "ChatGPT_API_KEY": "YOUR API KEY HERE" }

How to use:

1. Stage all your changes using 'git add' and 'git rm' commands

2. Run main.py
