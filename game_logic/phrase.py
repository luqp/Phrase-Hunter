from .character import Character


class Phrase:

    def __init__(self, phrase):
        self.characters = [Character(single_char) for single_char in phrase]

    @property
    def get_characters(self):
        return [single_char.get_value for single_char in self.characters]

    def check_if_contains(self, char_guessed):
        is_within = False
        for letter in self.characters:
            if letter.single_character == ' ':
                continue
            if letter.check_if_equal(char_guessed):
                is_within = True
        return is_within

    def were_shown(self):
        shown = True
        for letter in self.characters:
            if not letter.was_guessed:
                shown = False
        return shown
