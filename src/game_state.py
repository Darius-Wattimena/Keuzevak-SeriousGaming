
class GameState:
    def __init__(self):
        self.character_color = None
        self.character_clothes = None
        self.character_hairstyle = None
        self.money = 0

    def get_char(self):
        return [self.character_color, self.character_clothes, self.character_hairstyle]