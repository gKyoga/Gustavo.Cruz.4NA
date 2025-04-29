# 1. Instale as dependências necessárias com:
#    pip install streamlit altair==4.2.2 transformers torch
#
# 2. Execute o aplicativo com:
#    streamlit run app.py

import streamlit as st
from transformers import pipeline

# Carregar o modelo de análise de sentimento vindo do hugging face(tabularisai/multilingual-sentiment-analysis)
sentiment_analyzer = pipeline("sentiment-analysis", model="tabularisai/multilingual-sentiment-analysis")

# Função para analisar o sentimento
def analisar_sentimento(frase):
    resultado = sentiment_analyzer(frase)
    return resultado[0]['label']  



st.title("Analisador de Sentimentos Multilíngue")


frase_usuario = st.text_input("Digite uma frase para análise de sentimento:")

if frase_usuario:
    resultado = analisar_sentimento(frase_usuario)
    st.write(f"Sentimento: {resultado}")

