# Analisador de conversas de atendimento

> 🔨 Projeto em construção: atualizado a cada etapa.

Análise de mensagens de clientes de atendimento para entender **sobre o que os clientes falam e como escrevem**, com uso de um **LLM (Claude)** para classificar o sentimento e a urgência das mensagens.

## Dados

- **Dataset:** [Bitext Customer Support](https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset) (Hugging Face)
- **Volume:** 26.872 mensagens, 11 categorias e 27 intenções
- Dados públicos, com informações pessoais substituídas por marcadores como `{{Delivery City}}`

## Principais achados

| Pergunta | Resultado |
| --- | --- |
| Os dados têm valores faltando? | Não: nenhuma coluna tem valores nulos |
| Qual o assunto mais frequente? | **ACCOUNT** (conta, login, cadastro): 5.986 mensagens, cerca de 22% do total |
| Como os clientes escrevem? | Mensagens curtas: **46,9 caracteres** e **8,7 palavras**, em média |
| Qual a mensagem mais curta? | **1 palavra**, o caso mais difícil para um bot interpretar |
| Qual categoria tem mensagens mais longas? | **Reembolso** (50,7 caracteres em média). As mais curtas são **cancelamento** e **contato** (44,0) |
| Quais intenções pedem mais texto? | **Prazo de entrega** (11,0 palavras) e **política de reembolso** (10,5) |
| Há mensagens repetidas? | Sim: 24.635 mensagens únicas em 26.872, com frases que aparecem até 8 vezes |

![Média de caracteres por mensagem, por categoria](imagens/media_por_categoria.png)

**Leitura dos resultados:** a diferença entre categorias é pequena (cerca de 7 caracteres entre a maior e a menor média), e a maior mensagem de cada categoria fica entre 15 e 16 palavras. Em todos os assuntos o cliente escreve pouco, então um agente de atendimento precisa entender a intenção com pouquíssimo contexto.

**Observação sobre os dados:** várias categorias e intenções têm quantidades redondas (1.000 ou 2.000 mensagens), o que indica um dataset montado de forma **balanceada** para treinar modelos, diferente de dados reais de atendimento.

## Validação com SQL

Os dados foram carregados em um banco **SQLite** e as análises refeitas com **SQL**. As consultas em SQL e em Pandas chegaram aos **mesmos resultados**, uma verificação cruzada que confirma os números.

Exemplo: as 5 intenções com mensagens mais longas ([`sql/consultas.sql`](sql/consultas.sql)).

## Classificação com LLM

Uma amostra aleatória de **200 mensagens** foi classificada pelo modelo **Claude Haiku 4.5** (API da Anthropic) em duas dimensões:

- **Sentimento:** positivo, neutro ou negativo
- **Urgência:** baixa, média ou alta

**Como funciona:**

- Um *system prompt* define o papel do modelo (analista de atendimento) e as regras de classificação.
- O modelo responde em **JSON padronizado**, convertido em colunas com Pandas.
- Tratamento de erros (`try/except`) garante que uma falha isolada não interrompa o processo.
- A amostra usa `random_state=42`, então o sorteio é reproduzível.
- A chave da API fica em um arquivo `.env`, fora do repositório.
- **Custo total:** menos de US$ 0,04 para as 200 mensagens.

Resultado: [`resultados/classificacao_amostra.csv`](resultados/classificacao_amostra.csv). A análise dos resultados está em andamento.

## Etapas

- [x] Exploração inicial com Pandas (nulos, categorias, intenções, tamanho das mensagens)
- [x] Tamanho médio das mensagens por categoria e por intenção
- [x] Carga dos dados em banco SQLite e consultas SQL, validadas contra o Pandas
- [x] Visualizações
- [x] Classificação de sentimento e urgência com LLM (API do Claude) em amostra de 200 mensagens
- [ ] Análise dos resultados da classificação

## Estrutura do projeto

| Arquivo | O que faz |
| --- | --- |
| `src/carregar.py` | Exploração dos dados com Pandas |
| `src/exercicios.py` | Análises por categoria e intenção com `groupby` |
| `src/banco.py` | Cria o banco SQLite com a tabela `conversas` |
| `src/consultas.py` | Executa as consultas do arquivo `.sql` no banco |
| `sql/consultas.sql` | Consultas SQL |
| `src/grafico.py` | Gera o gráfico de média de caracteres por categoria |
| `src/teste_api.py` | Primeiro teste de chamada à API do Claude |
| `src/classificar.py` | Classifica sentimento e urgência com LLM e salva o resultado |
| `resultados/classificacao_amostra.csv` | Amostra de 200 mensagens classificadas |

## Tecnologias

Python · Pandas · SQL · SQLite · Matplotlib · API do Claude (Anthropic) · Git

## Como rodar

1. Clone o repositório e crie o ambiente virtual:

```
git clone https://github.com/Pedrofeliixx/analisador-conversas.git
cd analisador-conversas
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Baixe o CSV do dataset (link acima) e coloque na pasta `data/`.

3. Para a classificação com LLM, crie um arquivo `.env` na raiz do projeto com a sua chave da API da Anthropic (gerada em [platform.claude.com](https://platform.claude.com)):

```
ANTHROPIC_API_KEY=sua-chave
```

4. Rode as análises:

```
python src/carregar.py
python src/banco.py
python src/consultas.py
python src/grafico.py
python src/classificar.py
```