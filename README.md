# PIM
Repositório dedicado à disciplina de Processamento de Imagem, contendo os trabalhos desenvolvidos ao longo do curso, incluindo implementações, experimentos e análises relacionadas aos conceitos estudados.

### Fase 1: Captação e Preparação (Passos A, B, C e D)
* [cite_start][ ] **Gravar o Vídeo Base:** Faça um vídeo de pelo menos 10 segundos (mínimo de 300 quadros) mostrando um objeto se movendo lentamente[cite: 120]. 
    * [cite_start]*Regras:* Câmera estática, fundo constante, foco automático desligado, resolução mínima de 640x480 (VGA)[cite: 120, 121].
* [cite_start][ ] **Extrair Frames:** Crie um script Python simples com OpenCV para ler esse vídeo e salvar cada quadro como uma imagem individual (ex: `im1.jpg`, `im2.jpg`, etc.)[cite: 126].
* [cite_start][ ] **Converter para Cinza:** Garanta que esse mesmo script converta as imagens salvas para tons de cinza[cite: 125].
* [cite_start][ ] **Criar o Template:** Abra a primeira imagem (`im1`) em um editor de imagens ou via código, recorte apenas a região que contém o objeto que será rastreado e salve como `template.jpg`[cite: 155].

### Fase 2: O Rastreamento e Coleta de Dados (Passos E e F)
* [cite_start][ ] **Script Principal:** Crie o script `.py` que fará o loop de leitura da imagem `im2` até a `im300`[cite: 161].
* [cite_start][ ] **Aplicar os 6 Métodos:** Para cada frame no loop, aplique a função `cvMatchTemplate` usando os seguintes métodos do OpenCV: `'cv.TM_CCOEFF'`, `'cv.TM_CCOEFF_NORMED'`, `'cv.TM_CCORR'`, `'cv.TM_CCORR_NORMED'`, `'cv.TM_SQDIFF'` e `'cv.TM_SQDIFF_NORMED'`[cite: 156, 157, 158].
* [cite_start][ ] **Extrair Valores:** Use a função `cvMinMaxLoc` para capturar os valores de `min_val` e `max_val` de cada método em cada frame[cite: 159].
* [cite_start][ ] **Gerar os CSVs:** Exporte os dados capturados para 6 arquivos CSV diferentes (um para cada método), contendo as colunas: "Método", "Quadro (imagem)", "min_val" e "max_val"[cite: 160].

### Fase 3: Análise e Visualização (Passos F, G e H)
* [cite_start][ ] **Plotar os Gráficos:** Crie gráficos de linha (pode usar o `matplotlib` no Python) mostrando a variação das respostas (`min_val` e `max_val` no eixo Y) em relação ao número da imagem (eixo X)[cite: 162, 163]. [cite_start]Faça um gráfico para cada método testado[cite: 162].
* [cite_start][ ] **Escolher o Vencedor:** Analise os gráficos gerados e escolha o melhor método de rastreio de forma justificada[cite: 177].
* [cite_start][ ] **Gerar Vídeo de Saída:** Com o melhor método escolhido, crie um script que desenha o retângulo sobre o objeto rastreado em cada frame e salve o resultado como um novo vídeo[cite: 179].

### Fase 4: O Desafio Extra (Passo I)
* [cite_start][ ] **Cena Complexa:** Repita *todos* os passos acima, mas agora com um vídeo de uma cena mais complexa (como um mascote se movendo com um fundo cheio de informações)[cite: 188, 189].

### Fase 5: Empacotamento e Entrega via Moodle
* [cite_start][ ] **Comentar o Código:** Garanta que todos os seus scripts `.py` tenham comentários explicativos nos trechos mais importantes[cite: 193].
* [cite_start][ ] **Escrever o Relatório:** Redija o relatório contendo embasamento teórico, metodologia, os gráficos gerados, análise dos resultados e conclusão[cite: 195, 196]. [cite_start]Não esqueça de incluir o identificador da equipe (máximo 3 pessoas)[cite: 191].
* [cite_start][ ] **Montar o ZIP:** Junte os quadros individuais, o vídeo de entrada, o vídeo de saída marcado, os arquivos CSV, os gráficos, os códigos-fontes e o relatório final[cite: 198]. [cite_start]Envie pelo Moodle[cite: 190].
