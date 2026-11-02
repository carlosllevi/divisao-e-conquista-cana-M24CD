import time
import random
import csv
import matplotlib.pyplot as plt
from main import subarranjo_forca_bruta, subarranjo_dc, subarranjo_linear, pontos_forca_bruta, pontos_dc

def run_benchmark():
    tamanhos = [100, 200, 400, 800, 1600, 3200, 6400]
    execucoes = 5
    resultados = []

    print("Iniciando medições de tempo...")
    for n in tamanhos:
        tempos = {'n': n, 'soma_fb': 0, 'soma_dc': 0, 'soma_lin': 0, 'pontos_fb': 0, 'pontos_dc': 0}
        
        for _ in range(execucoes):
            # 1. Gerar massa de dados aleatória
            arr = [random.randint(-1000, 1000) for _ in range(n)]
            pontos = [(random.randint(0, 10000), random.randint(0, 10000)) for _ in range(n)]
            
            # 2. Etapa 1: Subarranjo de Soma Máxima
            t0 = time.time()
            subarranjo_forca_bruta(arr)
            tempos['soma_fb'] += (time.time() - t0) * 1000  # converter para milissegundos
            
            t0 = time.time()
            subarranjo_dc(arr, 0, n - 1)
            tempos['soma_dc'] += (time.time() - t0) * 1000
            
            t0 = time.time()
            subarranjo_linear(arr)
            tempos['soma_lin'] += (time.time() - t0) * 1000
            
            # 3. Etapa 2: Par de Pontos Mais Próximos
            t0 = time.time()
            pontos_forca_bruta(pontos)
            tempos['pontos_fb'] += (time.time() - t0) * 1000
            
            t0 = time.time()
            pontos_dc(pontos)
            tempos['pontos_dc'] += (time.time() - t0) * 1000
            
        # Calcular média das 5 execuções
        for key in tempos:
            if key != 'n':
                tempos[key] /= execucoes
        resultados.append(tempos)
        print(f"Tamanho N={n} concluído.")

    # Exportar resultados brutos para CSV
    with open('resultados_tempos.csv', 'w', newline='', encoding='utf-8') as csvfile:
        campos = ['n', 'soma_fb', 'soma_dc', 'soma_lin', 'pontos_fb', 'pontos_dc']
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
        for r in resultados:
            writer.writerow(r)
    print("Arquivo 'resultados_tempos.csv' exportado com sucesso.")
    
    # Gerar e exportar os Gráficos
    ns = [r['n'] for r in resultados]
    
    # Gráfico 1: Etapa 1
    plt.figure(figsize=(10, 6))
    plt.plot(ns, [r['soma_fb'] for r in resultados], label='Força Bruta O(n²)', marker='o', color='red')
    plt.plot(ns, [r['soma_dc'] for r in resultados], label='Divisão e Conquista O(n log n)', marker='s', color='blue')
    plt.plot(ns, [r['soma_lin'] for r in resultados], label='Algoritmo de Kadane O(n)', marker='^', color='green')
    plt.title('Etapa 1: Subarranjo de Soma Máxima')
    plt.xlabel('Tamanho da Entrada (N)')
    plt.ylabel('Tempo de Execução (ms)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('grafico_etapa1.png')
    plt.close()
    
    # Gráfico 2: Etapa 2
    plt.figure(figsize=(10, 6))
    plt.plot(ns, [r['pontos_fb'] for r in resultados], label='Força Bruta O(n²)', marker='o', color='red')
    plt.plot(ns, [r['pontos_dc'] for r in resultados], label='Divisão e Conquista O(n log n)', marker='s', color='blue')
    plt.title('Etapa 2: Par de Pontos Mais Próximos')
    plt.xlabel('Tamanho da Entrada (N)')
    plt.ylabel('Tempo de Execução (ms)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('grafico_etapa2.png')
    plt.close()
    print("Gráficos gerados e salvos como 'grafico_etapa1.png' e 'grafico_etapa2.png'.")

if __name__ == '__main__':
    run_benchmark()