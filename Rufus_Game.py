import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)

fonte = pygame.font.SysFont("arial", 32, True, False)

amarelo = (255, 255, 0)
vinho  = (41, 14, 14)
marrom = (15, 0, 0)
verde = (114, 245, 66)
velocidade = 1

#Classe para  cenario (MAPA)
class Cenario: 
    def __init__(self, tamanho, rufus):
        self.rufus = rufus
        self.tamanho = tamanho
        self.pontos = 0
        self.matriz =[ 
             [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 2, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 3, 3, 0, 0, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2],
            [2, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 3, 3, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]
    
    def mostrar_texto(self, tela):
        pontos_x = 30 * self.tamanho
        img_pontos = fonte.render("Pontos: {}".format(self.pontos), True, amarelo)
        tela.blit(img_pontos, (pontos_x, 50))


    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            metade = self.tamanho // 2
            cor = marrom
            if coluna == 2:
                pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)

            if coluna == 1: 
                pygame.draw.circle(tela, amarelo, (x + metade, y + metade), self.tamanho // 10, 0)
            
            if coluna == 3:
                pygame.draw.rect(tela, verde, (x, y, self.tamanho, self.tamanho), 0)


    def pintar(self, tela): 
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)
        self.mostrar_texto(tela)
    def calcular_regras(self):
        col = self.rufus.coluna_intencao
        lin = self.rufus.linha_intencao
        if 0 <= col < 28 and 0<= lin <29:
            if self.matriz[lin][col] != 2:
                self.rufus.aceitar_movimento()
                if self.matriz[lin][col] == 1: 
                    self.pontos +=1
                    self.matriz[lin][col] = 0
                
                if self.matriz[lin][col] == 3:
                    exit()


#Classe para o personagem 
class Rufus:
    def __init__(self, tamanho):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = tamanho
        self.vel_x = 0
        self.vel_y = 0
        self.raio = self.tamanho // 2
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        

    #MOVIMENTAÇÃO DO JOGO
    def calcular_regras(self):
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intencao = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

    #Mostrando o personagem
    def pintar(self, tela):
        # Desenhando rufus
        pygame.draw.rect(tela, amarelo, pygame.Rect(self.centro_x, self.centro_y, self.tamanho, self.tamanho)) 

    
    def processar_eventos(self, eventos):
        for e in eventos:    
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = velocidade
                elif e.key == pygame.K_LEFT:
                    self.vel_x = -velocidade
                elif e.key == pygame.K_DOWN:
                    self.vel_y = velocidade
                elif e.key == pygame.K_UP:
                    self.vel_y = -velocidade
                
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0
                elif e.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif e.key == pygame.K_DOWN:
                    self.vel_y = 0
                elif e.key == pygame.K_UP:
                    self.vel_y = 0

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao


if __name__ == "__main__":
    tamanho_padrao = 600// 30
    rufus = Rufus(tamanho_padrao -0.3)
    cenario = Cenario(tamanho_padrao, rufus)

#Laço de repetição para o jogo
    while True:
        # Calcular as regras
        rufus.calcular_regras()
        cenario.calcular_regras()

        # Pintar a tela
        screen.fill(vinho)
        cenario.pintar(screen)
        rufus.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)

        # Captura os eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
               exit()
        rufus.processar_eventos(eventos)