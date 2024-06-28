import os
from langchain_openai import OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore


def connect_to_astra_db(collection_name:str):
    astra_endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
    astra_token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
    vstore = AstraDBVectorStore(
        embedding=OpenAIEmbeddings(),
        api_endpoint= astra_endpoint,
        token=astra_token,
        collection_name=collection_name
    )
    return vstore
