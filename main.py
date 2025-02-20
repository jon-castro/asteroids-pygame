import pygame

from constants import *
from player import Player


def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        screen.fill((0,0,0))
        
        for member in drawable:
            member.draw(screen)
        
        pygame.display.flip()
        
        tick = clock.tick(60)
        dt = tick/1000
    
if __name__ == "__main__":
    main()