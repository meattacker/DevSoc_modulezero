from google import genai
import os
import json

api_key = os.environ["GEMINI_API_KEY"]
client = genai.Client(api_key= api_key)

prompts = []

with open("prompts.txt", "r") as file:
    content = file.readlines()
    for prompt in content:
        prompts.append(prompt.strip())

with open("responses.json", "w", encoding="utf-8") as f:
    results = []
    for prompt in prompts:
        response = client.models.generate_content(
            model = "gemini-3.8-flash",
            contents = prompt
        )
        response_dict = {"prompt": prompt, "response": response.text}
        results.append(response_dict)


    json.dumps(results, f, indent = 4)
