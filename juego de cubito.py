import pygame
import random

pygame.init()

ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Juego con Pygame")

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

jugador_imagen = pygame.image.load("jugador.png")
objetivo_imagen = pygame.image.load("objetivo.png")
fondo_imagen = pygame.image.load("fondo_galaxia.jpeg")
jugador_imagen = pygame.transform.scale(jugador_imagen, (50, 50))
objetivo_imagen = pygame.transform.scale(objetivo_imagen, (30, 30))
fondo_imagen = pygame.transform.scale(fondo_imagen, (ancho_pantalla, alto_pantalla))

jugador_rect = jugador_imagen.get_rect()
objetivo_rect = objetivo_imagen.get_rect()

jugador_rect.center = (ancho_pantalla // 2, alto_pantalla // 2)

def posicion_aleatoria_objetivo():
    x = random.randint(0, ancho_pantalla - objetivo_rect.width)
    y = random.randint(0, alto_pantalla - objetivo_rect.height)
    return x, y

objetivo_rect.topleft = posicion_aleatoria_objetivo()

puntaje = 0

fuente = pygame.font.Font(None, 36)

class Jugador:
    def __init__(self):
        self.rect = jugador_rect
        self.velocidad = 5
        self.puas = []

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidad

    def disparar(self):
        pua = Pua(self.rect.centerx, self.rect.top)
        self.puas.append(pua)

    def dibujar(self, pantalla):
        pantalla.blit(jugador_imagen, self.rect.topleft)
        for pua in self.puas:
            pua.dibujar(pantalla)

class Pua:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 5, 10)
        self.velocidad = 10

    def mover(self):
        self.rect.y -= self.velocidad

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, BLANCO, self.rect)

jugador = Jugador()

jugando = True
reloj = pygame.time.Clock()

while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jugador.disparar()

    teclas = pygame.key.get_pressed()

    jugador.mover(teclas)

    for pua in jugador.puas:
        pua.mover()
      
        if pua.rect.colliderect(objetivo_rect):
            puntaje += 1
            jugador.puas.remove(pua)
            objetivo_rect.topleft = posicion_aleatoria_objetivo()

    pantalla.blit(fondo_imagen, (0, 0)) 
    jugador.dibujar(pantalla)
    pantalla.blit(objetivo_imagen, objetivo_rect.topleft)

    texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto_puntaje, (10, 10))

    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
