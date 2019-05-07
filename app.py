from game_logic.game import Game, GameState
from console_ui.messages import Message

phrases = [
    "Game class",
    "Calls the methods",
    "Phrase object",
    "punctuation or numbers",
    "displayed again"
]


def get_phrase_value(phrase):
    return " ".join(phrase.get_characters)


def check_if_game_over(game):
    if game.state == GameState.IN_PROGRESS:
        return
    if game.state == GameState.WON:
        Message.print_game_over(True)
    elif game.state == GameState.LOST:
        Message.print_game_over(False)
    game.game_over()


def playing():
    game = Game(phrases)
    game.start_game()
    last_input = "_"
    Message.show_elements(
        game.lives_player,
        get_phrase_value(game.active_phrase)
    )
    while game.state != GameState.TURN_OFF:
        character = Message.input_user()
        try:
            was_bad = game.check_user_guess(character)
            if was_bad == None:
                character = last_input
            else:
                last_input = character
        except:
            Message.report_exceptions()
        Message.show_elements(
            game.lives_player,
            get_phrase_value(game.active_phrase),
            character
        )
        if was_bad:
            Message.notify_error()
        check_if_game_over(game)


if __name__ == "__main__":
    Message.show_banner()
    while True:
        playing()
        answer = Message.continue_playing()
        if answer.lower() == 'n':
            break
    Message.end_message()
