import random

from phrasehunter.canvas import Canvas
from phrasehunter.phrase import Phrase


class Game:

    def __init__(self, phrases):
        self.phrases = phrases
        self.active_phrase = None
        self.lives_player = 5
        self.active = False


    def start_game(self):
        self.active = True
        self.active_phrase = Phrase(random.choice(self.phrases))
        Canvas.show_elements(self.lives_player, self.active_phrase)
        self.__prompting_player()


    def __prompting_player(self):
        keys_selected = []
        while self.active:
            letter = Canvas.input_user()
            if self.has_exceptions(letter) or letter in keys_selected:
                Canvas.show_elements(self.lives_player, self.active_phrase)
                continue
            
            keys_selected.append(letter)
            if not self.active_phrase.exist_character(letter):
                self.removing_live()

            Canvas.show_elements(self.lives_player, self.active_phrase, letter)
            self.check_for_win()
            self.check_for_loss()


    def check_for_win(self):
        all_were_guessed = self.active_phrase.check_state()
        if all_were_guessed:
            self.game_over(True)


    def check_for_loss(self):
        if self.lives_player == 0:
            self.game_over(False)


    def removing_live(self):
        self.lives_player -= 1


    def game_over(self, state):
        Canvas.print_game_over(state)
        self.active = False


    def has_exceptions(self, user_input):
        try:
            if len(user_input) > 1:
                raise TypeError()
        except TypeError:
            Canvas.show_exceptions()
            return True
        try:
            isinstance(int(user_input), int)
        except ValueError:
            return False
        else:
            Canvas.show_exceptions()
            return True
