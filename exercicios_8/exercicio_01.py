import pygame
import random

# Inicializar o pygame
pygame.init()

# Configuração da janela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Quadrado Quicante 🎮")

clock = pygame.time.Clock()
FPS = 60

def mudar_cor():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

# Tamanho do retângulo
LARGURA_RET = 25
ALTURA_RET = 25

# Posição inicial
posicao_x = LARGURA // 2
posicao_y = ALTURA // 2

# Velocidade
vel_x = 5
vel_y = 5

# Cor inicial
cor_retangulo = mudar_cor()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento
    posicao_x += vel_x
    posicao_y += vel_y

    # Colisão horizontal
    if posicao_x + LARGURA_RET >= LARGURA or posicao_x <= 0:
        vel_x *= -1
        cor_retangulo = mudar_cor()

    # Colisão vertical
    if posicao_y + ALTURA_RET >= ALTURA or posicao_y <= 0:
        vel_y *= -1
        cor_retangulo = mudar_cor()

    # Limpa a tela
    tela.fill((0, 0, 0))

    # Desenha o retângulo
    pygame.draw.rect(
        tela,
        cor_retangulo,
        (posicao_x, posicao_y, LARGURA_RET, ALTURA_RET)
    )

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()






