# Exercício 5 – Preço com desconto
# Peça o preço de um produto e aplique 10% de desconto.

preco = float(input("Digite o preço do produto: "))
desconto = preco * 0.10
final = preco - desconto

print(f"O preço com desconto é: R$ {final:.2f}")