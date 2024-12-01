def imprimir_torres(torres):
    for nome, discos in torres.items():
        print(f"{nome}: {discos}")

def mover_disco(torres, origem, destino):
    disco = torres[origem].pop()
    torres[destino].append(disco)
    imprimir_torres(torres)

def torre_de_hanoi(n, origem, destino, auxiliar, torres):
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        mover_disco(torres, origem, destino)
    else:
        torre_de_hanoi(n - 1, origem, auxiliar, destino, torres)
        print(f"Mover disco {n} de {origem} para {destino}")
        mover_disco(torres, origem, destino)
        torre_de_hanoi(n - 1, auxiliar, destino, origem, torres)

n = 3
torres = {
    'A': list(range(n, 0, -1)),
    'B': [],
    'C': []
}

imprimir_torres(torres)
torre_de_hanoi(n, 'A', 'C', 'B', torres)
