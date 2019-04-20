import pygame

from game_object import GameObject


class Lives(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y, 0, game)
        self.font = pygame.font.SysFont('Verdana', 20)

    def draw(self):
        text_surface = self.font.render("XP: " + str(self.game.player.xp), True, (255, 255, 0))
        self.game.display.blit(text_surface, (10, 10))
        text_surface = self.font.render("Bullets: " + str(self.game.player.bullets_cnt), True, (255, 255, 0))
        self.game.display.blit(text_surface, (10, 30))
        text_surface = self.font.render("Score: " + str(self.game.player.score), True, (255, 255, 0))
        self.game.display.blit(text_surface, (10, 50))