from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()
response = client.chat.completions.create(
    model="llama3-8b-8192",  # A basic model to test with
    messages=[
        {"role": "user", "content": "Say hello world"}
    ]
)

print(response.choices[0].message.content)