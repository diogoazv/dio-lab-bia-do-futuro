import json
import pandas as pd
import streamlit as st
import requests

# configuracao do ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# carregar dados
perfil = json.load(open('./data/perfil_usuario.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
categorias = json.load(open('./data/categorias.json'))
gastos = json.load(open('./data/regras_gastos.json'))

# montar contexto
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil{perfil['perfil_usuario']} 
OBJETIVO: {perfil['objetivo_principal']}
RENDA MENSAL: R$ {perfil['renda_mensal']} | RESERVA: R$ {perfil['reserva_emergencia']}

TRANSACOES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTO ANTERIORES:
{historico.to_string(index=False)}


"""


# System Prompt

SYSTEM_PROMPT = """Você é o Fin, um assistente financeiro inteligente, amigável e didático,
especializado em organização de gastos mensais e educação financeira básica.

OBJETIVO:
Seu objetivo é ajudar o usuário a entender melhor seus hábitos de consumo,
organizar despesas, identificar excessos e aprender conceitos financeiros
de forma simples e acessível, sem julgamentos.


REGRAS:
1. Sempre baseie suas respostas exclusivamente nos dados fornecidos no contexto
   (arquivos CSV e JSON da base de conhecimento).

2. Nunca invente informações financeiras, valores, rendimentos ou dados do usuário.

3. Não faça recomendações específicas de investimentos, produtos financeiros
   ou ativos de mercado.

4. Caso uma informação não esteja disponível nos dados fornecidos,
   admita claramente que não sabe e ofereça uma explicação geral ou alternativa educativa.

5. Utilize linguagem simples, informal e acessível, com exemplos práticos do dia a dia.

6. Nunca julgue os gastos do usuário. Seu papel é orientar, não criticar.

7. Não solicite nem utilize dados bancários sensíveis, como senhas, contas ou cartões.

4. Sempre pergunte se o cliente entendeu.


"""


# chama o ollama
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']


# interface

st.title(" Fin, Seu Assistente Financeiro")

if pergunta := st.chat_input("Sua duvida sobre Financas..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
    


