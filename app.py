import os
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from dotenv import load_dotenv

load_dotenv()

# 1. Bağlantı Ayarları
search_client = SearchClient(
    os.getenv("AZURE_SEARCH_ENDPOINT"), 
    os.getenv("AZURE_SEARCH_INDEX_NAME"), 
    AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
)

ai_client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def asistan_cevapla(soru):
    # A - Kullanıcının sorusunu sayılara (vektöre) çevir
    print(f"Soru vektöre çevriliyor: {soru}")
    embedding = ai_client.embeddings.create(
        input=[soru],
        model=os.getenv("AZURE_OPENAI_EMBEDDING_NAME")
    ).data[0].embedding

    # B - Azure AI Search'te en yakın veriyi bul (Vektör Arama)
    vector_query = VectorizedQuery(vector=embedding, k_nearest_neighbors=3, fields="content_vector")
    
    search_results = search_client.search(
        search_text=None,
        vector_queries=[vector_query],
        select=["content"]
    )

    # C - Bulunan sonuçları birleştir (Context/Bağlam oluşturma)
    context = ""
    for result in search_results:
        context += result['content'] + "\n"
    
    print(f"Bulunan kaynak metin: {context}")

    # D - GPT-4o-mini'ye her şeyi gönder
    response = ai_client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        messages=[
            {"role": "system", "content": "Sen teknik bir dokümantasyon asistanısın. Sadece sana verilen bilgilere dayanarak cevap ver."},
            {"role": "user", "content": f"Bilgi: {context}\n\nSoru: {soru}"}
        ]
    )
    
    return response.choices[0].message.content

# --- TEST ---
user_query = "Azure DevOps pipeline'ları nasıl yönetilir?"
cevap = asistan_cevapla(user_query)
print("\n--- ASİSTANIN CEVABI ---")
print(cevap)