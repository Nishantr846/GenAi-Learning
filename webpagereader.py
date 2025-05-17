from llama_index.legacy.readers.web import SimpleWebPageReader
from llama_index.legacy.indices.vector_store import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv
load_dotenv()

# print("This is my OpenAi API Key:", os.environ["openai_api_key"])

def main(url:str)-> None:
    document = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    index = VectorStoreIndex.from_documents(documents=document)
    query_engine = index.as_query_engine()
    response = query_engine.query("When was the first generative AI model released?")
    print(response)

if __name__ == "__main__":
    main(url="https://en.wikipedia.org/wiki/Generative_artificial_intelligence")