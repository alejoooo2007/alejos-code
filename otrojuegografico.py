import pygame
import sys

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Detective Case Flowchart")

background_image = pygame.image.load("fondo.png")
background_image = pygame.transform.scale(background_image, (width, height)) 
screen.blit(background_image, (0,0))

def create_button(button, image, position, callback):
    button["image.png"] = image
    button["rect"] = image.get_rect(topleft=position)
    button["callback"] = callback
 
def button_on_click(button, event):
    if event.button == 1:
        if button["rect"].collidepoint(event.pos):
            button["callback"](button)
 
def push_button_goodbye(button):
    print("")

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
blue = (0, 0, 200)

font = pygame.font.Font(None, 36)


INICIO = 0
INTERROGA_VICTIMA = 1
REVISA_ESCENA = 2
REVISA_CAMARAS = 3
PISTA_VICTIMA = 4
TRAUMA_VICTIMA = 5
PISTA_ESCENA = 6
NADA_ESCENA = 7
PISTA_CAMARAS = 8
NADA_CAMARAS = 9
SIGUE_PISTA_VICTIMA = 10
INTERROGA_TESTIGO_ESCENA = 11
INVESTIGA_FIGURA_SOSPECHOSA = 12
REVISA_ANTECEDENTES_VICTIMA = 13
BUSCA_MAS_TESTIGOS = 14
ENCUENTRA_SOSPECHOSO = 15
TESTIGO_COARTADA = 16
DESCUBRE_MOTIVO = 17
NADA_RELEVANTE = 18
TESTIGO_ADICIONAL = 19
NO_MAS_TESTIGOS = 20
CONFRONTA_SUSPECHOSO = 21
BUSCA_MAS_PRUEBAS = 22
REVISA_REGISTROS_SOSPECHOSO = 23
CONFESION_SOSPECHOSO = 24
SOSPECHOSO_HUYE = 25
PRUEBAS_ADICIONALES = 26
NO_MAS_PRUEBAS = 27
COARTADA_SOSPECHOSO = 28
CASO_SIN_RESOLVER = 29
FINAL_BUENO = 30
FINAL_MALO = 31
FINAL_NORMAL = 32

state = INICIO

def draw_text(text, position, color=white):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)
def draw_button(text, rect, active=False):
    color = green if active else blue
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, white, rect, 2)
    draw_text(text, (rect[0] + 10, rect[1] + 10))

# Función para manejar eventos de los botones
def handle_buttons(rects, event):
    for rect, state_change in rects.items():
        if rect.collidepoint(event.pos):
            return state_change
    return None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if state == INICIO:
                button_rects = {
                    pygame.Rect(50, 100, 400, 50): INTERROGA_VICTIMA,
                    pygame.Rect(50, 150, 400, 50): REVISA_ESCENA,
                    pygame.Rect(50, 200, 400, 50): REVISA_CAMARAS,
                }
                state = handle_buttons(button_rects, event)
            elif state == INTERROGA_VICTIMA:
                button_rects = {
                    pygame.Rect(50, 100, 400, 50): PISTA_VICTIMA,
                    pygame.Rect(50, 150, 400, 50): TRAUMA_VICTIMA,
                }
                state = handle_buttons(button_rects, event)
            elif state == REVISA_ESCENA:
                button_rects = {
                    pygame.Rect(50, 100, 400, 50): PISTA_ESCENA,
                    pygame.Rect(50, 150, 400, 50): NADA_ESCENA,
                }
                state = handle_buttons(button_rects, event)
            elif state == REVISA_CAMARAS:
                button_rects = {
                    pygame.Rect(50, 100, 400, 50): PISTA_CAMARAS,
                    pygame.Rect(50, 150, 400, 50): NADA_CAMARAS,
                }
                state = handle_buttons(button_rects, event)

        if event.type == pygame.KEYDOWN:
            if state == INICIO:
                if event.key == pygame.K_1:
                    state = INTERROGA_VICTIMA
                elif event.key == pygame.K_2:
                    state = REVISA_ESCENA
                elif event.key == pygame.K_3:
                    state = REVISA_CAMARAS
            elif state == INTERROGA_VICTIMA:
                if event.key == pygame.K_1:
                    state = PISTA_VICTIMA
                elif event.key == pygame.K_2:
                    state = TRAUMA_VICTIMA
            elif state == REVISA_ESCENA:
                if event.key == pygame.K_1:
                    state = PISTA_ESCENA
                elif event.key == pygame.K_2:
                    state = NADA_ESCENA
            elif state == REVISA_CAMARAS:
                if event.key == pygame.K_1:
                    state = PISTA_CAMARAS
                elif event.key == pygame.K_2:
                    state = NADA_CAMARAS
           
    screen.blit(background_image, (0, 0))

    if state == INICIO:
        draw_text("Inicio: El detective recibe el caso", (50, 50))
        draw_button("¿Interroga a la víctima primero?", pygame.Rect(50, 100, 400, 50))
        draw_button("¿Revisa la escena del crimen primero?", pygame.Rect(50, 150, 400, 50))
        draw_button("¿Revisa las cámaras de seguridad primero?", pygame.Rect(50, 200, 400, 50))
    elif state == INTERROGA_VICTIMA:
        draw_text("Interroga a la víctima", (50, 50))
        draw_button("La víctima proporciona una pista crucial", pygame.Rect(50, 100, 400, 50))
        draw_button("La víctima está demasiado traumatizada para hablar", pygame.Rect(50, 150, 400, 50))
    elif state == REVISA_ESCENA:
        draw_text("Revisa la escena del crimen", (50, 50))
        draw_button("Encuentra una pista importante en la escena", pygame.Rect(50, 100, 400, 50))
        draw_button("No encuentra nada relevante en la escena", pygame.Rect(50, 150, 400, 50))
    elif state == REVISA_CAMARAS:
        draw_text("Revisa las cámaras de seguridad", (50, 50))
        draw_button("Las cámaras muestran una figura sospechosa", pygame.Rect(50, 100, 400, 50))
        draw_button("Las cámaras no muestran nada útil", pygame.Rect(50, 150, 400, 50))
    elif state == PISTA_VICTIMA:
        draw_text("La víctima proporciona una pista crucial", (50, 50))
        draw_button("Sigue la pista de la víctima", pygame.Rect(50, 100, 400, 50))
        
    pygame.display.flip()

    if state == FINAL_BUENO:
        print("¡Has resuelto el caso de manera excelente!")
        pygame.quit()
        sys.exit()
    elif state == FINAL_MALO:
        print("El caso no se ha resuelto correctamente. ¡Mejor suerte la próxima vez!")
        pygame.quit()
        sys.exit()
    elif state == FINAL_NORMAL:
        print("Has resuelto el caso, pero podría haber sido mejor. ¡Sigue practicando!")
        pygame.quit()
        sys.exit()
