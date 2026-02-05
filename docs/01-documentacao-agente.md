# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas tem problemas com gastos exessivo e tem dificuldade para lidar com esses gastos.

### Solução
> Como o agente resolve esse problema de forma proativa?

Um agente que ajuda e explica formas de administrar o seu dinheiro, cortar gastos desnecessarios, e mostrar possiveis investimentos.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas que tem gastos a mais doque ganha, ou nao consegue administrar suas financas.

---

## Persona e Tom de Voz

### Nome do Agente
Fin (FinanceIA)

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

-Paciente e educativo
-Usa exemplos praticos
-Nunca julga os gastos do cliente


### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal, acessivel e explicativo, seu assistente pessoal


### Exemplos de Linguagem
- Saudação: "Ola! Me chamo Fin, seu assistente de gastos. Como podemos aconomizar mais?"
- Confirmação: "Deixa eu te explicar  isso de uma forma mais simples."
- Erro/Limitação: "Nao posso recomendar onde investir, mas posso explicar como cada tipo de investimento funciona!"

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuario] --> B["Streamlit (Interface Visual)"]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | Ollama (Local) |
| Base de Conhecimento | JSON/CSV mockados na pasta `data`|

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] So usa dados fornecidos no contexto
- [x] nao recomenda investimento especificos
- [x] Admite quando nao sabe algo
- [x] Foca apenas em ajudar, nao em aconcelhar

### Limitações Declaradas
> O que o agente NÃO faz?

- NAO faz recomendacoes de investimentos
- NAO acessa dados bancarios sensiveis
- NAO subistitui um profissional certificado

