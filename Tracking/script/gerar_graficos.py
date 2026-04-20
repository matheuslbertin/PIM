import pandas as pd
import matplotlib.pyplot as plt
import os

# Lista dos métodos gerados
metodos = [
    'TM_CCOEFF', 'TM_CCOEFF_NORMED', 
    'TM_CCORR', 'TM_CCORR_NORMED', 
    'TM_SQDIFF', 'TM_SQDIFF_NORMED'
]

print("Lendo os arquivos CSV e gerando os gráficos...")

for metodo in metodos:
    arquivo_csv = f'{metodo}.csv'
    
    if not os.path.exists(arquivo_csv):
        print(f"Aviso: {arquivo_csv} não encontrado.")
        continue

    # Lê o arquivo CSV
    df = pd.read_csv(arquivo_csv)
    
    # Extrai apenas o número da imagem (tira o 'im' e o '.jpg') para organizar o eixo X
    df['num_quadro'] = df['Quadro (imagem)'].str.extract(r'(\d+)').astype(int)
    
    # Garante que os dados estão em ordem cronológica
    df = df.sort_values('num_quadro')

    # Configura o visual do gráfico
    plt.figure(figsize=(10, 5))
    
    # Desenha as linhas azul (min_val) e vermelha (max_val) 
    plt.plot(df['num_quadro'], df['min_val'], label='min_val', color='blue', linewidth=2)
    plt.plot(df['num_quadro'], df['max_val'], label='max_val', color='red', linewidth=2)
    
    # Títulos e legendas
    plt.title(f'Análise de Rastreio - {metodo}')
    plt.xlabel('Número da Imagem (Frame)')
    plt.ylabel('Valor da Resposta')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Salva o gráfico como imagem
    nome_grafico = f'grafico_{metodo}.png'
    plt.savefig(nome_grafico)
    plt.close() # Fecha a figura da memória

print("Sucesso! Verifique a sua pasta, os 6 gráficos foram gerados em formato PNG.")