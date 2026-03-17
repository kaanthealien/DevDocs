import streamlit as st
from app import asistan_cevapla # app.py'daki fonksiyonu çağırıyoruz

st.set_page_config(page_title="DevOps AI Assistant", page_icon="🤖")

st.title("DevOps Asistan DEMOSU")
st.markdown("Azure AI & RAG mimarisi ile güçlendirilmiş teknik asistan.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat geçmişini ekranda tut
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcıdan soru al
if prompt := st.chat_input("Neyi Merak Ediyorsun ?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Dokümanlar taranıyor..."):
            # Senin yazdığın o güçlü RAG fonksiyonunu çalıştırıyoruz
            response = asistan_cevapla(prompt) 
            st.markdown(response)
            
    st.session_state.messages.append({"role": "assistant", "content": response})