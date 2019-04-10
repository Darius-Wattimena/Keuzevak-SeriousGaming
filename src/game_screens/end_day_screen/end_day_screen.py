from src.helper.screen_base import ScreenBase
import pygame as py
from src.helper.label import Label


class EndDayScreen(ScreenBase):

    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.game.drawer.add_background_image("resources/graphics/computer/Home_Computer.png")

        self.game.money += self.game.dingengoed * 1000

        self.game.dingengoed = 0

        text_font = "resources/fonts/helsinki.ttf"

        self.headline_text = Label(game.py_screen, "€" + str(self.game.money), [0, 0, 0], 32, text_font)


        self.mouse_position = None


    def on_render(self):
        self.game.drawer.draw_canvas()

        self.headline_text.render(800, 70)

        py.display.update()

    def on_events(self, events):
        for event in events:
            if event.type == py.MOUSEBUTTONDOWN:
                from src.game_screens.news_screen.news_screen import NewsScreen
                self.game.drawer.clear()
                NewsScreen(self.game)

    def on_update(self):
        pass

    def handle_key_input(self, keys):
        return

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position

    def handle_mouse_input(self, event):
        pass


