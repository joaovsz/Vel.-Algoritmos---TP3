# def fatorial_recursivo(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fatorial_recursivo(n - 1)

# try:
#     resultado = fatorial_recursivo(2988)
#     print(f"Fatorial calculado com sucesso: {resultado}")
# except RecursionError:
#     print("Erro: Stack Overflow ocorreu devido à profundidade de recursão.")

# ////////////////////////////////////////////////////////////////////////////

def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n_teste = 2972
try:
    resultado = fatorial_iterativo(n_teste)
    print("Iterativo calculou com sucesso.")
except Exception as e:
    print(f"Erro na abordagem iterativa: {e}")
