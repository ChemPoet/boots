import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # FPS tracked using float value
    dt = 0.0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # You can iterate over objects in a group
        
    Player.containers = (updatable, drawable)
    # Player is the name of the class, not an instance of it
    # All future instances of Player are in the Groups (updatable) and (drawable)
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
