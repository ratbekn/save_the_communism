import pygame
from UI.ui_object import UIObject


class Button(UIObject):
    def __init__(self, x, y, width, height, color, text, event_handler, font_color = pygame.Color('white')):
        super().__init__(x, y, width, height)
        self.__click_handlers = []
        self.font_color = font_color
        self.font = pygame.font.SysFont('Verdana', 14)
        self.standard_color = color
        self.color = color
        self.text = text
        self.__event_handler = event_handler
        self.pressed = False

    def draw(self, surface):
        # pygame.draw.rect(surface, self.color, pygame.Rect(self.left, self.top, self.width, self.height))
        text_surface = self.font.render(self.text, True, self.font_color)
        surface.blit(text_surface, (self.centerX - self.font.size(self.text)[0]//2, self.centerY - self.font.size(self.text)[1]//2))

    def __highlight_color(self, color):
        new_color = []
        for component in color[0:2]:
            if component + 20 <= 255:
                new_color.append(component + 20)
            else:
                new_color.append(component)
        if color[2] - 20 >= 0:
            new_color.append(color[2] - 20)
        else:
            new_color.append(color[2])
        new_color.append(color[2])
        return new_color

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.bounds.collidepoint(*mouse_pos):
            if not self.pressed:
                self.color = self.__highlight_color(self.color)
            if self.__event_handler.last_event.type == pygame.MOUSEBUTTONDOWN:
                self.pressed = True
                self.color = pygame.Color('white')
            if self.__event_handler.last_event.type == pygame.MOUSEBUTTONUP:
                self.__on_click()
                self.pressed = False
                self.color = pygame.Color('yellow')
        else:
            self.color = self.standard_color

    def __on_click(self):
        for handler in self.__click_handlers:
            if len(handler[1]) == 0:
                handler[0]()
            else:
                handler[0](*handler[1])

    def add_click_handler(self, handler, *args):
        self.__click_handlers.append((handler, args))
