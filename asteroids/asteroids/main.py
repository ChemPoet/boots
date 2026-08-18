import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    #SETUP
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # FPS tracked using float value
    dt = 0.0

    #GROUPS    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # You can iterate over objects in a group
    
    #CONTAINERS
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    # Player is the name of the class, not an instance of it
    # All future instances of Player are in the Groups (updatable) and (drawable)
    
    #OBJECTS
    board = AsteroidField()
    ship = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # Game Loop
    while True:
        log_state()
    
        for event in pygame.event.get():
            pass
        
        for obj in updatable:
            obj.update(dt)
        # You may call the .update() method for every member of a group by calling it on the group itself
        
        # ship.update(dt)
        # Update player movement before rendering
        
        for obj in asteroids:
            if obj.collides_with(ship):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for obj in asteroids:
            for bullet in shots:
                if bullet.collides_with(obj):
                    log_event("asteroid_shot")
                    bullet.kill()
                    obj.split()
        
        screen.fill("black")
        for fig in drawable:
            fig.draw(screen)
        # Call the .draw() method for every member of the (drawable) group by calling it on the group itself
                
        # ship.draw(screen)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000
        # Test FPS throttle using temporaty print statement.
        # print(dt)
    
    
# Ensures main() is only called when file run directly - not when imported
if __name__ == "__main__":
    main()
