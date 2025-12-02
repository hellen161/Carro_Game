import pygame
from scripts.jogador import Jogador
from scripts.obstaculo import Obstaculo
from scripts.interfaces import Texto, Botao

class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, "CARRO GAME", 250, 100, (255, 255, 255), 60)
        self.botao_jogar = Botao(tela, "JOGAR", 300, 300, 200, 60, (0, 200, 0), (255, 255, 255))
        self.estado = "menu"

    def atualizar(self):
        self.titulo.desenhar()
        self.botao_jogar.desenhar()
        
        if self.botao_jogar.clique():
            self.estado = "partida"
        
        return self.estado

class Partida:
    def __init__(self, tela):
        self.tela = tela
        # Posição inicial mais central
        self.jogador = Jogador(tela, tela.get_width() // 2 - 30, tela.get_height() // 2 - 20)
        
        # Cria mais obstáculos para maior desafio
        self.obstaculos = [Obstaculo(tela) for _ in range(5)]  # Aumentei para 5
        
        self.pontos = 0
        self.contador = 0
        self.texto_pontos = Texto(tela, f"Pontos: {self.pontos}", 10, 10, (255, 255, 255))
        self.estado = "partida"
        
        # Texto de instruções
        self.instrucoes = Texto(tela, "Use WASD ou SETAS para mover", 10, 50, (200, 200, 200), 20)

    def atualizar(self):
        # Atualiza jogador (agora com movimento vertical)
        self.jogador.atualizar()
        
        # Atualiza obstáculos
        colidiu = False
        for obs in self.obstaculos:
            obs.atualizar()
            
            # Verifica colisão
            if obs.detectar_colisao(self.jogador.get_rect()):
                colidiu = True
        
        # Se colidiu, volta ao menu
        if colidiu:
            self.estado = "menu"
            return self.estado
        
        # Atualiza pontuação (mais rápida)
        self.contador += 1
        if self.contador >= 30:  # A cada meio segundo
            self.pontos += 1
            self.contador = 0
            self.texto_pontos.atualizar_texto(f"Pontos: {self.pontos}")
        
        # Desenha tudo
        self.jogador.desenhar()
        for obs in self.obstaculos:
            obs.desenhar()
        
        self.texto_pontos.desenhar()
        self.instrucoes.desenhar()
        
        return self.estado