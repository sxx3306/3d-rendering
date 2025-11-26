import pygame
import math
from config import Config


class Game:
    pygame.init()

    def __init__(self):
        self.config = Config()
        self.dims = [[-2, 2, 2], [2, 2, 2], [-2, -2, 2], [2, -2, 2], [-2, 2, -2], [2, 2, -2], [-2, -2, -2], [2, -2, -2]]
        self.camera = [0, 0, -5]
        self.dist = 100
        self.screen = pygame.display.set_mode((1000, 500))
    
    def project(self, dim):

        x = dim[0] - self.camera[0]
        y = dim[1] - self.camera[1]
        z = dim[2] - self.camera[2]

        if z <= 0:
            return None

        xp = (self.dist * x) / z
        yp = (self.dist * y) / z
        new_x = (self.screen.get_width() / 2) + xp
        new_y = (self.screen.get_height() / 2) + yp
        return new_x, new_y

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill('black')

            keys = pygame.key.get_pressed()
            
            for dim in self.dims:
                new_x, new_y = self.project(dim)
                pygame.draw.circle(self.screen, "white", pygame.Vector2(new_x, new_y), 5)
                

            pygame.display.flip()

            dt = clock.tick(60)

        pygame.quit()

game = Game()
game.run()