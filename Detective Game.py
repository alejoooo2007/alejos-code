import pygame
import sys

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Detective Case Flowchart")


MENU = -1
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
CONFRONTA_SOSPECHOSO = 21
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


background_images = {
    MENU: pygame.transform.scale(pygame.image.load("fondo_menu.png"), (width, height)),
    INICIO: pygame.transform.scale(pygame.image.load("fondo_inicio.png"), (width, height)),
    INTERROGA_VICTIMA: pygame.transform.scale(pygame.image.load("fondo_interroga_victima.png"), (width, height)),
    REVISA_ESCENA: pygame.transform.scale(pygame.image.load("fondo_revisa_escena.png"), (width, height)),
    REVISA_CAMARAS: pygame.transform.scale(pygame.image.load("fondo_revisa_camaras.png"), (width, height)),
    PISTA_VICTIMA: pygame.transform.scale(pygame.image.load("fondo_pista_victima.png"), (width, height)),
    TRAUMA_VICTIMA: pygame.transform.scale(pygame.image.load("fondo_trauma_victima.png"), (width, height)),
    PISTA_ESCENA: pygame.transform.scale(pygame.image.load("fondo_pista_escena.png"), (width, height)),
    NADA_ESCENA: pygame.transform.scale(pygame.image.load("fondo_nada_escena.png"), (width, height)),
    PISTA_CAMARAS: pygame.transform.scale(pygame.image.load("fondo_pista_camaras.png"), (width, height)),
    NADA_CAMARAS: pygame.transform.scale(pygame.image.load("fondo_nada_camaras.png"), (width, height)),
    FINAL_BUENO: pygame.transform.scale(pygame.image.load("fondo_final_bueno.png"), (width, height)),
    FINAL_MALO: pygame.transform.scale(pygame.image.load("fondo_final_malo.png"), (width, height)),
    FINAL_NORMAL: pygame.transform.scale(pygame.image.load("fondo_final_normal.png"), (width, height))
}

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
blue = (0, 0, 200)

font = pygame.font.Font(None, 36)

state = MENU

questions = {
    MENU: {
        "text": "Menu Principal",
        "options": [("1. Jugar", INICIO), ("2. Salir", None)]
    },
    INICIO: {
        "text": "Inicio: El detective recibe el caso",
        "options": [
            ("1. Interroga a la víctima primero", INTERROGA_VICTIMA),
            ("2. Revisa la escena del crimen primero", REVISA_ESCENA),
            ("3. Revisa las cámaras de seguridad primero", REVISA_CAMARAS)
        ]
    },
    INTERROGA_VICTIMA: {
        "text": "Interroga a la víctima",
        "options": [
            ("1. La víctima proporciona una pista crucial", PISTA_VICTIMA),
            ("2. La víctima está demasiado traumatizada para hablar", TRAUMA_VICTIMA)
        ]
    },
    REVISA_ESCENA: {
        "text": "Revisa la escena del crimen",
        "options": [
            ("1. Encuentra una pista importante en la escena", PISTA_ESCENA),
            ("2. No encuentra nada relevante en la escena", NADA_ESCENA)
        ]
    },
    REVISA_CAMARAS: {
        "text": "Revisa las cámaras de seguridad",
        "options": [
            ("1. Las cámaras muestran una figura sospechosa", PISTA_CAMARAS),
            ("2. Las cámaras no muestran nada útil", NADA_CAMARAS)
        ]
    },
    PISTA_VICTIMA: {
        "text": "La víctima proporciona una pista crucial",
        "options": [("1. Sigue la pista de la víctima", FINAL_BUENO)]
    },
    TRAUMA_VICTIMA: {
        "text": "La víctima está demasiado traumatizada para hablar",
        "options": [("1. Fin del juego", FINAL_MALO)]
    },
    PISTA_ESCENA: {
        "text": "Encuentra una pista importante en la escena",
        "options": [("1. Fin del juego", FINAL_NORMAL)]
    },
    NADA_ESCENA: {
        "text": "No encuentra nada relevante en la escena",
        "options": [("1. Fin del juego", FINAL_MALO)]
    },
    PISTA_CAMARAS: {
        "text": "Las cámaras muestran una figura sospechosa",
        "options": [("1. Fin del juego", FINAL_NORMAL)]
    },
    NADA_CAMARAS: {
        "text": "Las cámaras no muestran nada útil",
        "options": [("1. Fin del juego", FINAL_MALO)]
    }
}

def draw_text(text, position, color=white, size=36):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def draw_button(text, rect, active=False):
    color = green if active else blue
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, white, rect, 2)
    draw_text(text, (rect[0] + 10, rect[1] + 10))

def handle_input(key):
    global state
    if state in questions:
        options = questions[state]["options"]
        if key == pygame.K_1 and len(options) > 0:
            state = options[0][1]
        elif key == pygame.K_2 and len(options) > 1:
            state = options[1][1]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            handle_input(event.key)

    
    if state in background_images:
        screen.blit(background_images[state], (0, 0))
    else:
        
        screen.blit(background_images[FINAL_MALO], (0, 0))

    if state in questions:
        question = questions[state]
        draw_text(question["text"], (50, 50), size=50)
        for idx, (text, _) in enumerate(question["options"]):
            draw_button(text, pygame.Rect(50, 150 + idx * 100, 700, 50))
    else:
        draw_text("Fin del juego", (300, 250), size=50)
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
