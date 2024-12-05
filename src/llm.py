from openai import OpenAI
from src.promt import system_instruction

messages = [
    {"role":"system", "content":system_instruction}
]


client = OpenAI()


def ask_order(messages):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages 
        
    )
    return response.choices[0].message.content

