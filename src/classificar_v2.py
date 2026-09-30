import os
import time
import json
import pandas as pd
from dotenv import load_dotenv
import anthropic

load_dotenv()
cliente = anthropic.Anthropic()

INSTRUCAO = """Você é um analista de atendimento ao cliente de um e-commerce.
Classifique a mensagem do cliente em sentimento e urgência, seguindo estes critérios:

SENTIMENTO
- negativo: reclamação, frustração, irritação ou relato de problema
- neutro: pedido de informação ou de ação, sem emoção aparente
- positivo: elogio, agradecimento ou satisfação

URGÊNCIA
- alta: o cliente está impedido de fazer algo importante agora (não consegue pagar, acessar a conta, receber o pedido, falar com alguém) ou relata cobrança indevida
- media: o cliente precisa de uma ação da empresa, mas não está bloqueado (alterar ou cancelar pedido, pedir reembolso, atualizar dados)
- baixa: dúvida ou consulta informativa (prazos, políticas, formas de pagamento, como fazer algo)

Não use "media" como resposta padrão: escolha o nível que melhor corresponde aos critérios.

EXEMPLOS
Mensagem: "I can't log into my account, it keeps giving an error"
{"sentimento": "negativo", "urgencia": "alta"}

Mensagem: "I want to change the address of my order"
{"sentimento": "neutro", "urgencia": "media"}

Mensagem: "what payment methods do you accept?"
{"sentimento": "neutro", "urgencia": "baixa"}

Responda APENAS com um JSON neste formato, sem nenhum texto antes ou depois e sem markdown:
{"sentimento": "...", "urgencia": "..."}"""


def classificar(mensagem):
    resposta = cliente.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=50,
        system=INSTRUCAO,
        messages=[{"role": "user", "content": mensagem}]
    )
    texto = resposta.content[0].text.strip()
    texto = texto.removeprefix("```json").removesuffix("```").strip()
    return json.loads(texto)


df = pd.read_csv("data/Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv")
amostra = df.sample(200, random_state=42).copy()

sentimentos = []
urgencias = []

for i, mensagem in enumerate(amostra["instruction"], start=1):
    try:
        resultado = classificar(mensagem)
        sentimentos.append(resultado["sentimento"])
        urgencias.append(resultado["urgencia"])
    except Exception as erro:
        print(f"Erro na mensagem {i}: {erro}")
        sentimentos.append("erro")
        urgencias.append("erro")
    print(f"{i}/200 classificadas")
    time.sleep(1)

amostra["sentimento"] = sentimentos
amostra["urgencia"] = urgencias

os.makedirs("resultados", exist_ok=True)
colunas = ["instruction", "category", "intent", "sentimento", "urgencia"]
amostra[colunas].to_csv("resultados/classificacao_amostra_v2.csv", index=False)
print("Arquivo salvo em resultados/classificacao_amostra_v2.csv")