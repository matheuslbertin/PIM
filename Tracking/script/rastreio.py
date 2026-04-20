import cv2
import os
import csv

# Lista com os 6 métodos 
metodos = [
    ('TM_CCOEFF', cv2.TM_CCOEFF),
    ('TM_CCOEFF_NORMED', cv2.TM_CCOEFF_NORMED),
    ('TM_CCORR', cv2.TM_CCORR),
    ('TM_CCORR_NORMED', cv2.TM_CCORR_NORMED),
    ('TM_SQDIFF', cv2.TM_SQDIFF),
    ('TM_SQDIFF_NORMED', cv2.TM_SQDIFF_NORMED)
]

# Carrega a imagem que serve como molde (template) em tons de cinza [cite: 155]
template = cv2.imread('template.jpg', cv2.IMREAD_GRAYSCALE)

# Trava de segurança caso o template não seja encontrado
if template is None:
    print("Erro: O arquivo 'template.jpg' não foi encontrado nesta pasta!")
    exit()

pasta_frames = 'frames'

# Conta quantas imagens foram extraídas para sabermos até onde o loop deve ir
arquivos = [f for f in os.listdir(pasta_frames) if f.startswith('im') and f.endswith('.jpg')]
num_frames = len(arquivos)

print(f"Iniciando a análise de {num_frames - 1} quadros. Isso pode levar alguns segundos...")

# Dicionário para organizar os resultados de cada método antes de salvar
resultados = {nome: [] for nome, _ in metodos}

# Inicia a partir da imagem 2 (im2, im3, etc...) 
for i in range(2, num_frames + 1):
    nome_img = f'im{i}.jpg'
    caminho_img = os.path.join(pasta_frames, nome_img)
    
    # Lê o quadro atual em tons de cinza
    img = cv2.imread(caminho_img, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        continue # Ignora caso algum arquivo tenha corrompido
        
    # Aplica os 6 métodos na imagem atual 
    for nome_metodo, metodo in metodos:
        # A função matchTemplate faz o rastreio real 
        res = cv2.matchTemplate(img, template, metodo)
        
        # A função minMaxLoc extrai as respostas máxima e mínima 
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        # Guarda os dados na nossa lista
        resultados[nome_metodo].append([nome_img, min_val, max_val])

print("Processamento das imagens concluído! Gerando os arquivos CSV...")

# Loop final para criar e salvar as 6 tabelas CSV 
for nome_metodo in resultados:
    nome_arquivo_csv = f'{nome_metodo}.csv'
    
    with open(nome_arquivo_csv, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        
        # Escreve o cabeçalho idêntico ao solicitado no roteiro 
        writer.writerow(['Método', 'Quadro (imagem)', 'min_val', 'max_val'])
        
        # Escreve linha por linha com os dados extraídos
        for linha in resultados[nome_metodo]:
            writer.writerow([nome_metodo] + linha)

print("Tudo pronto! Verifique sua pasta, os 6 arquivos CSV foram criados.")