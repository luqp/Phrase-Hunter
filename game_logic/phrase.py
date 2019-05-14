from .character import Character


class Phrase:

    def __init__(self, phrase):
        self.characters = [Character(single_char) for single_char in phrase]

    def check_if_contains(self, char_guessed):
        was_guessed = False
        for letter in self.characters:
            if letter.single_character == ' ':
                continue
            if letter.check_if_equal(char_guessed):
                was_guessed = True
        return was_guessed

    def were_shown(self):
        for letter in self.characters:
            if not letter.was_guessed:
                return False
        return True
