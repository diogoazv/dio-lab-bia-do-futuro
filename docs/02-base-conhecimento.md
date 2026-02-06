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
> Alguns arquivos não utilizados no MVP, como histórico de atendimento, perfil de investidor e produtos financeiros, foram mantidos na mesma pasta para possível uso futuro.

---

## Adaptações nos Dados

Os dados mockados foram **adaptados para o contexto de um consultor de gastos mensais**.  
Informações relacionadas a investimentos, produtos financeiros e perfil de risco foram removidas do fluxo principal do agente, mantendo apenas dados essenciais para organização financeira e controle de despesas.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento
Os arquivos CSV e JSON são carregados localmente no início da execução da aplicação a partir da pasta `data/`.  
Esses dados são processados antes de serem utilizados pelo agente.

```python
import pandas as pd
import json

# CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = ped_read_csv('data/transacoes.csv')

# JSONs
with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
    produtos = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vao no system prompt? Sao consultadas dinamicamente?

Para simplificar, podemos simplismente "injetar" os dados em nosso prompt, garantindo que a gente tenha o melhor contexto possivel. lembrando que, em solucoes mais robustas, o ideal e que essas solucoes sejam carregadas dinamicamente para que possamos ganhar flexibilidade.

```text
DADOS DO CLIENTE (data/perfil_usuario.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "objetivo_principal": "Controlar gastos mensais"
}

CATEGORIAS (data/categorias.json):
{
  "categorias": {
    "moradia": "fixo",
    "alimentacao": "variavel",
    "transporte": "variavel",
    "lazer": "variavel",
    "saude": "variavel",
    "receita": "entrada"
  }
}

TRANSACOES DO CLIENTE (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

GASTOS DO CLIENTE (data/regras_gastos.json):
{
  "aluguel_maximo_percentual": 0.30,
  "lazer_maximo_percentual": 0.15,
  "reserva_minima_percentual": 0.10
}
```


---

## Exemplo de Contexto Montado
> Mostre um exemplo de como os dados sao formatados para o agente.

O exemplo de contexto montado abaixo, se baseia nos dados originais da base de conhecimento, mas os sintetiza deixando apenas as informacoes mais relevantes, otimizando assim o consumo de tokens. Entretanto, vale lembrar que mais importante do que economizar tokens, é ter todas as informacoes relevantes disponiveis em seu contexto.

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
