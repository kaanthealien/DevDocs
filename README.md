🤖 Azure-Based DevOps RAG Assistant (PoC)
=========================================

Bu proje, bir **AI Engineer** yolculuğunun ilk adımı ve teknik bir **Proof of Concept (PoC)** çalışması olarak geliştirilmiştir. Cloud ve DevOps prensiplerini Yapay Zeka ile birleştirerek, teknik dokümanlar üzerinden akıllı ve bağlam odaklı cevaplar üreten bir **RAG (Retrieval-Augmented Generation)** asistanı sunar.

🏗 Mimari Yapı (Architecture)
-----------------------------

Proje, verinin işlenmesinden kullanıcıya sunulmasına kadar üç temel teknik katmandan oluşmaktadır:

1.  **Ingestion Layer (ingest\_data.py):** Ham metin verileri text-embedding-3-small modeli ile 1536 boyutlu vektörlere dönüştürülür ve Azure AI Search üzerindeki **HNSW** tabanlı indekslere aktarılır.
    
2.  **Retrieval Layer (app.py):** Kullanıcı sorusu anlık olarak vektörize edilir ve vektör uzayında anlamsal benzerlik metrikleri kullanılarak en yakın 3 doküman parçası (k-NN) çekilir.
    
3.  **Generation Layer:** Elde edilen bağlam (context), sistem mesajları ile "grounding" işlemine tabi tutulmuş bir **GPT-4o-mini** modeline beslenerek döküman dışı bilgi (Hallucination) üretimi engellenir.
    

🌟 Öne Çıkan Teknik Özellikler
------------------------------

*   **Semantic Search:** Anahtar kelime eşleşmesinin ötesinde, vektör uzayında anlamsal arama kabiliyeti.
    
*   **Hallucination Prevention:** Modeli sadece sağlanan teknik dokümanlarla kısıtlayan katı sistem mesajı yapılandırması.
    
*   **HNSW :** Yüksek boyutlu vektörlerde performanslı ve düşük gecikmeli arama sağlayan algoritma konfigürasyonu.
    
*   **Hybrid Cloud Logic:** Azure OpenAI'ın zekasını, Azure AI Search'ün güçlü indeksleme yeteneğiyle harmanlayan kurumsal mimari.
    
*   **Developer-Centric:** DevOps iş akışlarını ve dokümantasyon süreçlerini hızlandırmak için özel olarak optimize edilmiştir.
    

🛠 Teknoloji Yığını (Tech Stack)
--------------------------------

**LLM**: Azure OpenAI - GPT-4o-mini

**Embeddings**: Azure OpenAI - text-embedding-3-small (1536 dim)

**Vector DB**: Azure AI Search - Pricing Tier: Free / Algorithm: HNSW

**Orchestration**: Python SDK - OpenAI & Azure Integration

**Frontend**: Streamlit - Responsive Chat UI

🚀 Hızlı Başlangıç
------------------

### 1\. Gereksinimler & Kurulum

*   Python 3.10+
    
*   Aktif bir Azure Aboneliği (OpenAI & AI Search servisleri)
    


`git clone [https://github.com/kaanthealien/devops-ai-assistant.git](https://github.com/kaanthealien/devops-ai-assistant.git)`  
<br>
`cd devops-ai-assistant`
<br>
`python -m venv ai-env  # Windows için: ai-env\Scripts\activate | macOS/Linux: source ai-env/bin/activate  `  
<br>
`pip install -r requirements.txt`

### 2\. Yapılandırma

.env dosyanızı oluşturun ve Azure portalından aldığınız anahtarları tanımlayın:


`AZURE_OPENAI_KEY=your_key_here  AZURE_OPENAI_ENDPOINT=[https://your-endpoint.openai.azure.com/](https://your-endpoint.openai.azure.com/)`
<br>
`AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-mini  `
<br>
`AZURE_OPENAI_EMBEDDING_NAME=text-embedding-3-small  AZURE_SEARCH_ENDPOINT=[https://your-search-service.search.windows.net](https://your-search-service.search.windows.net)`  
<br>
`AZURE_SEARCH_KEY=your_admin_key_here`
<br>
`AZURE_SEARCH_INDEX_NAME=devops-docs-index`

### 3\. Veri Yükleme ve Çalıştırma

`# Adım 1: Teknik dokümanları vektörize edip Index'e yükleyin  python ingest_data.py  # Adım 2: Asistan arayüzünü başlatın  streamlit run ui.py `

---------

Bu çalışma bir **PoC** niteliğindedir. Geliştirme aşamasında Azure Free Tier limitleri ve gerçek dünya senaryolarına uygun veri güvenliği prensipleri göz önünde bulundurulmuştur.
