from src.game_screens.news_screen.news_items import NewsItems
from src.helper.button import Button
from src.helper.label import Label
from src.helper.screen_base import ScreenBase
from src.game_config import GameConfig
import pygame as py


class NewsScreen(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.mouse_position = None
        self.game.drawer.add_background_image("resources/graphics/Studio.png")
        self.show_news_button = CustomButton(game.py_screen, "Show News", [100, 100, 100], [100, 100, 100])
        self.news_true_button = CustomButton(game.py_screen, "Waar", [29, 226, 72], [29, 226, 72])
        self.news_false_button = CustomButton(game.py_screen, "Niet waar", [216, 86, 86], [216, 86, 86])
        self.dismiss_feedback = CustomButton(game.py_screen, "Oke", [100, 100, 100], [100, 100, 100])
        self.dismiss_feedback.visible = False
        self.news_buttons_visible = False
        self.news_items = NewsItems(game.drawer)
        self.current_news_item = None
        self.show_news_item = False
        self.headline_text = Label(game.py_screen, "", [0, 0, 0], 64, font="resources/fonts/helsinki.ttf")
        self.headline_text_x = 25
        self.headline_set = False
        self.items_count = 0

    def on_render(self):
        self.game.drawer.draw_canvas()
        if self.show_news_button.visible:
            self.show_news_button.render(self.mouse_position, 1280 - 335, 10)

        self.headline_text.render(self.headline_text_x, 640)

        if self.news_buttons_visible:
            self.news_true_button.render(self.mouse_position, 75, 450)
            self.news_false_button.render(self.mouse_position, 425, 450)

        if self.dismiss_feedback.visible:
            self.dismiss_feedback.render(self.mouse_position, 1280-345, 530)
        py.display.update()

    def on_events(self, events):
        for event in events:
            if event.type == py.MOUSEBUTTONDOWN:
                if self.show_news_button.is_clicked(self.mouse_position) and self.show_news_button.visible:
                    self.current_news_item = self.news_items.get_random_news_item()
                    self.show_news_button.visible = False
                    self.show_news_item = True
                    self.items_count += 1
                if self.news_true_button.is_clicked(self.mouse_position) and self.news_buttons_visible:
                    if self.current_news_item.is_fake_news:
                        self.current_news_item.show_result(True)
                    self.current_news_item.unload_image()
                    self.news_buttons_visible = False
                    self.dismiss_feedback.visible = True
                    self.show_news_item = False
                if self.news_false_button.is_clicked(self.mouse_position) and self.news_buttons_visible:
                    if self.current_news_item.is_fake_news:
                        self.current_news_item.show_result(False)
                    self.current_news_item.unload_image()
                    self.news_buttons_visible = False
                    self.dismiss_feedback.visible = True
                    self.show_news_item = False
                if self.dismiss_feedback.is_clicked(self.mouse_position) and self.dismiss_feedback.visible:
                    self.dismiss_feedback.visible = False
                    self.current_news_item.unload_feedback()
                    self.current_news_item = None
                    self.show_news_button.visible = True
                    if self.items_count >= GameConfig().items_each_day:
                        from src.game_screens.end_day_screen.end_day_screen import EndDayScreen
                        self.game.drawer.clear()
                        EndDayScreen(self.game)

    def on_update(self):
        if self.show_news_item:
            self.current_news_item.load_image()
            self.news_buttons_visible = True

        if self.current_news_item is not None:
            self.headline_text_x -= 2
            if not self.headline_set and len(self.headline_text.text) < 400:
                self.headline_text.text = "".join((self.headline_text.text, self.current_news_item.headline))
                self.headline_set = True
        else:
            self.headline_set = False


    def handle_key_input(self, keys):
        return

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position

    def handle_mouse_input(self, event):
        pass


class CustomButton(Button):
    def __init__(self, screen, text, button_color, button_color_hover):
        text_color = [255, 255, 255]
        text_color_hover = [200, 200, 200]
        text_size = 40
        button_width = 325
        button_height = 70
        super().__init__(screen, text, button_color, button_color_hover, text_color, text_color_hover, text_size,
                         button_width, button_height)
        self.visible = True

