import random


class NewsItems:
    def __init__(self, drawer):
        self.item_list = [NewsItem("resources/graphics/news_items/POPUP_DronkenMan_F.png",
                                   "resources/graphics/news_items/Feedback_Goed.png",
                                   "resources/graphics/news_items/Feedback_Fout.png",
                                   "MAN WINT EX-VRIENDIN TERUG DANKZIJ DRONKEN TELEFOONTJES | ", True, drawer),
                          NewsItem("resources/graphics/news_items/POPUP_NatureGoedSlecht_F.png",
                                   "resources/graphics/news_items/Feedback_Goed.png",
                                   "resources/graphics/news_items/Feedback_Fout.png",
                                   "IS DE MENS VAN NATURE GOED OF SLECHT? | ", True, drawer),
                          NewsItem("resources/graphics/news_items/POPUP_VoiceOfHolland_F.png",
                                   "resources/graphics/news_items/Feedback_Goed.png",
                                   "resources/graphics/news_items/Feedback_Fout.png",
                                   "VOICE OF HOLLAND BEVOORDEELT MENSEN DIE GOED KUNNEN ZINGEN | ", True, drawer)]

    def get_random_news_item(self):
        return self.item_list[random.randint(0, len(self.item_list) - 1)]


class NewsItem:
    def __init__(self, image_loc, correct_result_loc, wrong_result_loc, headline, is_fake_news, drawer):
        self.image_loc = image_loc
        self.correct_result_loc = correct_result_loc
        self.wrong_result_loc = wrong_result_loc
        self.headline = headline
        self.is_fake_news = is_fake_news
        self.drawer = drawer
        self.loaded = False
        self.feedback_loaded = False
        self.image = None
        self.feedback_image = None

    def show_result(self, marked_as_true):
        if marked_as_true and not self.is_fake_news:
            self.load_correct_feedback()
        elif marked_as_true and self.is_fake_news:
            self.load_wrong_feedback()
        elif not marked_as_true and not self.is_fake_news:
            self.load_wrong_feedback()
        elif not marked_as_true and self.is_fake_news:
            self.load_correct_feedback()

    def load_correct_feedback(self):
        if not self.feedback_loaded:
            self.feedback_image = self.drawer.add_image(self.correct_result_loc, 0, 0, transparent=True)
            self.feedback_loaded = True

    def load_wrong_feedback(self):
        if not self.feedback_loaded:
            self.feedback_image = self.drawer.add_image(self.wrong_result_loc, 0, 0, transparent=True)
            self.feedback_loaded = True

    def load_image(self):
        if not self.loaded:
            self.image = self.drawer.add_image(self.image_loc, 0, 0, transparent=True)
            self.loaded = True

    def unload_image(self):
        if self.loaded:
            self.drawer.remove_image(self.image)
            self.loaded = False

    def unload_feedback(self):
        if self.feedback_loaded:
            self.drawer.remove_image(self.feedback_image)
            self.feedback_loaded = False
