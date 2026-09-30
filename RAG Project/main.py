from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
data=TextLoader("document loaders/notes.txt")
docs=data.load()

template=ChatPromptTemplate([("system","You are an Ai that summarises the text")
                    ,("human","{data}")]
 )



model = ChatGroq(model="openai/gpt-oss-120b",
    temperature=1)

prompt = template.format_messages(data= docs[0].page_content)
result= model.invoke(prompt)

print(result.content)