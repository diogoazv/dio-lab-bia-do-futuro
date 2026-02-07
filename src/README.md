# Passo a passo de Execucao

## Setup do Ollama

```bash
# 1. Instalar o Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull gpt-oss

# 3. Testar se funciona
ollama run gpt-oss "Ola!"
```

## Codigo Completo

Todo o codigo-fonte esta no `app.py`.

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run app.py
```
