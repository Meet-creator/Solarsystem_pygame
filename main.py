import pygame
from math import *

#initialising the pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Solar system")
icon = pygame.image.load('solarsystem.png')
pygame.display.set_icon(icon)

# Sun
sun = pygame.image.load("sun.png")
sunX = 384 
sunY = 284

def draw_sun():
    screen.blit(sun, (sunX, sunY))

# Mercury
mercury = pygame.image.load("mercury.png")
mercuryX = 392 
mercuryY = 400
mercury_radius = 1

def draw_mercury():
    screen.blit(mercury, (mercuryX, mercuryY))


# Game Loop
running = True
while running:  
    
    # Background Color
    screen.fill((10, 10, 10))

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False

    draw_sun()
    draw_mercury()

    pygame.display.update()

# Planet class
class planets:
    
    
    def __init__(self, planet, planetX, planetY, radius):
        self.planet = planet
        self.planetX = planetX
        self.planetY = planetY
        self.radius = radius

          
    def draw():
        angle = 0
        theta = math.radians(angle)
        planet_coords = planetX + radius * math.cos(theta), planetY + radius * math.sin(theta)
        angle += 1
         

"""
angle = 0

# [...]

while True:
    # [...]

    center = image_earth_rect.center
    Satellite_pos = [center[0] + radius * cos(angle), center[1] + radius * sin(angle)]
    angle += 0.01

    # [...]"""