import cv2
import os

# Nome exato do seu arquivo de vídeo
nome_video = 'IMG_0354.MOV'

# Cria uma pasta chamada 'frames' para organizar as imagens extraídas
pasta_destino = 'frames'
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Inicia a captura do vídeo usando o OpenCV
cap = cv2.VideoCapture(nome_video)

# Variável para controlar o número da imagem (im1, im2...)
contador = 1

# Inicia o laço de repetição para ler todos os quadros
while True:
    # A função read() devolve se deu certo (sucesso) e a imagem em si (frame)
    sucesso, frame = cap.read()
    
    # Se não tiver mais quadros (acabou o vídeo), sai do laço
    if not sucesso:
        break
        
    # Converte o quadro colorido original para tons de cinza (requisito do professor)
    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Monta o caminho e o nome final do arquivo (ex: frames/im1.jpg)
    nome_arquivo = os.path.join(pasta_destino, f'im{contador}.jpg')
    
    # Salva a imagem convertida
    cv2.imwrite(nome_arquivo, frame_cinza)
    
    print(f'Imagem {nome_arquivo} salva.')
    
    # Aumenta a contagem para a próxima imagem
    contador += 1

# Libera o arquivo de vídeo da memória
cap.release()

print('Extração finalizada com sucesso! Verifique a pasta "frames".')