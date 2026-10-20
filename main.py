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

import math

# Etapa 2: Par de Pontos Mais Próximos
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def pontos_forca_bruta(pontos):
    n = len(pontos)
    min_d = float('inf')
    par = None
    for i in range(n):
        for j in range(i + 1, n):
            d = dist(pontos[i], pontos[j])
            if d < min_d:
                min_d = d
                par = (pontos[i], pontos[j])
    return min_d, par

def pontos_dc_rec(pontos_x, pontos_y):
    n = len(pontos_x)
    if n <= 3: return pontos_forca_bruta(pontos_x)
    
    meio = n // 2
    ponto_mid = pontos_x[meio]
    
    esq_x, dir_x = pontos_x[:meio], pontos_x[meio:]
    esq_y = [p for p in pontos_y if p[0] <= ponto_mid[0]]
    dir_y = [p for p in pontos_y if p[0] > ponto_mid[0]]
    
    d1, par1 = pontos_dc_rec(esq_x, esq_y)
    d2, par2 = pontos_dc_rec(dir_x, dir_y)
    d, par_min = (d1, par1) if d1 < d2 else (d2, par2)
    
    faixa = [p for p in pontos_y if abs(p[0] - ponto_mid[0]) < d]
    
    for i in range(len(faixa)):
        for j in range(i + 1, min(i + 8, len(faixa))):
            d_faixa = dist(faixa[i], faixa[j])
            if d_faixa < d:
                d = d_faixa
                par_min = (faixa[i], faixa[j])
                
    return d, par_min

def pontos_dc(pontos):
    px = sorted(pontos, key=lambda x: x[0])
    py = sorted(pontos, key=lambda x: x[1])
    return pontos_dc_rec(px, py)