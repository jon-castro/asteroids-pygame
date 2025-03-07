import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        screen.fill((0,0,0))
        
        for member in drawable:
            member.draw(screen)
            
        for asteroid in asteroids:
            check = asteroid.detect_collision(player)
            if check:
                print("Game over!")
                sys.exit()
            for bullet in shots:
                shot_check = bullet.detect_collision(asteroid)
                if shot_check:
                    bullet.kill()
                    asteroid.split()
        
        pygame.display.flip()
        
        tick = clock.tick(60)
        dt = tick/1000
    
if __name__ == "__main__":
    main()