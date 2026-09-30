from langchain_community.document_loaders import PyPDFLoader

data=PyPDFLoader("//pdfhere")

docs=data.load()

print(docs[4])