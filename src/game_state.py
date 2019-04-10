
class GameState:
    def __init__(self):
        self.character_color = "resources/graphics/char/female_character/Female_Pale.png"
        self.character_clothes = "resources/graphics/char/female_clothes/Female_Clothes_3.png"
        self.character_hairstyle = "resources/graphics/char/female_hairstyles/Female_Haircut_3.png"
        self.money = 0

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
