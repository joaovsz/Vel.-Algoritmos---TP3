def contar_repeticoes(s, char):
    if not s:
        return 0
    if s[0] == char:
        return 1 + contar_repeticoes(s[1:], char)
    else:
        return contar_repeticoes(s[1:], char)

print(contar_repeticoes("banana", "a"))