# Setup Python ----------------------------------------------- #
import pygame
from  random import randint

 
# Setup pygame/window ---------------------------------------- #
Clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Particles.py')
screen = pygame.display.set_mode((500, 500),0,32)
 

# a particle is...
# a thing that exists at a location
# typically moves around
# typically changes over time
# and typically disappears after a certain amount of time
 
# [loc, velocity, timer]
particles = []
 
# Loop ------------------------------------------------------- #
while True:
   
    # Background --------------------------------------------- #
    screen.fill((0,0,0))
    # Taking Mouse position
    mx, my = pygame.mouse.get_pos()
    particles.append([[mx, my], [randint(0, 20) / 10 - 1, -2], randint( 8,10)])
 
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.1
        # Drawing Circles (Particles)
        pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))  
        if particle[2] <= 0:
            particles.remove(particle)
   
    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
               
    # Update ------------------------------------------------- #
    pygame.display.update()
    Clock.tick(60)