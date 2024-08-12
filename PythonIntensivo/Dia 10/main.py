import pygame
import random
import math
from pygame import mixer

# Inicializar Pygame
pygame.init()

# Creamos la pantalla
pantalla = pygame.display.set_mode((800,600))

# Titulo e icono
pygame.display.set_caption("Attack Aliens")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("espacio.png")

# agregar musica
mixer.music.load("musica_fondo.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# Jugador
img_jugador = pygame.image.load("astronave.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(2)
    enemigo_y_cambio.append(50)

# Variables Bala
balas = []
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False


# Puntuacion

puntuacion = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10

# texto final del juego
fuente_final = pygame.font.Font("freesansbold.ttf", 40)

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO",True,(255,255,255))
    pantalla.blit(mi_fuente_final,(60,200))


# funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntuacion: {puntuacion}",True,(255,255,255))
    pantalla.blit(texto,(x, y))
def jugador(x,y):
    """
    Funcion que declara el jugador
    :param x:
    :param y:
    :return:
    """
    pantalla.blit(img_jugador,(x,y))


def enemigo(x ,y , ene):
    """
    Funcion que declara el enemigo
    :param x:
    :param y:
    :return:
    """
    pantalla.blit(img_enemigo[ene],(x,y))

# funcion disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

# funcion detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 35:
        return True
    else:
        return False

# Loop para contener el juego
se_ejecuta = True
while se_ejecuta:

   # imagen de fondo actualizar
    pantalla.blit(fondo, (0, 0))


    # Evento para cerrar el programa
    for evento in pygame.event.get():
        # evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento para ingresar movimiento
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                jugador_x_cambio = -2.5
            if evento.key == pygame.K_d:
                jugador_x_cambio = 2.5
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a or evento.key == pygame.K_d:
                jugador_x_cambio = 0


    #Modificar ubicacion jugador
    jugador_x += jugador_x_cambio

# Movimiento bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)

    # Modificar ubicacion enemigo
    for e in range(cantidad_enemigos):

        # FIN del juego
        if enemigo_y[e] > 450:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]


        # Limitar los bordes
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 2
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -2
            enemigo_y[e] += enemigo_y_cambio[e]

        # colision
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntuacion += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break

        enemigo(enemigo_x[e], enemigo_y[e], e)

    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736


   # movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio


    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x,texto_y)

    pygame.display.update()



