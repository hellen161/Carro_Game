import pygame

class Texto:
    def __init__(self, tela, texto, x, y, cor, tamanho=36):
        self.tela = tela
        self.texto = texto
        self.pos = (x, y)
        self.cor = cor
        self.fonte = pygame.font.SysFont('Arial', tamanho, bold=True)
        self.atualizar_texto(texto)

    def desenhar(self):
        self.tela.blit(self.superficie, self.pos)

    def atualizar_texto(self, novo_texto):
        self.texto = novo_texto
        self.superficie = self.fonte.render(novo_texto, True, self.cor)

class Botao:
    def __init__(self, tela, texto, x, y, largura, altura, cor_fundo, cor_texto):
        self.tela = tela
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor_fundo = cor_fundo
        self.texto_obj = Texto(tela, texto, x + largura//2, y + altura//2, cor_texto, 30)
        
        # Centraliza texto
        texto_largura = self.texto_obj.superficie.get_width()
        self.texto_obj.pos = (x + (largura - texto_largura)//2, y + 15)

    def desenhar(self):
        pygame.draw.rect(self.tela, self.cor_fundo, self.rect, border_radius=10)
        pygame.draw.rect(self.tela, (255, 255, 255), self.rect, 3, border_radius=10)
        self.texto_obj.desenhar()

    def clique(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            # Feedback visual ao passar mouse
            pygame.draw.rect(self.tela, (100, 255, 100), self.rect, border_radius=10)
            
            if pygame.mouse.get_pressed()[0]:
                pygame.time.delay(150)  # Pequeno delay para feedback
                return True
        return False