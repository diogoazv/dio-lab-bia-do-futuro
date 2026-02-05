# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `transacoes.csv` | CSV | Analisar receitas e despesas mensais, identificar padrões de gastos e calcular totais |
| `categorias.json` | JSON | Definir categorias de gastos e classificar despesas como fixas ou variáveis |
| `regras_gastos.json` | JSON | Aplicar regras simples de educação financeira (ex: limites percentuais por categoria) |
| `dicas.json` | JSON | Fornecer mensagens e orientações padronizadas para o usuário |
| `perfil_usuario.json` | JSON | Armazenar informações financeiras básicas, como renda mensal e objetivo principal |

> ℹ️ **Observação**  
> Arquivos não utilizados no MVP, como histórico de atendimento, perfil de investidor e produtos financeiros, foram mantidos em uma pasta separada (`extras/`) para possível uso futuro.

---

## Adaptações nos Dados

Os dados mockados foram **adaptados para o contexto de um consultor de gastos mensais**.  
Informações relacionadas a investimentos, produtos financeiros e perfil de risco foram removidas do fluxo principal do agente, mantendo apenas dados essenciais para organização financeira e controle de despesas.

---

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos CSV e JSON são carregados localmente no início da execução da aplicação a partir da pasta `data/`.  
Esses dados são processados antes de serem utilizados pelo agente.

### Como os dados são usados no prompt?
Os arquivos não são enviados de forma bruta ao modelo.  
A aplicação gera **resumos financeiros**, **totais por categoria** e **alertas baseados em regras**, que são inseridos dinamicamente no contexto do prompt para orientar as respostas do agente.

---

## Exemplo de Contexto Montado

```text
Resumo Financeiro do Usuário:
- Renda mensal: R$ 5.000
- Total de gastos no mês: R$ 2.488,90
- Percentual da renda comprometida: 49,7%

Gastos por categoria:
- Moradia: R$ 1.380,00
- Alimentação: R$ 570,00
- Transporte: R$ 295,00
- Lazer: R$ 55,90
- Saúde: R$ 188,00

Alertas:
- Gastos com moradia próximos do limite recomendado
- Situação financeira dentro do orçamento
