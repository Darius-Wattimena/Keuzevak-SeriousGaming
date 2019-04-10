""" Game module """
import pygame as py, logging
from .helper.drawer import Drawer
from .helper.singleton import Singleton
from .global_screens.main_menu import MainMenu
from src.game_state import GameState

@Singleton
class Game:
    """ This class is where the start and stop the game and where we place the game loop. """

    def __init__(self):
        self.enable_logging()
        self.running = False
        self.drawer = None
        self.py_screen = None
        self.screen = None
        self.screen_change = None
        self.temp_screen = None
        self.config = None
        self.FULLSCREEN = False
        self.DEBUG = False
        self.clock = py.time.Clock()
        self.screen_center_width = None
        self.screen_center_height = None
        self.game_state = GameState()
        self.character_color = "resources/graphics/char/female_character/Female_Pale.png"
        self.character_clothes = "resources/graphics/char/female_clothes/Female_Clothes_3.png"
        self.character_hairstyle = "resources/graphics/char/female_hairstyles/Female_Haircut_3.png"
        self.money = 0
        self.dingengoed = 0
        self.need_instruction = True



    def get_char(self):
        return [self.character_color, self.character_clothes, self.character_hairstyle]

    def get_char_clothes(self):
        return self.character_clothes

    def get_char_color(self):
        return self.character_color

    def get_char_hair(self):
        return self.character_hairstyle

    def set_char_hair(self, link):
        self.character_hairstyle = link

    def set_char_color(self, link):
        self.character_color = link

    def set_char_clothes(self, link):
        self.character_clothes = link

    def enable_logging(self):
        self.logger = logging.getLogger('scope.name')
        self.logger.setLevel(logging.DEBUG)

        file_log_handler = logging.FileHandler('logfile.log')
        self.logger.addHandler(file_log_handler)

        stderr_log_handler = logging.StreamHandler()
        self.logger.addHandler(stderr_log_handler)

        # nice output format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_log_handler.setFormatter(formatter)
        stderr_log_handler.setFormatter(formatter)

    def start(self, py_screen, config):
        """ Start the game. """
        self.py_screen = py_screen
        self.screen_center_width = py_screen.get_width() / 2
        self.screen_center_height = py_screen.get_height() / 2
        self.config = config
        self.drawer = Drawer.Instance()
        self.drawer.set_screen(self.py_screen)
        self.screen = MainMenu(self)
        self.running = True
        self.game_loop()

    def game_loop(self):
        while self.running:
            self.clock.tick(30)
            self.screen.handle_key_input(py.key.get_pressed())
            self.screen.handle_mouse_input(py.mouse.get_pressed())
            self.screen.handle_mouse_position(py.mouse.get_pos())
            self.handle_events(py.event.get())
            if self.running:
                self.screen.on_update()
                self.screen.on_render()
            if self.screen_change:
                self.screen = self.temp_screen

    def handle_events(self, events):
        for event in events:
            if event.type == py.QUIT:
                self.quit()
        self.screen.on_events(events)

    def quit(self):
        """ Quit the game. """
        self.running = False
        py.quit()

    def set_screen(self, screen):
        self.screen_change = True
        self.temp_screen = screen
