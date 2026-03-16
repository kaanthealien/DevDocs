import os
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex, SearchField, SearchFieldDataType, SimpleField, SearchableField, 
    VectorSearch, VectorSearchProfile, HnswAlgorithmConfiguration, VectorSearchAlgorithmKind
)
from dotenv import load_dotenv

load_dotenv()


endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_KEY")
search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
search_key = os.getenv("AZURE_SEARCH_KEY")
index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")

client = AzureOpenAI(api_key=api_key, api_version="2024-02-01", azure_endpoint=endpoint)
search_index_client = SearchIndexClient(search_endpoint, AzureKeyCredential(search_key))

# --- 1. INDEX OLUŞTURMA (Vektör Destekli Tablo Yapısı) ---
fields = [
    SimpleField(name="id", type=SearchFieldDataType.String, key=True),
    SearchableField(name="content", type=SearchFieldDataType.String),
    # Vektör alanı: 1536 boyutlu (text-embedding-3-small standardı)
    SearchField(name="content_vector", type=SearchFieldDataType.Collection(SearchFieldDataType.Single), 
                vector_search_dimensions=1536, vector_search_profile_name="myHnswProfile")
]

vector_search = VectorSearch(
    profiles=[VectorSearchProfile(name="myHnswProfile", algorithm_configuration_name="myHnsw")] ,
    algorithms=[HnswAlgorithmConfiguration(name="myHnsw", kind=VectorSearchAlgorithmKind.HNSW)]
)

index = SearchIndex(name=index_name, fields=fields, vector_search=vector_search)
search_index_client.create_or_update_index(index)
print(f"Index {index_name} oluşturuldu.")

# --- 2. VERİYİ VEKTÖRE ÇEVİRİP YÜKLEME ---
text_to_upload = "Azure DevOps üzerinde CI/CD pipeline'ları YAML dosyaları ile tanımlanır."

# Metni vektöre çevir
embedding_response = client.embeddings.create(
    model=os.getenv("AZURE_OPENAI_EMBEDDING_NAME"),
    input=text_to_upload
)
vector = embedding_response.data[0].embedding

# Azure AI Search'e gönder
search_client = SearchClient(search_endpoint, index_name, AzureKeyCredential(search_key))
search_client.upload_documents(documents=[{
    "id": "1",
    "content": text_to_upload,
    "content_vector": vector
}])

print("Veri başarıyla vektörize edildi ve yüklendi")