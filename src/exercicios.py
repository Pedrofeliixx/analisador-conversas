import pandas as pd

df = pd.read_csv("data/Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv")
df["tamanho_msg"] = df["instruction"].str.len()
df["qtd_palavras"] = df["instruction"].str.split().str.len()

print("=== Exercício 1: média de caracteres por categoria ===")
media_caracteres = df.groupby("category")["tamanho_msg"].mean()
print(media_caracteres.sort_values(ascending=False).round(1))

print()
print("=== Exercício 2: categorias com mensagens mais curtas ===")
print(media_caracteres.sort_values(ascending=True).round(1))        

print()
print("=== Exercício 3: maior mensagem por categoria ===")
maior_por_categoria = df.groupby("category")["qtd_palavras"].max()
print(maior_por_categoria.sort_values(ascending=False))