from enum import Enum
from .phrase import Phrase

import random


class GameState(Enum):
    TURN_OFF = 0
    WON = 1
    LOST = 2
    IN_PROGRESS = 3


class Game:
    def __init__(self, phrases):
        self.phrases = phrases
        self.active_phrase = None
        self.lives_player = 5
        self.state = GameState.TURN_OFF

    @property
    def get_state(self):
        return self.state

    @property
    def get_lives_number(self):
        return self.lives_player

    def start_game(self):
        self.state = GameState.IN_PROGRESS
        self.active_phrase = Phrase(random.choice(self.phrases))
        self.keys_selected = []

    def check_user_guess(self, user_input):

        if user_input.isdigit() or len(user_input) > 1:
            raise TypeError
        if user_input in self.keys_selected:
            return

        self.keys_selected.append(user_input)
        is_contained = self.active_phrase.check_if_contains(user_input)
        if not is_contained:
            self.__remove_life()

        self.__update_state_game()

    def __remove_life(self):
        self.lives_player -= 1

    def __update_state_game(self):
        if self.active_phrase.were_shown():
            self.state = GameState.WON
        if self.lives_player == 0:
            self.state = GameState.LOST

    def match_over(self):
        self.state = GameState.TURN_OFF
