import pygame

class Jogador:
    def __init__(self, tela, x, y):
        self.tela = tela
        self.posicao = [x, y]
        self.tamanho = (60, 40)
        
        # Carrega a imagem
        try:
            self.imagem = pygame.image.load('assets/carro.png').convert_alpha()
        except:
            # Cria um retângulo vermelho se a imagem não existir
            self.imagem = pygame.Surface(self.tamanho)
            self.imagem.fill((255, 0, 0))
        
        self.imagem = pygame.transform.scale(self.imagem, self.tamanho)
        self.rect = pygame.Rect(self.posicao, self.tamanho)
        self.velocidade = 8  # Velocidade base

    def atualizar(self):
        teclas = pygame.key.get_pressed()
        
        # MOVIMENTO HORIZONTAL
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.posicao[0] -= self.velocidade
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.posicao[0] += self.velocidade
        
        # MOVIMENTO VERTICAL - ADICIONADO!
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.posicao[1] -= self.velocidade
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.posicao[1] += self.velocidade
        
        # Limita dentro da tela HORIZONTALMENTE
        self.posicao[0] = max(0, min(self.posicao[0], self.tela.get_width() - self.tamanho[0]))
        
        # Limita dentro da tela VERTICALMENTE - ADICIONADO!
        self.posicao[1] = max(0, min(self.posicao[1], self.tela.get_height() - self.tamanho[1]))
        
        self.rect.topleft = self.posicao

    def desenhar(self):
        self.tela.blit(self.imagem, self.posicao)

    def get_rect(self):
        return self.rect
    
    def reset(self):
        self.posicao = [100, 300]
        self.rect.topleft = self.posicao