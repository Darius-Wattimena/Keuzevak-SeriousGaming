from src.helper.screen_base import ScreenBase
import pygame as py


class HomeScreen(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)

    def on_render(self):
        return

    def on_events(self, events):
        for event in events:
            if event.type == py.MOUSEBUTTONDOWN:
                pass

    def on_update(self):
        pass

    def handle_key_input(self, keys):
        return

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position

    def handle_mouse_input(self, event):
        pass


