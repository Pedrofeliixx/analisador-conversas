import pandas as pd

CAMINHO = "data/Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv"

df = pd.read_csv(CAMINHO)

print("=== Visão geral ===")
print(f"Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")
print(df.columns.tolist())
print()
print(df.head(3))

print()
print("=== 1. Valores nulos por coluna ===")
print(df.isnull().sum())

print()
print("=== 2. Mensagens por categoria ===")
print(f"Total de categorias: {df['category'].nunique()}")
print(df["category"].value_counts())

print()
print("=== 3. Intenções ===")
# Dataset balanceado: várias intenções têm exatamente 1000 mensagens
print(f"Total de intenções: {df['intent'].nunique()}")
print("Mais frequentes:")
print(df["intent"].value_counts().head(5))
print("Menos frequentes:")
print(df["intent"].value_counts().tail(5))

print()
print("=== 4. Tamanho das mensagens ===")
df["tamanho_msg"] = df["instruction"].str.len()
print(f"Média de caracteres: {df['tamanho_msg'].mean():.1f}")
print(f"Menor mensagem: {df['tamanho_msg'].min()} caracteres")
print(f"Maior mensagem: {df['tamanho_msg'].max()} caracteres")

print()
print("=== 5. Palavras por mensagem ===")
df["qtd_palavras"] = df["instruction"].str.split().str.len()
print(f"Média de palavras: {df['qtd_palavras'].mean():.1f}")
print(f"Menor mensagem: {df['qtd_palavras'].min()} palavras")
print(f"Maior mensagem: {df['qtd_palavras'].max()} palavras")

print()
print("=== 6. Tamanho médio por categoria ===")
media_palavras = df.groupby("category")["qtd_palavras"].mean()
print(media_palavras.sort_values(ascending=False).round(1))