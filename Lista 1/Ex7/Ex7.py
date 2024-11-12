import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# Define o tamanho da grade (n x n)
n = 100

# Define as probabilidades de gerar 0 ou 1 na grade inicial
p0, p1 = 0.7, 0.3

# Cria uma grade inicial aleatória com 0s e 1s com base nas probabilidades p0 e p1
grid = np.random.choice([0,1], 100*100, p=[p0, p1]).reshape(n, n)

# Função para atualizar a grade a cada frame da animação
def update(frameNum, img, grid):

    # Cria uma cópia da grade atual para calcular a nova geração
    new_grid = grid.copy()

    # Itera sobre cada célula da grade
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            quantidade = 0  # Contador de vizinhos vivos (células com valor 1)

            # Conta os vizinhos vivos ao redor da célula grid[i][j]
            if j > 0:
                quantidade += grid[i][j-1]  # Vizinho à esquerda
            if j < n-1:
                quantidade += grid[i][j+1]  # Vizinho à direita
            if i > 0:
                quantidade += grid[i-1][j]  # Vizinho acima
            if i < n-1:
                quantidade += grid[i+1][j]  # Vizinho abaixo
            if i > 0 and j > 0:
                quantidade += grid[i-1][j-1]  # Vizinho diagonal superior esquerdo
            if i > 0 and j < n-1:
                quantidade += grid[i-1][j+1]  # Vizinho diagonal superior direito
            if i < n-1 and j < n-1:
                quantidade += grid[i+1][j+1]  # Vizinho diagonal inferior direito
            if i < n-1 and j > 0:
                quantidade += grid[i+1][j-1]  # Vizinho diagonal inferior esquerdo

            # Aplica as regras do jogo da vida de Conway
            if grid[i][j] == 0:  # Célula está morta
                if quantidade == 3:
                    new_grid[i][j] = 1  # Nasce uma célula viva (se exatamente 3 vizinhos vivos)
                else:
                    new_grid[i][j] = 0  # Continua morta
            elif grid[i][j] == 1:  # Célula está viva
                if quantidade < 2:
                    new_grid[i][j] = 0  # Morre de solidão (menos de 2 vizinhos vivos)
                elif quantidade >= 2 and quantidade <= 3:
                    new_grid[i][j] = 1  # Sobrevive (2 ou 3 vizinhos vivos)
                elif quantidade > 3:
                    new_grid[i][j] = 0  # Morre de superpopulação (mais de 3 vizinhos vivos)

    # Atualiza a imagem da grade para refletir o novo estado
    img.set_data(new_grid)

    # Copia os dados de new_grid de volta para grid para manter a referência original
    grid[:] = new_grid[:]

    # Adiciona o número do frame no título da janela da animação
    plt.title(f"Game of Life - Frame {frameNum}")
    
    # Retorna a imagem atualizada para a animação
    return img,

# Exibe o valor de grid[1][2] como teste (apenas para debug)
print(grid[1][2])

# Cria a figura e o eixo para a exibição gráfica
fig, ax = plt.subplots()

# Mostra a grade inicial como uma imagem no gráfico
img = ax.imshow(grid, interpolation='nearest')

# Configura a animação, que chama a função update a cada frame
# fargs passa a imagem e a grade como argumentos adicionais para update
ani = animation.FuncAnimation(fig, update, fargs=(img, grid), interval=10)

# Exibe a animação
plt.show()
