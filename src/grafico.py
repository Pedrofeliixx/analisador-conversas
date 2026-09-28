import pandas as pd
import matplotlib.pyplot as plt

# 1. Preparar os dados (igual ao exercício 1)
df = pd.read_csv("data/Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv")
df["tamanho_msg"] = df["instruction"].str.len()
media_caracteres = df.groupby("category")["tamanho_msg"].mean().sort_values()

# 2. Criar o gráfico
cores = ["#2a78d6" if categoria == "REFUND" else "#c9c8c2" for categoria in media_caracteres.index]

fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(media_caracteres.index, media_caracteres.values, color=cores)

# Valor escrito ao lado de cada barra
for posicao, valor in enumerate(media_caracteres.values):
    ax.text(valor + 0.5, posicao, f"{valor:.1f}", va="center")

# Títulos
ax.set_title("Média de caracteres por mensagem, por categoria", loc="left", fontsize=13, fontweight="bold")
ax.set_xlabel("Caracteres por mensagem")

# Visual limpo: tirar bordas de cima e da direita
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 3. Salvar a imagem em alta resolução
plt.tight_layout()
plt.savefig("imagens/media_por_categoria.png", dpi=150)
print("Gráfico salvo em imagens/media_por_categoria.png")