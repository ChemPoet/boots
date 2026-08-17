import pygame

from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # FPS tracked using float value
    dt = 0.0
    ship = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    

    # Game Loop
    while True:
        log_state()
    
        for event in pygame.event.get():
            pass
            
        screen.fill("black")
        ship.draw(screen)
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
