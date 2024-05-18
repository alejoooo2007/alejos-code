import pygame
import sys

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego del cuadrado asesino")


background_color = (0, 0, 0)


square_size = 50
x = width // 2 - square_size // 2
y = height // 2 - square_size // 2


speed = 5


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed  
    if keys[pygame.K_DOWN]:
        y += speed  
    if keys[pygame.K_LEFT]:
        x -= speed  
    if keys[pygame.K_RIGHT]:
        x += speed  
    
    
    if x < 0:  
        x = 0
    elif x + square_size > width:  
        x = width - square_size
    if y < 0:  
        y = 0
    elif y + square_size > height:  #Parte investigada: verifica si el cuadrado se extiende más allá del borde derecho de la ventana. Si es así, ajusta la posición x para que el cuadrado quede completamente dentro de la ventana. Esto se hace restando el tamaño del cuadrado a la anchura de la ventana.
        y = height - square_size
    
   
    screen.fill(background_color)
    pygame.draw.rect(screen, (255, 0, 0), (x, y, square_size, square_size))

  
    pygame.display.flip()

                                                                                      
    pygame.time.Clock().tick(60)


pygame.quit()
sys.exit()
