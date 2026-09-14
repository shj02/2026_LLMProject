from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
strGPT_API_Key = os.getenv('OPENAI_API_KEY') #Get API Key from .env file

#Call OpenAI() method
client = OpenAI(api_key = strGPT_API_Key)

#Create a chat completion
response = completion = client.completions.create(
    model="gpt-3.5-turbo-instruct",     #GPT model
    prompt="AI 기술의 미래에 대해 알려줘.",
    temperature=0.7,
    max_tokens=150,
)

print('===[ Response Content ]===')
print(response.choices[0].text)  #GPT 답변 출력