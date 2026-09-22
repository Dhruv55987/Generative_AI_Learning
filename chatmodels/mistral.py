from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2506")

response=model.invoke("Tell me a joke anout AI")

print(response.context)