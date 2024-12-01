import os

def listar_diretorios_recursivo(caminho, ignorar_paths=["venv", "tp1_files"], nivel=0):
    try:
        with os.scandir(caminho) as itens:
            for item in itens:
                indentacao = "    " * nivel
                if item.is_dir(follow_symlinks=False):
                    if item.name in ignorar_paths:
                        print(f"{indentacao}Ignorando pasta: {item.path}")
                        continue
                    print(f"{indentacao}Diretório: {item.path}")
                    listar_diretorios_recursivo(item.path, ignorar_paths, nivel + 1)
                else:
                    print(f"{indentacao}Arquivo: {item.path}")
    except PermissionError:
        print(f"Permissão negada: {caminho}")

if __name__ == "__main__":
    caminho_inicial = os.path.expanduser("~/Documentos/Faculdade")
    listar_diretorios_recursivo(caminho_inicial)
