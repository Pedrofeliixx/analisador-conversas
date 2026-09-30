import pandas as pd

df = pd.read_csv("resultados/classificacao_amostra.csv")
print(df.head())

# Exercício 1: quantas mensagens de cada sentimento
print("\n--- Sentimento (quantidade) ---")
print(df["sentimento"].value_counts())

# Exercício 2: porcentagem de cada urgência
print("\n--- Urgência (%) ---")
print((df["urgencia"].value_counts(normalize=True) * 100).round(1))

# Exercício 3: categoria x urgência
print("\n--- Categoria x Urgência ---")
print(pd.crosstab(df["category"], df["urgencia"]))

# Exercício 4: categoria x sentimento
print("\n--- Categoria x Sentimento ---")
print(pd.crosstab(df["category"], df["sentimento"]))

# Exercício 5: % de cada urgência dentro de cada categoria
print("\n--- % Urgência por categoria ---")
print((pd.crosstab(df["category"], df["urgencia"], normalize="index") * 100).round(0))
