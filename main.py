import pygame
import math

angle = 0

#initialising the pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((1920, 1080))

# Title and Icon
pygame.display.set_caption("Solar system")
icon = pygame.image.load('solarsystem.png')
pygame.display.set_icon(icon)

# Planet class
class Planets:

    def __init__(self, planet,radius,size):
        self.planet = planet
        self.radius = radius
        self.size = size


    def draw(self):
        global angle
        global sunX
        global sunY
        theta = math.radians(angle)
        planet_coords = sunX + self.radius * math.cos(theta), sunY + self.radius * math.sin(theta)
        angle += 0.01
        pygame.draw.circle(screen, (173, 173, 174), [sunX + 16, sunY + 16], self.radius, 2)
        screen.blit(self.planet, (planet_coords[0] + self.size, planet_coords[1] + self.size))



# Sun
sun = pygame.image.load("sun.png")
sunX = 944
sunY = 524

def draw_sun():
    screen.blit(sun, (sunX, sunY))

# Mercury
mercury = pygame.image.load("mercury.png")
Mercury = Planets(mercury,100,12)

# Venus
venus = pygame.image.load("venus.png")
Venus = Planets(venus,130,16)

# Earth
earth = pygame.image.load("earth.png")
Earth = Planets(earth,160,16)

# Mars
mars = pygame.image.load("mars.png")
Mars = Planets(mars,200,16)

# Jupiter
jupiter = pygame.image.load("jupiter.png")
Jupiter = Planets(jupiter,300,32)

# Saturn
saturn = pygame.image.load("saturn.png")
Saturn = Planets(saturn,380,16)

# Uranus
uranus = pygame.image.load("uranus.png")
Uranus = Planets(uranus,450,16)

# Neptune
neptune = pygame.image.load("neptune.png")
Neptune = Planets(neptune,550,12)

# Game Loop
running = True
while running:

    # Background Color
    screen.fill((10, 10, 10))

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False

    draw_sun()
    Mercury.draw()
    Venus.draw()
    Earth.draw()
    Mars.draw()
    Jupiter.draw()
    Saturn.draw()
    Uranus.draw()
    Neptune.draw()

    pygame.display.update()
