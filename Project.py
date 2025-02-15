# Importação das bibliotecas necessárias
import cv2  # Biblioteca OpenCV para processamento de imagens
import numpy as np  # Biblioteca NumPy para manipulação de arrays
import matplotlib.pyplot as plt  # Biblioteca Matplotlib para visualização
 
# Função para converter uma imagem colorida para tons de cinza
def converter_para_cinza(imagem):
    """
    Converte uma imagem colorida (RGB) para tons de cinza.
    A conversão é feita usando a fórmula ponderada:
        0.299 * R + 0.587 * G + 0.114 * B
    Essa fórmula dá mais peso ao canal verde (G), que é percebido mais fortemente pelo olho humano.
    """
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    return imagem_cinza

# Função para binarizar uma imagem em preto e branco
def binarizar_imagem(imagem_cinza, limiar=128):
    """
    Binariza uma imagem em escala de cinza, definindo pixels abaixo do limiar como 0 (preto)
    e pixels acima ou igual ao limiar como 255 (branco).
    Parâmetros:
        - imagem_cinza: Imagem em tons de cinza.
        - limiar: Valor de corte (threshold). Pixels abaixo deste valor são convertidos para 0.
    Retorna:
        - imagem_binarizada: Imagem binária (preto e branco).
    """
    _, imagem_binarizada = cv2.threshold(imagem_cinza, limiar, 255, cv2.THRESH_BINARY)
    return imagem_binarizada

# Função principal
def main():
    """
    Função principal que carrega uma imagem, converte-a para tons de cinza,
    binariza a imagem e exibe os resultados.
    """
    # Carrega a imagem colorida
    caminho_imagem = "pietro-de-grandi-T7K4aEPoGGk-unsplash-1024x683.jpg"  # Nome da imagem fornecido
    imagem_colorida = cv2.imread(caminho_imagem)

    # Verifica se a imagem foi carregada corretamente
    if imagem_colorida is None:
        print("Erro: Imagem não encontrada. Verifique o caminho.")
        return

    # Converte a imagem para tons de cinza
    imagem_cinza = converter_para_cinza(imagem_colorida)

    # Define o limiar para binarização e aplica a função
    limiar = 128  # Valor padrão para o limiar (pode ser ajustado conforme necessário)
    imagem_binarizada = binarizar_imagem(imagem_cinza, limiar)

    # Exibe as imagens usando Matplotlib
    plt.figure(figsize=(12, 6))  # Define o tamanho da figura

    # Subplot 1: Imagem Colorida Original
    plt.subplot(1, 3, 1)
    plt.title("Imagem Colorida")  # Título do gráfico
    plt.imshow(cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2RGB))  # Converte BGR para RGB para exibição correta
    plt.axis("off")  # Remove os eixos para melhor visualização

    # Subplot 2: Imagem em Tons de Cinza
    plt.subplot(1, 3, 2)
    plt.title("Tons de Cinza")
    plt.imshow(imagem_cinza, cmap="gray")  # Usa o mapa de cores 'gray' para escala de cinza
    plt.axis("off")

    # Subplot 3: Imagem Binarizada
    plt.subplot(1, 3, 3)
    plt.title("Imagem Binarizada")
    plt.imshow(imagem_binarizada, cmap="gray")  # Usa o mapa de cores 'gray' para preto e branco
    plt.axis("off")

    # Mostra as imagens na tela
    plt.show()

    # Salva as imagens processadas no disco (opcional)
    cv2.imwrite("imagem_cinza.jpg", imagem_cinza)  # Salva a imagem em tons de cinza
    cv2.imwrite("imagem_binarizada.jpg", imagem_binarizada)  # Salva a imagem binarizada
    print("Imagens salvas com sucesso!")

# Executa o programa
if __name__ == "__main__":
    main()