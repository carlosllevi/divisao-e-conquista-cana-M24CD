# Feito por: Carlos Levi e Rafael Alencar
# Etapa 1: Subarranjo de Soma Máxima - Força Bruta

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

if __name__ == "__main__":
    teste = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Força Bruta:", subarranjo_forca_bruta(teste))