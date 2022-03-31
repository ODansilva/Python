import re
from unittest import result
import pygame
import sys, random, os
from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

def botoes():
    pygame.draw.circle(bkgd1, amarelo, (285, 640), (r + 14), 5) and pygame.draw.circle(bkgd1, vermelho, (285, 640),
                                                                                       r + 10, 0) \
    and pygame.draw.circle(bkgd1, amarelo, (335, 640), (r + 14), 5) and pygame.draw.circle(bkgd1, azul, (335, 640),
                                                                                           r + 10, 0) \
    and pygame.draw.circle(bkgd1, amarelo, (385, 640), (r + 14), 5) and pygame.draw.circle(bkgd1, verde, (385, 640),
                                                                                           r + 10, 0) \
    and pygame.draw.circle(bkgd1, amarelo, (435, 640), (r + 14), 5) and pygame.draw.circle(bkgd1, laranja, (435, 640),
                                                                                           r + 10, 0)

para = False
roda = True
y = 0
vg = 7

# nao sei o que eu fiz com o 'n' aparentemnte é o contador universal
n = 0

r = 10
velocidade = 5

# Possição inicial das notas
oy = 300
acordes = 0
pontos = 0

# Teclas de Entrada
kays = [pygame.K_q,pygame.K_w,pygame.K_e,pygame.K_r]

# Cores
amarelo = (255, 165, 0)
azul = (30,144,255)
verde = (50,205,50)
vermelho = (205, 0, 0)
laranja = (255, 69, 0)
preto = (0, 0, 0)
branco = (255,255,255)

# Definir Tela
l, a = 720, 640
meiox, meioy = a / 2, l / 2
tela = pygame.display.set_mode((l, a))
fps = 60

# Player de Musica
pygame.mixer.init()
pygame.mixer.music.load('Rocksaveit/acdc-hth.mp3')
pygame.mixer.music.play()

relogio = pygame.time.Clock()

# Definido as Imagen do Projeto
bkgd1 = pygame.image.load('Rocksaveit/bk1.png')
bkgd2 = pygame.image.load('Rocksaveit/p1.png')
tpot = pygame.image.load("Rocksaveit/notas.png")

pygame.display.set_caption('RockSaveit')

while not para:
    # Braço Esteira da Guittara
    ret_y = y % bkgd2.get_rect().width
    tela.blit(bkgd2, (0, ret_y - bkgd2.get_rect().width))
    if ret_y < a:
        tela.blit(bkgd2, (0, ret_y))
    # Randomização das Notas
    corda = random.randint(1, 4)
    if n == 0:
        if acordes == 0:
            if corda == 1:
                ox = 285
                cor = vermelho
                ox1 = 435
                cor1 = laranja
                n = 1
            if corda == 2:
                ox = 335
                cor = azul
                ox1 = 285
                cor1 = vermelho
                n = 1
            if corda == 3:
                ox = 385
                cor = verde
                ox1 = 285
                cor1 = vermelho
                n = 1
            if corda == 4:
                ox = 435
                cor = laranja
                ox1 = 335
                cor1 = azul
                n = 1
    # Imagem de Fundo
    if roda:
        tela.blit(bkgd1, (0, 0))
        # Velocidade das notas
        oy += velocidade
    # Geração de notas
    nota = pygame.draw.circle(tela, amarelo, (ox, oy), 15, 5) and pygame.draw.circle(tela, cor, (ox, oy), 10, 0) and pygame.draw.circle(tela, amarelo, (ox1, oy), 15, 5) and pygame.draw.circle(tela, cor1, (ox1, oy), 10, 0)
    
    # Evento de saida e colizões
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYUP and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

        def teclas(tecla):
            for tecla in kays:
                match tecla:
                    case pygame.K_q:
                        acerto = nota.collidepoint(285, 630) or nota.collidepoint(285, 635)
                    case pygame.K_w:
                        acerto = nota.collidepoint(285, 630) or nota.collidepoint(285, 635)
                    case pygame.K_e:
                        acerto = nota.collidepoint(285, 630) or nota.collidepoint(285, 635)
                    case pygame.K_r:
                        acerto = nota.collidepoint(285, 630) or nota.collidepoint(285, 635)
                return acerto

                '''
                # forma de testa as teclas arterior caso de algo errado
                if tecla == pygame.K_1:
                    acerto = nota.collidepoint(285, 630) or nota.collidepoint(285, 635)
                    if acerto:
                        n = 0
                        pontos += 1
                    else:
                        n = 1
                '''
        pontos = int(pontos)

        if event.type == pygame.KEYDOWN:
            tecla = event.key
            acertos = (teclas(tecla))
            if acertos:
                pontos += 1

        if pontos <= 5:
            velocidade += 1
            vg = 10
        else:
            velocidade += 1
            vg = 15
        if oy >= 640:
            oy = 300
            n = 0
            
    # Pontuaçao na Tela
    tela.blit(tpot, (0, 0))
    pontos = str(pontos)
    pygame.font.init()
    fonte = pygame.font.Font("Rocksaveit/RockShowWhiplash.ttf", 15)
    pontuacao = fonte.render("PONTUAÇÂO", True, branco)
    texpontos = fonte.render(pontos, True, branco)
    tela.blit(pontuacao, (320, 252))
    tela.blit(texpontos, (355, 273))

    # Iniciando o Game
    pygame.display.flip()
    botoes()
    y += vg
    relogio.tick(fps)
    pygame.display.update()
