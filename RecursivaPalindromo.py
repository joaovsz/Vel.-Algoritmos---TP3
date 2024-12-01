def eh_palindromo(palavra):
    if len(palavra) <= 1:
        return "Sim"
    if palavra[0] != palavra[-1]:
        return "Não"
    return eh_palindromo(palavra[1:-1])

palavra = "kayak"
print(f"A palavra '{palavra}' é um palíndromo? {eh_palindromo(palavra)}")

palavra = "python"
print(f"A palavra '{palavra}' é um palíndromo? {eh_palindromo(palavra)}")