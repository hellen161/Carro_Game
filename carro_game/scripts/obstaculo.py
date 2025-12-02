import pygame
import random

class Obstaculo:
    def __init__(self, tela):
        self.tela = tela
        self.largura = random.randint(40, 80)  # Largura variável
        self.altura = random.randint(40, 80)   # Altura variável
        
        # Carrega imagem ou cria uma
        try:
            self.imagem = pygame.image.load('assets/obstaculo.png').convert_alpha()
        except:
            # Cria um obstáculo colorido
            self.imagem = pygame.Surface((self.largura, self.altura))
            cor = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)])
            self.imagem.fill(cor)
        
        self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))
        
        # Posição inicial: começa à direita da tela
        self.x = tela.get_width() + random.randint(0, 200)
        
        # Posição Y aleatória em qualquer lugar da tela - AGORA TAMBÉM VERTICAL
        self.y = random.randint(0, tela.get_height() - self.altura)
        
        self.velocidade = random.randint(4, 8)  # Velocidade variada
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def atualizar(self):
        # Move da DIREITA para a ESQUERDA
        self.x -= self.velocidade
        self.rect.topleft = (self.x, self.y)
        
        # Se sair da tela, reposiciona
        if self.x < -self.largura:
            self.reset()

    def desenhar(self):
        self.tela.blit(self.imagem, (self.x, self.y))

    def reset(self):
        # Reposiciona à direita da tela
        self.x = self.tela.get_width() + random.randint(50, 200)
        
        # NOVO: Tamanho aleatório
        self.largura = random.randint(40, 80)
        self.altura = random.randint(40, 80)
        
        # NOVO: Posição Y aleatória (agora pode estar em qualquer altura)
        self.y = random.randint(0, self.tela.get_height() - self.altura)
        
        # Recria imagem
        if isinstance(self.imagem, pygame.Surface):
            self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))
        
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.velocidade = random.randint(4, 8)

    def detectar_colisao(self, rect_jogador):
        return self.rect.colliderect(rect_jogador)