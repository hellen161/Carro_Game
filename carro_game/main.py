import pygame
from scripts.cenas import Menu, Partida

pygame.init()

tamanho_tela = (800, 600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Carro Game - Mova com WASD ou Setas")
relogio = pygame.time.Clock()
cor_fundo = (30, 30, 40)  # Cor mais escura para contraste

# Cria as cenas
cenas = {
    'menu': Menu(tela),
    'partida': Partida(tela)
}

cena_atual = 'menu'
executando = True

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    
    tela.fill(cor_fundo)
    
    # Atualiza a cena atual
    estado_retornado = cenas[cena_atual].atualizar()
    
    # Se a cena mudar, atualiza
    if estado_retornado != cena_atual:
        if estado_retornado == 'partida':
            # Recria a partida do zero
            cenas['partida'] = Partida(tela)
        cena_atual = estado_retornado
    
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()