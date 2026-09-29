from dotenv import load_dotenv
import anthropic

load_dotenv()

cliente = anthropic.Anthropic()

resposta = cliente.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=50,
    messages=[
        {
            "role": "user",
            "content": "Classifique o sentimento desta mensagem de cliente como positivo, neutro ou negativo. Responda só com uma palavra: 'I want a refund, this product is terrible'"
        }
    ]
)

print(resposta.content[0].text)
print(resposta.usage)