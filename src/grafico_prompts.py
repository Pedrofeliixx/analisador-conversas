import pandas as pd
import matplotlib.pyplot as plt

v1 = pd.read_csv("resultados/classificacao_amostra.csv")
v2 = pd.read_csv("resultados/classificacao_amostra_v2.csv")

ordem = ["baixa", "media", "alta"]
p1 = (v1["urgencia"].value_counts(normalize=True) * 100).reindex(ordem)
p2 = (v2["urgencia"].value_counts(normalize=True) * 100).reindex(ordem)

posicoes = range(len(ordem))
largura = 0.38

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar([p - largura / 2 for p in posicoes], p1, largura, label="Prompt v1", color="#c9c8c2")
ax.bar([p + largura / 2 for p in posicoes], p2, largura, label="Prompt v2", color="#2a78d6")

ax.set_xticks(list(posicoes))
ax.set_xticklabels(["Baixa", "Média", "Alta"])
ax.set_ylabel("% das mensagens")
ax.set_title("Urgência classificada pelo LLM: prompt v1 x v2")
ax.legend()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

for i, valor in enumerate(p1):
    ax.text(i - largura / 2, valor + 1, f"{valor:.1f}%", ha="center")

for i, valor in enumerate(p2):
    ax.text(i + largura / 2, valor + 1, f"{valor:.1f}%", ha="center")

plt.tight_layout()
plt.savefig("imagens/comparacao_prompts.png", dpi=150)
print("Gráfico salvo")