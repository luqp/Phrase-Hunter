class Character:
    __HIDDEN = '_'

    def __init__(self, value):
        if len(value) != 1:
            raise ValueError("The value must be a single string character")
        self.single_character = value
        self.was_guessed = False if self.single_character != ' ' else True

    @property
    def get_value(self):
        return self.single_character if self.was_guessed else self.__HIDDEN

    def check_if_equal(self, character):
        guessed_right = self.single_character.lower() == character.lower()
        if guessed_right:
            self.was_guessed = True
        return guessed_right
