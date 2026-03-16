# 🤖 Azure-Based DevOps RAG Assistant

Bu proje, bir **AI Engineer** yolculuğunun ilk adımı olarak geliştirilmiştir. Cloud ve DevOps prensiplerini Yapay Zeka ile birleştirerek, teknik dökümanlar üzerinden akıllı ve bağlam odaklı cevaplar üreten bir **RAG (Retrieval-Augmented Generation)** asistanı sunar.

---

## 🌟 Öne Çıkan Özellikler

- **Semantic Search:** Anahtar kelime eşleşmesinin ötesinde, vektör uzayında anlamsal arama kabiliyeti.
- **Hallucination Prevention:** Modeli sadece sağlanan teknik dökümanlarla kısıtlayan sistem mesajı yapılandırması.
- **Hybrid Cloud Logic:** Azure OpenAI'ın zekasını, Azure AI Search'ün güçlü indeksleme yeteneğiyle harmanlayan mimari.
- **Developer-Centric:** DevOps iş akışlarını ve dokümantasyon süreçlerini hızlandırmak için tasarlandı.

## 🛠 Teknik Mimari ve Stack

- **LLM:** Azure OpenAI `gpt-4o-mini`
- **Embeddings:** `text-embedding-3-small` (1536 dimensions)
- **Vector Database:** Azure AI Search (Pricing Tier: Free, Algorithm: HNSW)
- **Orchestration:** Python SDK & Open AI Integration
- **Environment Management:** Python Venv & Dotenv Security

## 🚀 Hızlı Başlangıç

### 1. Gereksinimler
- Python 3.10+
- Aktif bir Azure Aboneliği
- Azure OpenAI ve Azure AI Search servislerinin kurulumu

### 2. Kurulum
Projeyi klonlayın ve sanal ortamı hazırlayın:
```bash
git clone [https://github.com/kullaniciadi/devops-ai-assistant.git](https://github.com/kullaniciadi/devops-ai-assistant.git)
cd devops-ai-assistant
python -m venv ai-env
source ai-env/bin/activate  # Windows için: ai-env\Scripts\activate
pip install -r requirements.txt
```
### 3. Yapılandırma
`.env.example` dosyasını `.env` olarak kopyalayın ve Azure portalından aldığınız anahtarları girin:
```bash
AZURE_OPENAI_KEY=your_key_here
AZURE_OPENAI_ENDPOINT=[https://your-endpoint.openai.azure.com/](https://your-endpoint.openai.azure.com/)
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-mini
AZURE_OPENAI_EMBEDDING_NAME=text-embedding-3-small

AZURE_SEARCH_ENDPOINT=[https://your-search-service.search.windows.net](https://your-search-service.search.windows.net)
AZURE_SEARCH_KEY=your_admin_key_here
AZURE_SEARCH_INDEX_NAME=devops-docs-index
```

### 4. Veri Yükleme
Teknik dökümanlarınızı vektör veritabanına basmak için:
```bash
python ingest_data.py
```

### 5. Asistanı Çalıştırma
Soru sormaya başlamak için:
```bash
python app.py
```
