from game_logic.game import Game, GameState
from console_ui.messages import Printer

phrases = [
    "Game class",
    "Calls the methods",
    "Phrase object",
    "punctuation or numbers",
    "displayed again"
]


def get_phrase_value(phrase):
    list_letter = [single_char.get_value for single_char in phrase.characters]
    return " ".join(list_letter)


def check_if_game_over(game):
    if game.state == GameState.IN_PROGRESS:
        return
    if game.state == GameState.WON:
        Printer.print_end_game(True)
    elif game.state == GameState.LOST:
        Printer.print_end_game(False)
    game.state = GameState.TURN_OFF


def playing():
    game = Game(phrases)
    game.start_game()
    last_input = "_"
    Printer.show_elements(
        game.lives_player,
        get_phrase_value(game.active_phrase)
    )
    while game.state != GameState.TURN_OFF:
        character = Printer.input_user()
        try:
            was_bad = game.check_user_guess(character)
            if was_bad == None:
                character = last_input
            else:
                last_input = character
        except:
            Printer.report_exceptions()
        Printer.show_elements(
            game.lives_player,
            get_phrase_value(game.active_phrase),
            character
        )
        check_if_game_over(game)


if __name__ == "__main__":
    Printer.show_banner()
    while True:
        playing()
        answer = Printer.continue_playing()
        if answer.lower() == 'n':
            break
    Printer.end_message()
