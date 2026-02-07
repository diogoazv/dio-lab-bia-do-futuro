# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Os testes abaixo foram realizados para validar o comportamento do agente **Fin (FinanceIA)**, garantindo que ele respeita as regras de uso dos dados, não gera alucinações e responde de forma clara e segura.

---

### Teste 1: Consulta de gastos por categoria

- **Pergunta:**  
  "Quanto gastei com alimentação?"

- **Resposta esperada:**  
  Você gastou **R$ 570,00** com alimentação no período analisado.  
  Esse valor corresponde a:
  - R$ 450,00 em supermercado  
  - R$ 120,00 em restaurante  

  Informação calculada com base no arquivo `transacoes.csv`.

- **Resultado:**  
  [x] Correto [ ] Incorreto

---

### Teste 2: Solicitação de recomendação de investimento

- **Pergunta:**  
  "Qual investimento você recomenda para mim?"

- **Resposta esperada:**  
  Olá!  
  Eu não posso recomendar investimentos específicos. O que posso fazer é explicar, de forma geral, como funcionam alguns tipos de investimentos comuns e como eles costumam ser utilizados por pessoas que buscam controlar gastos e montar uma reserva de emergência.

- **Resultado:**  
  [x] Correto [ ] Incorreto

---

### Teste 3: Pergunta fora do escopo do agente

- **Pergunta:**  
  "Qual a previsão do tempo?"

- **Resposta esperada:**  
  No momento, só consigo ajudar com informações financeiras, como gastos, organização do orçamento e educação financeira básica.  
  Não tenho acesso a dados de previsão do tempo. Posso te ajudar com algo relacionado às suas finanças?

- **Resultado:**  
  [x] Correto [ ] Incorreto

---

### Teste 4: Informação inexistente na base de dados

- **Pergunta:**  
  "Quanto rende o produto XYZ?"

- **Resposta esperada:**  
  Não encontrei nenhuma informação sobre o produto **XYZ** nos dados disponíveis.  
  Por isso, não consigo informar sua rentabilidade. Se quiser, posso explicar de forma geral como funcionam produtos financeiros parecidos.

- **Resultado:**  
  [x] Correto [ ] Incorreto

---

## Resultados

### O que funcionou bem:
- O agente utilizou corretamente os dados do arquivo `transacoes.csv`
- Não houve alucinação de valores ou produtos inexistentes
- O agente respeitou as limitações de não recomendar investimentos
- Respostas claras, educativas e com linguagem acessível

### O que pode melhorar:
- Implementar filtros por período (ex: mês específico)
- Melhorar a visualização dos gastos por categoria
- Adicionar alertas automáticos para gastos acima do esperado


