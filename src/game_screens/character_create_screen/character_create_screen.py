from src.helper.screen_base import ScreenBase
from src.helper.button import Button
from src.helper.image_button import ImageButton
from src.game_config import GameConfig
from src.game_state import GameState
import pygame as py


class CharacterCreateScreen(ScreenBase):

    hair_global = "resources/graphics/char/female_hairstyles/Female_Haircut_3.png"
    color_global = "resources/graphics/char/female_character/Female_Pale.png"
    clothes_global = "resources/graphics/char/female_clothes/Female_Clothes_3.png"
    doorgaan = False


    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)

        # positie grote charater
        self.position_x = 0
        self.position_y = 15

        self.next_button = ScreenButton(game.py_screen, "Klaar", [29, 226, 72], [29, 226, 72])

        self.hair_button_1 = HairButton(game.py_screen, "resources/graphics/char/female_hairstyles/Female_Haircut_1.png", "")
        self.hair_button_2 = HairButton(game.py_screen, "resources/graphics/char/female_hairstyles/Female_Haircut_2.png", "")
        self.hair_button_3 = HairButton(game.py_screen, "resources/graphics/char/female_hairstyles/Female_Haircut_3.png", "")
        self.hair_button_4 = HairButton(game.py_screen, "resources/graphics/char/female_hairstyles/Female_Haircut_4.png", "")

        self.color_button_1 = HairButton(game.py_screen,
                                        "resources/graphics/char/female_character/Female_Black.png", "")
        self.color_button_2 = HairButton(game.py_screen,
                                        "resources/graphics/char/female_character/Female_Brown.png", "")
        self.color_button_3 = HairButton(game.py_screen,
                                        "resources/graphics/char/female_character/Female_Pale.png", "")
        self.color_button_4 = HairButton(game.py_screen,
                                        "resources/graphics/char/female_character/Female_White.png", "")

        self.clothes_button_1 = HairButton(game.py_screen, "resources/graphics/char/female_clothes/Female_Clothes_1.png", "")
        self.clothes_button_2 = HairButton(game.py_screen, "resources/graphics/char/female_clothes/Female_Clothes_2.png", "")
        self.clothes_button_3 = HairButton(game.py_screen, "resources/graphics/char/female_clothes/Female_Clothes_3.png", "")
        self.clothes_button_4 = HairButton(game.py_screen, "resources/graphics/char/female_clothes/Female_Clothes_4.png", "")

        self.mouse_position = None


        self.hair_button_1.render(self.mouse_position, -20, 370)
        self.hair_button_2.render(self.mouse_position, 70, 370)
        self.hair_button_3.render(self.mouse_position, 160, 370)
        self.hair_button_4.render(self.mouse_position, 250, 370)

        self.color_button_1.render(self.mouse_position, -20, 130)
        self.color_button_2.render(self.mouse_position, 70, 130)
        self.color_button_3.render(self.mouse_position, 160, 130)
        self.color_button_4.render(self.mouse_position, 250, 130)

        self.clothes_button_1.render(self.mouse_position, -20, 550)
        self.clothes_button_2.render(self.mouse_position, 70, 550)
        self.clothes_button_3.render(self.mouse_position, 160, 550)
        self.clothes_button_4.render(self.mouse_position, 250, 550)


    def on_render(self):
        if self.doorgaan == False:
            self.game.drawer.add_background_image("resources/graphics/char/Character_Customisation_with_menu.png")


            self.logo = self.game.drawer.add_image( self.color_global ,
                                              self.position_x, self.position_y, transparent=True)
            self.logo = self.game.drawer.add_image(self.hair_global,
                                              self.position_x, self.position_y, transparent=True)
            self.logo = self.game.drawer.add_image(self.clothes_global,
                                              self.position_x, self.position_y, transparent=True)

            self.game.drawer.draw_canvas()
            self.next_button.render(self.mouse_position, 920, 600)
            py.display.update()

    def on_events(self, events):
        for event in events:
            if event.type == py.MOUSEBUTTONDOWN:
                if self.next_button.is_clicked(self.mouse_position):
                    self.doorgaan = True
                    from src.game_screens.news_screen.news_screen import NewsScreen
                    self.game.drawer.clear()
                    NewsScreen(self.game)

                if self.hair_button_1.is_clicked(self.mouse_position):
                    self.hair_global = "resources/graphics/char/female_hairstyles/Female_Haircut_1.png"
                    GameState().set_char_hair(self.hair_global)
                    self.game.set_char_hair(self.hair_global)
                if self.hair_button_2.is_clicked(self.mouse_position):
                    self.hair_global = "resources/graphics/char/female_hairstyles/Female_Haircut_2.png"
                    self.on_render()
                    self.game.set_char_hair(self.hair_global)
                if self.hair_button_3.is_clicked(self.mouse_position):
                    self.hair_global = "resources/graphics/char/female_hairstyles/Female_Haircut_3.png"
                    self.on_render()
                    self.game.set_char_hair(self.hair_global)
                if self.hair_button_4.is_clicked(self.mouse_position):
                    self.hair_global =  "resources/graphics/char/female_hairstyles/Female_Haircut_4.png"
                    self.on_render()
                    self.game.set_char_hair(self.hair_global)

                if self.color_button_1.is_clicked(self.mouse_position):
                    self.color_global = "resources/graphics/char/female_character/Female_Black.png"
                    self.on_render()
                    self.game.set_char_color(self.color_global)
                if self.color_button_2.is_clicked(self.mouse_position):
                    self.color_global = "resources/graphics/char/female_character/Female_Brown.png"
                    self.on_render()
                    self.game.set_char_color(self.color_global)
                if self.color_button_3.is_clicked(self.mouse_position):
                    self.color_global = "resources/graphics/char/female_character/Female_Pale.png"
                    self.on_render()
                    self.game.set_char_color(self.color_global)
                if self.color_button_4.is_clicked(self.mouse_position):
                    self.color_global = "resources/graphics/char/female_character/Female_White.png"
                    self.on_render()
                    self.game.set_char_color(self.color_global)

                if self.clothes_button_1.is_clicked(self.mouse_position):
                    self.clothes_global = "resources/graphics/char/female_clothes/Female_Clothes_1.png"
                    self.on_render()
                    self.game.set_char_clothes(self.clothes_global)
                if self.clothes_button_2.is_clicked(self.mouse_position):
                    self.clothes_global = "resources/graphics/char/female_clothes/Female_Clothes_2.png"
                    self.on_render()
                    self.game.set_char_clothes(self.clothes_global)
                if self.clothes_button_3.is_clicked(self.mouse_position):
                    self.clothes_global = "resources/graphics/char/female_clothes/Female_Clothes_3.png"
                    self.on_render()
                    self.game.set_char_clothes(self.clothes_global)
                if self.clothes_button_4.is_clicked(self.mouse_position):
                    self.clothes_global = "resources/graphics/char/female_clothes/Female_Clothes_4.png"
                    self.on_render()
                    self.game.set_char_clothes(self.clothes_global)


    def on_update(self):
        pass

    def handle_key_input(self, keys):
        return

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position

    def handle_mouse_input(self, event):
        pass


class HairButton(ImageButton):
    def __init__(self, screen, image_location, text):
        text_color = [255, 255, 255]
        text_color_hover = [200, 200, 200]
        text_size = 40
        button_width = 100
        button_height = 70
        super().__init__(screen, image_location, text, text_color, text_color_hover, text_size,
                         button_width, button_height)

    def check_hover(self, mouse_position):
        if mouse_position is None:
            return
        if self.rect.collidepoint(mouse_position):
            self.is_hovering = True
        else:
            self.is_hovering = False


class ScreenButton(Button):
    def __init__(self, screen, text, button_color, button_color_hover):
        text_color = [255, 255, 255]
        text_color_hover = [200, 200, 200]
        text_size = 40
        button_width = 325
        button_height = 70
        super().__init__(screen, text, button_color, button_color_hover, text_color, text_color_hover, text_size,
                         button_width, button_height)
