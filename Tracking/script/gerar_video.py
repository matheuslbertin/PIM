import cv2
import os

print("Iniciando a renderização do vídeo final...")

# 1. Configurações Iniciais
metodo = cv2.TM_SQDIFF_NORMED
template = cv2.imread('template.jpg', cv2.IMREAD_GRAYSCALE)

# Pega a largura (w) e altura (h) do template para desenhar o retângulo do tamanho exato
h, w = template.shape

# 2. Configuração do Vídeo de Saída
# Lê a primeira imagem para descobrir o tamanho (resolução) do vídeo
frame_teste = cv2.imread('frames/im1.jpg')
altura, largura, _ = frame_teste.shape

# Configura o formato MP4 (garantia de compatibilidade) e 30 frames por segundo
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_saida = cv2.VideoWriter('resultado_rastreio.mp4', fourcc, 30.0, (largura, altura))

# Descobre quantas imagens existem na pasta
arquivos = [f for f in os.listdir('frames') if f.startswith('im') and f.endswith('.jpg')]
num_frames = len(arquivos)

# 3. Loop de Rastreamento e Desenho
for i in range(1, num_frames + 1):
    caminho_img = f'frames/im{i}.jpg'
    
    # Precisamos ler a imagem duas vezes:
    # Uma colorida (para desenhar o retângulo verde bonito)
    frame_colorido = cv2.imread(caminho_img)
    # E uma cinza (para a matemática do OpenCV funcionar)
    frame_cinza = cv2.cvtColor(frame_colorido, cv2.COLOR_BGR2GRAY)
    
    # Aplica o método Campeão
    res = cv2.matchTemplate(frame_cinza, template, metodo)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # Como usamos o SQDIFF, a melhor resposta está no min_loc (menor diferença)
    canto_superior_esquerdo = min_loc
    canto_inferior_direito = (canto_superior_esquerdo[0] + w, canto_superior_esquerdo[1] + h)
    
    # Desenha o retângulo verde (0, 255, 0) com espessura 2
    cv2.rectangle(frame_colorido, canto_superior_esquerdo, canto_inferior_direito, (0, 255, 0), 2)
    
    # Grava esse frame riscado no nosso vídeo final
    video_saida.write(frame_colorido)
    
    # Mostra o progresso no terminal a cada 50 
    if i % 50 == 0:
        print(f"Renderizando frame {i} de {num_frames}...")

# Fecha o arquivo de vídeo e libera a memória
video_saida.release()

print("Vídeo renderizado com sucesso! Abra o arquivo 'resultado_rastreio.mp4'.")