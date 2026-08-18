import random

import pygame

from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            splinter_angle = random.uniform(20,50)
            splinter_radius = self.radius - ASTEROID_MIN_RADIUS
            
            splinter_1 = Asteroid(self.position.x, self.position.y, splinter_radius)
            splinter_2 = Asteroid(self.position.x, self.position.y, splinter_radius)
                        
            splinter_1_vector = self.velocity.rotate(splinter_angle)
            splinter_2_vector = self.velocity.rotate(-splinter_angle)
            
            splinter_1.velocity = splinter_1_vector * 1.2
            splinter_2.velocity = splinter_2_vector * 1.2

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    
    def update(self, dt):
        self.position += self.velocity * dt