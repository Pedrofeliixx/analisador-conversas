import sqlite3
import pandas as pd

# 1. Ler o CSV e criar as colunas calculadas
df = pd.read_csv("data/Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv")
df["tamanho_msg"] = df["instruction"].str.len()
df["qtd_palavras"] = df["instruction"].str.split().str.len()

# 2. Conectar ao banco (o arquivo é criado se não existir)
conexao = sqlite3.connect("data/conversas.db")

# 3. Salvar a tabela no banco
df.to_sql("conversas", conexao, if_exists="replace", index=False)

conexao.close()
print(f"Banco criado com {len(df)} linhas na tabela 'conversas'.")