import os
from dotenv import load_dotenv
from huggingface_hub import HfApi

load_dotenv()

api = HfApi(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

models = api.list_models(
    pipeline_tag="image-text-to-text",
    inference_provider="all"
)

for model in models:
    print(model.id)