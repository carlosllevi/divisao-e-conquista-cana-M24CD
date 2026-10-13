# Feito por: Carlos Levi e Rafael Alencar

def subarranjo_forca_bruta(arr):
    n = len(arr)
    if n == 0: return 0, -1, -1
    max_soma = float('-inf')
    inicio = fim = -1
    for i in range(n):
        soma_atual = 0
        for j in range(i, n):
            soma_atual += arr[j]
            if soma_atual > max_soma:
                max_soma = soma_atual
                inicio, fim = i, j
    return max_soma, inicio, fim

def max_cruzamento(arr, esq, meio, dir):
    soma_esq = float('-inf')
    soma_atual = 0
    max_esq = meio
    for i in range(meio, esq - 1, -1):
        soma_atual += arr[i]
        if soma_atual > soma_esq:
            soma_esq, max_esq = soma_atual, i

    soma_dir = float('-inf')
    soma_atual = 0
    max_dir = meio + 1
    for j in range(meio + 1, dir + 1):
        soma_atual += arr[j]
        if soma_atual > soma_dir:
            soma_dir, max_dir = soma_atual, j
    return soma_esq + soma_dir, max_esq, max_dir

def subarranjo_dc(arr, esq, dir):
    if esq == dir: return arr[esq], esq, dir
    meio = (esq + dir) // 2
    soma_e, i_e, j_e = subarranjo_dc(arr, esq, meio)
    soma_d, i_d, j_d = subarranjo_dc(arr, meio + 1, dir)
    soma_c, i_c, j_c = max_cruzamento(arr, esq, meio, dir)
    
    if soma_e >= soma_d and soma_e >= soma_c: return soma_e, i_e, j_e
    elif soma_d >= soma_e and soma_d >= soma_c: return soma_d, i_d, j_d
    else: return soma_c, i_c, j_c