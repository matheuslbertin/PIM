### Fase 1: Captação e Preparação (Passos A, B, C e D)
- [✅] **Gravar o Vídeo Base:** Faça um vídeo de pelo menos 10 segundos (mínimo de 300 quadros).
- [✅] *Regras:* Mostre um objeto se movendo lentamente. Use câmera estática e fundo constante.
- [✅] *Configuração da Câmera:* Foco automático desligado e resolução mínima de 640x480 (VGA).
- [✅] **Extrair Frames:** Crie um script Python simples com OpenCV para ler o vídeo e salvar cada quadro como uma imagem.
- [✅] **Converter para Cinza:** Garanta que esse mesmo script converta as imagens salvas para tons de cinza.
- [✅] **Criar o Template:** Abra a primeira imagem (`im1`) e recorte apenas a região que contém o objeto rastreado. Salve como `template.jpg`.

### Fase 2: O Rastreamento e Coleta de Dados (Passos E e F)
- [✅] **Script Principal:** Crie o script `.py` que fará o loop de leitura da imagem `im2` até a `im300`.
- [✅] **Aplicar os 6 Métodos:** Em cada frame, aplique a função `cvMatchTemplate`.
- [✅] *Métodos a usar:* `cv.TM_CCOEFF`, `cv.TM_CCOEFF_NORMED`, `cv.TM_CCORR`, `cv.TM_CCORR_NORMED`, `cv.TM_SQDIFF` e `cv.TM_SQDIFF_NORMED`.
- [✅] **Extrair Valores:** Use a função `cvMinMaxLoc` para capturar os valores de `min_val` e `max_val` de cada método.
- [✅] **Gerar os CSVs:** Exporte os dados capturados para 6 arquivos CSV diferentes (um por método).
- [✅] *Colunas do CSV:* "Método", "Quadro (imagem)", "min_val" e "max_val".

### Fase 3: Análise e Visualização (Passos F, G e H)
- [✅] **Plotar os Gráficos:** Crie gráficos de linha mostrando a variação das respostas (`min_val` e `max_val`) em relação ao número da imagem.
- [✅] **Escolher o Vencedor:** Analise os gráficos e escolha o melhor método de rastreio de forma justificada.
- [✅] **Gerar Vídeo de Saída:** Crie um script que desenha o retângulo sobre o objeto rastreado usando o melhor método. Salve como um novo vídeo.

### Fase 4: Empacotamento e Entrega via Moodle
- [✅] **Comentar o Código:** Revise todos os seus scripts `.py` e adicione comentários nos trechos importantes.
- [✅] **Escrever o Relatório:** Redija o documento com embasamento teórico, metodologia, gráficos, análise e conclusão.
- [✅] **Montar o ZIP:** Junte os quadros, vídeos (entrada e saída), arquivos CSV, gráficos, códigos-fontes e o relatório.
- [✅] **Enviar:** Faça o upload do arquivo ZIP no Moodle.