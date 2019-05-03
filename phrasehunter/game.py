import random

from phrasehunter.phrase import Phrase


class Game:

    def __init__(self, phrases):
        self.phrases = phrases
        self.active_phrase = None
        self.lives_player = None
        self.active = False


    def start_game(self):
        self.active_phrase = Phrase(random.choice(self.phrases))
        self.lives_player = 5
        self.active = True
        self.guess_letters()


    def guess_letters(self):
        pass


    def check_for_win_or_loss(self):
        pass


    def removing_live(self):
        pass



