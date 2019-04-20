import pygame


class EventHandler:
    def __init__(self):
        self.last_event = None
        self.__keys_pressed_queue = set()
        self.key_pressed = None
        self.__event_frames_counter = 0

    def handle_events(self):
        event = pygame.event.poll()
        self.last_event = event
        if event.type == pygame.KEYDOWN:
            self.__event_frames_counter = 60
            self.key_pressed = event.key
            self.__keys_pressed_queue.add(event.key)
        elif event.type == pygame.KEYUP:
            self.__keys_pressed_queue.remove(event.key)
            if not len(self.__keys_pressed_queue) == 0:
                self.key_pressed = min(self.__keys_pressed_queue)
        if len(self.__keys_pressed_queue) == 0:
            if self.__event_frames_counter == 0:
                self.key_pressed = None
            else:
                self.__event_frames_counter -= 1
