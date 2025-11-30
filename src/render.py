import pygame
import math
from config import Config


class Game:
    pygame.init()

    def __init__(self):
        self.config = Config()
        self.dims = [
            [-2,  2,  2],
            [ 2,  2,  2],
            [ 2, -2,  2],
            [-2, -2,  2],
            [-2,  2, -2],
            [ 2,  2, -2],
            [ 2, -2, -2],
            [-2, -2, -2]
        ]

        self.edges = [
            (0,1), (1,2), (2,3), (3,0),
            (4,5), (5,6), (6,7), (7,4),
            (0,4), (1,5), (2,6), (3,7)
        ]

        self.camera = [0, 0, -4]
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
    
    def rotate_x(self, dim, angle):
        angle = math.radians(angle)
        new_x = dim[0]
        new_y = dim[1] * math.cos(angle) - dim[2] * math.sin(angle)
        new_z = dim[1] * math.sin(angle) + dim[2] * math.cos(angle) 
        return [new_x, new_y, new_z]
    
    def rotate_y(self, dim, angle):
        angle = math.radians(angle)
        new_x = dim[0] * math.cos(angle) + dim[2] * math.sin(angle)
        new_y = dim[1]
        new_z = -dim[0] * math.sin(angle) + dim[2] * math.cos(angle) 
        return [new_x, new_y, new_z]
    
    def rotate_z(self, dim, angle):
        angle = math.radians(angle)
        new_x = dim[0] * math.cos(angle) - dim[1] * math.sin(angle)
        new_y = dim[0] * math.sin(angle) + dim[1] * math.cos(angle)
        new_z = dim[2]
        return [new_x, new_y, new_z]
    
    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill('black')

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                for i in range(len(self.dims)):
                    dim = self.dims[i]
                    dim = self.rotate_x(dim, 1)
                    self.dims[i] = dim
            elif keys[pygame.K_s]:
                for i in range(len(self.dims)):
                    dim = self.dims[i]
                    dim = self.rotate_x(dim, -1)
                    self.dims[i] = dim
            elif keys[pygame.K_d]:
                for i in range(len(self.dims)):
                    dim = self.dims[i]
                    dim = self.rotate_y(dim, 1)
                    self.dims[i] = dim
            elif keys[pygame.K_a]:
                for i in range(len(self.dims)):
                    dim = self.dims[i]
                    dim = self.rotate_y(dim, -1)
                    self.dims[i] = dim
            elif keys[pygame.K_e]:
                for i in range(len(self.dims)):
                    dim = self.dims[i]
                    dim = self.rotate_z(dim, 1)
                    self.dims[i] = dim
            elif keys[pygame.K_q]:
                for i in range(len(self.dims)):
                    dim = self.dims[i]
                    dim = self.rotate_z(dim, -1)
                    self.dims[i] = dim



            # dots
            for i in range(len(self.dims)):
                dim = self.dims[i]
                new_x, new_y = self.project(dim)
                pygame.draw.circle(self.screen, "white", pygame.Vector2(new_x, new_y), 5)
            
            # lines
            for i in range(len(self.edges)):
                start_x, start_y = self.project(self.dims[self.edges[i][0]])
                end_x, end_y = self.project(self.dims[self.edges[i][1]])
                pygame.draw.line(self.screen, 'white', pygame.Vector2(start_x, start_y), pygame.Vector2(end_x, end_y), 3)
                
            pygame.display.flip()

            dt = clock.tick(30)

        pygame.quit()

game = Game()
game.run()