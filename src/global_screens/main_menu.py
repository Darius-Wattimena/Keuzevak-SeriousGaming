from src.helper.button import Button
from src.helper.screen_base import ScreenBase
from src.helper.label import Label
import pygame as py


class MainMenu(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.mouse_position = None
        game.drawer.add_background_image("resources/graphics/main_menu_background.jpg")
        self.title = Label(game.py_screen, self.game.config.title, [0, 0, 0], 75, "resources/fonts/Fira.ttf")
        self.btn = []
        btn_base_color = [50, 50, 50]
        self.btn.append(MainMenuButton(game.py_screen, "Nieuw spel", [10, 200, 0], [10, 200, 0], [255, 255, 255], [200, 200, 200]))
        self.btn.append(MainMenuButton(game.py_screen, "Laad spel", btn_base_color, btn_base_color, [255, 255, 255], [200, 200, 200]))
        self.btn.append(MainMenuButton(game.py_screen, "Stoppen", btn_base_color, btn_base_color, [255, 255, 255], [200, 200, 200]))

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position

    def handle_mouse_input(self, event):
        pass

    def on_render(self):
        self.game.drawer.draw_canvas()
        screen_center_width = self.game.py_screen.get_width() / 2
        title_x = screen_center_width - (self.title.get_width() / 2)
        button_x = screen_center_width - (self.btn[0].width / 2)

        self.title.render(title_x, 80)
        self.btn[0].render(self.mouse_position, button_x, 180)
        self.btn[1].render(self.mouse_position, button_x, 260)
        self.btn[2].render(self.mouse_position, button_x, 600)
        py.display.update()

    def handle_key_input(self, keys):
        return

    def on_events(self, events):
        for event in events:
            if event.type == py.MOUSEBUTTONDOWN:
                if self.btn[0].is_clicked(self.mouse_position):
                    self.show_pick_minigame()
                elif self.btn[1].is_clicked(self.mouse_position):
                    self.show_options()
                elif self.btn[2].is_clicked(self.mouse_position):
                    self.game.quit()

    def on_update(self):
        pass

    def show_pick_minigame(self):
        return

    def show_options(self):
        return


class MainMenuButton(Button):
    def __init__(self, screen, text, button_color, button_color_hover, text_color, text_color_hover):
        text_size = 45
        button_width = 350
        button_height = 70
        super().__init__(screen, text, button_color, button_color_hover, text_color, text_color_hover, text_size,
                         button_width, button_height)
