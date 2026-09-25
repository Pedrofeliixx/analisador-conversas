# Analisador de conversas de atendimento

> 🔨 Projeto em construção: atualizado a cada etapa.

Análise de mensagens de clientes de atendimento para entender **sobre o que os clientes falam e como escrevem**, com o objetivo final de usar um LLM para classificar sentimento e urgência das mensagens.

## Dados

- **Dataset:** [Bitext Customer Support](https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset) (Hugging Face)
- **Volume:** 26.872 mensagens, 11 categorias e 27 intenções
- Dados públicos, com informações pessoais substituídas por marcadores como `{{Delivery City}}`

## Primeiros achados

| Pergunta | Resultado |
| --- | --- |
| Os dados têm valores faltando? | Não: nenhuma coluna tem valores nulos |
| Qual o assunto mais frequente? | **ACCOUNT** (conta, login, cadastro): 5.986 mensagens, cerca de 22% do total |
| Como os clientes escrevem? | Mensagens curtas: **46,9 caracteres** e **8,7 palavras**, em média |
| Qual a mensagem mais curta? | **1 palavra**, o caso mais difícil para um bot interpretar |
| Há mensagens repetidas? | Sim: 24.635 mensagens únicas em 26.872, com frases que aparecem até 8 vezes |

**Observação:** várias categorias e intenções têm quantidades redondas (1.000 ou 2.000 mensagens), o que indica um dataset montado de forma **balanceada** para treinar modelos, diferente de dados reais de atendimento.

## Etapas

- [x] Exploração inicial com Pandas (nulos, categorias, intenções, tamanho das mensagens)
- [ ] Tamanho médio das mensagens por categoria
- [ ] Carga dos dados em banco SQLite e consultas SQL
- [ ] Classificação de sentimento e urgência com LLM
- [ ] Visualizações e conclusões

## Tecnologias

Python · Pandas · SQLite · Git

## Como rodar

1. Clone o repositório e crie o ambiente virtual:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Baixe o CSV do dataset (link acima) e coloque na pasta `data/`.

3. Rode a análise:

```
python src/carregar.py
```