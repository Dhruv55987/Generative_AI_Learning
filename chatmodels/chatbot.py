from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq"
)

print("Press 1 for angry mode")
print("Press 2 for sad mode")
print("Press 3 for funny mode")

choice = int(input("Tell your response"))
if choice ==1:
    mode="You are an angry ai agent and reply very aggressively"
if choice == 2:
    mode="You are a sad ai agent and reply very depressed"
if choice == 3:
    mode = "You are a very funny ai agend and respond with humor and jokes"

messages = [
    SystemMessage(content=mode)
]

print("------------ Welcome to the Chatbot ------------")
print("Type '0' to exit")

while True:

    user_input = input("You: ")

    if user_input == "0":
        print("Goodbye!")
        break

    messages.append(
        HumanMessage(content=user_input)
    )

    response = model.invoke(messages)

    print("Bot:", response.content)

    messages.append(
        AIMessage(content=response.content)
    )