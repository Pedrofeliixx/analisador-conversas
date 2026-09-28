import sqlite3
import pandas as pd

conexao = sqlite3.connect("data/conversas.db")

# Lê a consulta que você escreveu no arquivo .sql
with open("sql/consultas.sql", encoding="utf-8") as arquivo:
    consulta = arquivo.read()

# Executa no banco e traz o resultado como tabela
resultado = pd.read_sql(consulta, conexao)

print("=== Exercício 5 (SQL): intenções com mensagens mais longas ===")
print(resultado)

conexao.close()


