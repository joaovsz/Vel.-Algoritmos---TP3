def soma_recursiva(lista):
    if not lista:
        return 0
    soma = lista[0] + soma_recursiva(lista[1:])
    print(f"Lista: {lista}, Soma parcial: {soma}")
    return soma

# Exemplo de uso
lista = [1, 2, 3, 4, 5]
resultado = soma_recursiva(lista)
print(f"Soma total: {resultado}")
