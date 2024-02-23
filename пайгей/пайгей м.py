import pygame
pygame.init()

#pygame.FULLSCREEN , DOUBLEBUF двойная буфферизация, HWSURFACE, OPENGL,
#RESIZABLE, NOFRAME, SCALED


sc = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
pygame.display.set_caption("Egor pidor")
pygame.display.set_icon(pygame.image.load("madison.bmp"))

pygame.draw.rect(sc, (255,255,255), (10, 10, 250, 250))
pygame.draw.circle(sc, (200,100,200), (300, 200), 40)
pygame.display.update()

clock = pygame.time.Clock()
FPS = 60

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False

    #pygame.time.delay(17) #задержка на 17 мс = 60 фпс
    clock.tick(FPS) # дает 60 фпс