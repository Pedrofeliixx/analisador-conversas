-- Exercício 5: as 5 intenções com mensagens mais longas (em palavras)
SELECT
    intent,
    ROUND(AVG(qtd_palavras), 1) AS media_palavras
FROM conversas
GROUP BY intent
ORDER BY media_palavras DESC
LIMIT 5;