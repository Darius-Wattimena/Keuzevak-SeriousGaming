from src.helper.button import Button
from src.helper.screen_base import ScreenBase
from src.helper.text_input import TextInput
import pygame as py


class StartScreen(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.game.drawer.add_background_image("resources/graphics/KVK_Formulier.png")
        self.next_button = ScreenButton(game.py_screen, "Klaar", [29, 226, 72], [29, 226, 72])
        self.back_button = ScreenButton(game.py_screen, "Terug", [50, 50, 50], [50, 50, 50])
        self.button_x = self.game.screen_center_width - (self.back_button.width / 2)
        text_font = "resources/fonts/helsinki.ttf"
        self.name_input = CustomInputField(game.py_screen, TextInput("Henk", text_font), 440, 400, 325, 40, [225, 225, 225])
        self.company_input = CustomInputField(game.py_screen, TextInput("Het nieuws", text_font), 440, 450, 325, 40, [225, 225, 225])
        self.mouse_position = None

    def on_render(self):
        self.game.drawer.draw_canvas()
        self.next_button.render(self.mouse_position, self.button_x, 560)
        self.back_button.render(self.mouse_position, self.button_x, 640)

        self.name_input.render()
        self.company_input.render()
        py.display.update()

    def on_events(self, events):
        self.name_input.update(events)
        self.company_input.update(events)
        for event in events:
            if event.type == py.MOUSEBUTTONDOWN:
                if self.next_button.is_clicked(self.mouse_position):
                    self.character_create()
                elif self.back_button.is_clicked(self.mouse_position):
                    self.back_to_menu()
                elif self.name_input.is_clicked(self.mouse_position):
                    self.name_input.selected = True
                    self.company_input.selected = False
                elif self.company_input.is_clicked(self.mouse_position):
                    self.company_input.selected = True
                    self.name_input.selected = False

    def on_update(self):
        pass

    def handle_key_input(self, keys):
        return

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position

    def handle_mouse_input(self, event):
        pass

    def back_to_menu(self):
        from src.global_screens.main_menu import MainMenu
        self.game.drawer.clear()
        MainMenu(self.game)

    def character_create(self):
        from src.game_screens.character_create_screen.character_create_screen import CharacterCreateScreen
        self.game.drawer.clear()
        CharacterCreateScreen(self.game)


class ScreenButton(Button):
    def __init__(self, screen, text, button_color, button_color_hover):
        text_color = [255, 255, 255]
        text_color_hover = [200, 200, 200]
        text_size = 40
        button_width = 325
        button_height = 70
        super().__init__(screen, text, button_color, button_color_hover, text_color, text_color_hover, text_size,
                         button_width, button_height)


class CustomInputField:
    def __init__(self, surface, text_input, x, y, width, height, background):
        self.height = height
        self.width = width
        self.background = background
        self.text_input = text_input
        self.x = x
        self.y = y
        self.surface = surface
        self.initialized = False
        self.selected = False
        self.rect = None

    def render(self):
        self.rect = py.draw.rect(self.surface, self.background, [self.x, self.y, self.width, self.height])
        self.surface.blit(self.text_input.get_surface(), (self.x, self.y))

    def update(self, events):
        if not self.initialized or self.selected:
            self.text_input.update(events)
            self.initialized = True

    def is_clicked(self, mouse_position):
        if self.rect is not None:
            return self.rect.collidepoint(mouse_position)
