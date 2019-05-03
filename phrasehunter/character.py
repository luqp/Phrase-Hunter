class Character:
    
    _hidden = '_'

    
    def __init__(self, value):
        if len(value) != 1:
            raise ValueError("The value must be a single string character")

        self.value = value
        self.was_guessed = False if self.value != ' ' else True
    

    def check_if_exist(self, character):
        guessed_right = self.value.lower() == character.lower()
        if guessed_right:
            self.was_guessed = True

        return guessed_right


    def show(self):
        return self.value if self.was_guessed else self._hidden