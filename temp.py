import ollama

response = ollama.chat(
    model='mistral:7b',
    messages=[{'role': 'user', 'content': 'Hi.'}]
)
print(response['message']['content'])