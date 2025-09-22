import google.generativeai as genai

response = genai.chat(
  model="gemini-2.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(response.candidates[0]['content'])
# Removed undefined 'client' usage. If you want to use another API, initialize 'client' properly.