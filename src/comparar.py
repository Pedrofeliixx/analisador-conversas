import pandas as pd

v1 = pd.read_csv("resultados/classificacao_amostra.csv")
v2 = pd.read_csv("resultados/classificacao_amostra_v2.csv")

# Conferência: as duas versões têm as mesmas mensagens, na mesma ordem?
print("Mesmas mensagens:", (v1["instruction"] == v2["instruction"]).all())

# 1. Distribuição de urgência: v1 x v2
print("\n--- Urgência (%) ---")
urgencia = pd.DataFrame({
    "v1": (v1["urgencia"].value_counts(normalize=True) * 100).round(1),
    "v2": (v2["urgencia"].value_counts(normalize=True) * 100).round(1),
})
print(urgencia)

# 2. Distribuição de sentimento: v1 x v2
print("\n--- Sentimento (%) ---")
sentimento = pd.DataFrame({
    "v1": (v1["sentimento"].value_counts(normalize=True) * 100).round(1),
    "v2": (v2["sentimento"].value_counts(normalize=True) * 100).round(1),
})
print(sentimento)

# 3. Quantas classificações mudaram
mudou_urgencia = (v1["urgencia"] != v2["urgencia"]).sum()
mudou_sentimento = (v1["sentimento"] != v2["sentimento"]).sum()
print(f"\nUrgência mudou em {mudou_urgencia} de {len(v1)} mensagens")
print(f"Sentimento mudou em {mudou_sentimento} de {len(v1)} mensagens")

# 4. Para onde as urgências migraram
print("\n--- Migração da urgência (linhas = v1, colunas = v2) ---")
print(pd.crosstab(v1["urgencia"], v2["urgencia"], rownames=["v1"], colnames=["v2"]))

# 5. Exemplos de mensagens que mudaram
exemplos = pd.DataFrame({
    "mensagem": v1["instruction"],
    "v1": v1["urgencia"],
    "v2": v2["urgencia"],
})
print("\n--- Exemplos que mudaram de urgência ---")
print(exemplos[exemplos["v1"] != exemplos["v2"]].head(10).to_string())

# 6. Mensagens que subiram para urgência alta no v2
print("\n--- Subiram para alta no v2 ---")
subiram = exemplos[(exemplos["v1"] != "alta") & (exemplos["v2"] == "alta")]
print(subiram.to_string())