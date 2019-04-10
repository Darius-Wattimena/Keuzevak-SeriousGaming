import pygame as py

class InstructionDisplay:
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.game.drawer.add_background_image("resources/graphics/computer/EXAMPLE_PopUp_Computer.jpg")

        if game.need_instruction == False:
            from src.game_screens.end_day_screen.end_day_screen import EndDayScreen
            self.game.drawer.clear()
            EndDayScreen(self.game)

    def on_render(self):
        self.game.drawer.draw_canvas()

        py.display.update()

    def on_events(self, events):
        for event in events:
            if event.type == py.MOUSEBUTTONDOWN:
                self.game.need_instruction = False
                from src.game_screens.end_day_screen.end_day_screen import EndDayScreen
                self.game.drawer.clear()
                EndDayScreen(self.game)

    def on_update(self):
        pass

    def handle_key_input(self, keys):
        return

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position

    def handle_mouse_input(self, event):
        pass



