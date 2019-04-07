from src.helper.button import Button
from src.helper.screen_base import ScreenBase
import pygame as py


class MainMenu(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.mouse_position = None
        game.drawer.add_background_image("resources/graphics/StartScherm_Background.png")

        self.logo_x = self.game.screen_center_width - (325 / 2)
        self.logo = game.drawer.add_image("resources/graphics/Kliknieuws_Logo.png", self.logo_x, 80, 325, 199)
        self.btn = []
        btn_base_color = [50, 50, 50]
        self.btn.append(MainMenuButton(game.py_screen, "Nieuw spel", [29, 226, 72], [29, 226, 72], [255, 255, 255], [200, 200, 200]))
        self.btn.append(MainMenuButton(game.py_screen, "Laad spel", btn_base_color, btn_base_color, [255, 255, 255], [200, 200, 200]))
        self.btn.append(MainMenuButton(game.py_screen, "Stoppen", btn_base_color, btn_base_color, [255, 255, 255], [200, 200, 200]))
        self.button_x = self.game.screen_center_width - (self.btn[0].width / 2)

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position

    def handle_mouse_input(self, event):
        pass

    def on_render(self):
        self.game.drawer.draw_canvas()

        self.btn[0].render(self.mouse_position, self.button_x, 300)
        self.btn[1].render(self.mouse_position, self.button_x, 380)
        self.btn[2].render(self.mouse_position, self.button_x, 560)
        py.display.update()

    def handle_key_input(self, keys):
        return

    def on_events(self, events):
        for event in events:
            if event.type == py.MOUSEBUTTONDOWN:
                if self.btn[0].is_clicked(self.mouse_position):
                    self.start_new_game()
                elif self.btn[1].is_clicked(self.mouse_position):
                    self.load_save()
                elif self.btn[2].is_clicked(self.mouse_position):
                    self.game.quit()

    def on_update(self):
        pass

    def start_new_game(self):
        from src.game_screens.start_screen.start_screen import StartScreen
        self.game.drawer.clear()
        StartScreen(self.game)

    def load_save(self):
        return


class MainMenuButton(Button):
    def __init__(self, screen, text, button_color, button_color_hover, text_color, text_color_hover):
        text_size = 40
        button_width = 325
        button_height = 70
        super().__init__(screen, text, button_color, button_color_hover, text_color, text_color_hover, text_size,
                         button_width, button_height)
