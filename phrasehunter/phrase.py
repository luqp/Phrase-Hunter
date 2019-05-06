from phrasehunter.character import Character

class Phrase:

    def __init__(self, phrase):
        self.characters = [Character(letter) for letter in phrase]


    def display(self):
        letters = [letter.show() for letter in self.characters]
        print(' '.join(letters))


    def exist_character(self, char_guessed):
        was_guessed = False
        for letter in self.characters:
            if letter.value == ' ':
                continue
            if letter.check_if_exist(char_guessed):
                was_guessed = True

        return was_guessed


    def check_state(self):
        were_shown = True
        for letter in self.characters:
            if not letter.was_guessed:
                were_shown = False

        return were_shown
