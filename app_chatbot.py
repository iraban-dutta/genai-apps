from dotenv import load_dotenv
import gradio as gr
from groq import Groq

load_dotenv()
MODEL = "llama-3.3-70b-versatile"
client = Groq()
system_message = "You are a helpful assistant"

def chat(message, history):
    history = [{"role": msg["role"], "content": msg["content"]} for msg in history]
    messages = (
        [{"role": "system", "content": system_message}]
        + history
        + [{"role": "user", "content": message}]
    )
    stream = client.chat.completions.create(model=MODEL, messages=messages, stream=True)
    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response

gr.ChatInterface(fn=chat, type="messages").launch()