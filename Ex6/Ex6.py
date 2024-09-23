import numpy as np  
from matplotlib import pyplot as plt  


# Cria uma classe para representar um ponto que recebe suas coordenadas (x, y)
class Ponto: 
    def __init__(self, x, y):  # Construtor da classe que inicializa as coordenadas
        self.x = x
        self.y = y

xs = []  # Lista para armazenar as coordenadas x dos pontos
ys = []  # Lista para armazenar as coordenadas y dos pontos
linhas = []  # Lista para armazenar as conexões (arestas) entre os pontos como tuplas

# Cria a classe Grafo, que contém métodos para manipular a matriz de adjacência e visualização
class Grafo:
    def __init__(self):  # Inicializa a classe
        self.matriz = []  # Matriz de adjacência que representa as ligações entre os pontos
        self.textos = []  # Lista para armazenar os textos (rótulos) associados aos pontos
        self.i = 0  # Contador para numerar os pontos adicionados ao grafo

    # Função para criar uma matriz inicial de adjacência com zeros
    def criarInicial(self, n):
        self.matriz = np.zeros(shape=(n, n), dtype=int)  # Cria uma matriz n x n preenchida com zeros
    
    # Função para mostrar a matriz de adjacência no console
    def mostrarGrafo(self):
        for i in self.matriz:  # Para cada linha da matriz de adjacência
            print(i)  # Imprime a linha
    
    # Função para adicionar uma ligação (aresta) entre dois pontos n e z
    def adicionarLigacao(self, n, z):
        self.matriz[n, z] = 1  # Adiciona 1 à matriz de adjacência para indicar a ligação
        novacoordx = (xs[n], xs[z])  # Coordenadas x dos dois pontos conectados
        novacoordy = (ys[n], ys[z])  # Coordenadas y dos dois pontos conectados
        
        # Desenha a linha entre os dois pontos (ligação) no gráfico
        linha, = plt.plot(novacoordx, novacoordy, color='black', zorder=1)  
        linhas.append((n, z, linha))  # Armazena a linha e os pontos conectados

    # Função para adicionar um ponto ao grafo, com coordenadas (cx, cy)
    def adicionarPonto(self, cx, cy):
        # Cria uma nova matriz de adjacência maior para incluir o novo ponto
        matriz_zero = np.zeros(shape=(len(self.matriz)+1, len(self.matriz)+1), dtype=int)
        matriz_zero[:len(self.matriz), :len(self.matriz)] = self.matriz  # Copia a matriz existente para a nova
        self.matriz = matriz_zero  # Atualiza a matriz de adjacência com a nova matriz

        ponto = Ponto(cx, cy)  # Cria um novo ponto com as coordenadas fornecidas
        # Adiciona um rótulo ao ponto, posicionando-o levemente acima da coordenada y
        texto = plt.text(cx, cy + 0.2, str(self.i), fontsize=12, ha='center')
        self.textos.append(texto)  # Armazena o rótulo do ponto
        xs.append(cx)  # Armazena a coordenada x do ponto
        ys.append(cy)  # Armazena a coordenada y do ponto
        self.i = self.i + 1  # Incrementa o contador de pontos

    # Função para plotar o gráfico com todos os pontos e conexões
    def plotarGrafico(self):
        self.grafico = plt.scatter(xs, ys, s=300, zorder=2)  # Desenha os pontos no gráfico
        plt.show()  # Exibe o gráfico

    # Função para remover um ponto do grafo, dado seu índice p
    def removerPonto(self, p):
        # Remove as linhas conectadas ao ponto a ser removido
        for (n, z, linha) in linhas[:]:  # Itera sobre todas as linhas (arestas)
            if n == p or z == p:  # Se o ponto está envolvido na conexão
                linha.remove()  # Remove a linha do gráfico
                linhas.remove((n, z, linha))  # Remove a linha da lista de linhas
        
        # Remove a linha e a coluna correspondente ao ponto na matriz de adjacência
        self.matriz = np.delete(self.matriz, p, axis=0)
        self.matriz = np.delete(self.matriz, p, axis=1)
        
        # Remove as coordenadas do ponto nas listas xs e ys
        del xs[p]
        del ys[p]
        
        # Remove todos os rótulos dos pontos
        for texto in self.textos:
            texto.remove()  # Remove o texto do gráfico
        self.textos.clear()  # Limpa a lista de textos (rótulos)
        
        # Re-adiciona os rótulos corrigidos, atualizando o índice dos pontos restantes
        for i, (x, y) in enumerate(zip(xs, ys)):
            texto = plt.text(x, y + 0.2, str(i), fontsize=12, ha='center')  # Reinsere o rótulo
            self.textos.append(texto)  # Armazena o novo rótulo

# Instancia um grafo e começa a adicionar pontos e ligações
grafo = Grafo()  # Cria uma instância da classe Grafo
grafo.criarInicial(0)  # Inicializa a matriz de adjacência vazia (sem pontos inicialmente)

# Adiciona pontos ao grafo com coordenadas específicas
grafo.adicionarPonto(0, 0)  # Ponto no centro (0, 0)
grafo.adicionarPonto(1, 1)  # Ponto (1, 1)
grafo.adicionarPonto(2, 1)  # Ponto (2, 1)
grafo.adicionarPonto(1, -1)  # Ponto (1, -1)
grafo.adicionarPonto(2, -1)  # Ponto (2, -1)
grafo.adicionarPonto(3.8, -1.2)  # Ponto (3.8, -1.2)
grafo.adicionarPonto(4, 1.5)  # Ponto (4, 1.5)
grafo.adicionarPonto(5, 0.3)  # Ponto (5, 0.3)
grafo.adicionarPonto(6, 1.5)  # Ponto (6, 1.5)
grafo.adicionarPonto(6, -1)  # Ponto (6, -1)

# Adiciona ligações entre os pontos (arestas)
grafo.adicionarLigacao(0, 1)  # Conexão entre o ponto 0 e o ponto 1
grafo.adicionarLigacao(1, 3)  # Conexão entre o ponto 1 e o ponto 3
grafo.adicionarLigacao(1, 2)  # Conexão entre o ponto 1 e o ponto 2
grafo.adicionarLigacao(3, 4)  # Conexão entre o ponto 3 e o ponto 4
grafo.adicionarLigacao(4, 2)  # Conexão entre o ponto 4 e o ponto 2
grafo.adicionarLigacao(2, 6)  # Conexão entre o ponto 2 e o ponto 6
grafo.adicionarLigacao(6, 5)  # Conexão entre o ponto 6 e o ponto 5
grafo.adicionarLigacao(6, 7)  # Conexão entre o ponto 6 e o ponto 7
grafo.adicionarLigacao(5, 7)  # Conexão entre o ponto 5 e o ponto 7
grafo.adicionarLigacao(7, 8)  # Conexão entre o ponto 7 e o ponto 8
grafo.adicionarLigacao(8, 9)  # Conexão entre o ponto 8 e o ponto 9

grafo.mostrarGrafo()  # Mostra a matriz de adjacência no console
grafo.plotarGrafico()  # Plota o gráfico final com todos os pontos e ligações