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
    if game.state == GameState.LOST:
        Message.print_game_over(False)
    game.match_over()


def playing():
    game = Game(phrases)
    Message.show_banner()
    game.start_game()
    Message.show_elements(
        game.lives_player,
        get_phrase_value(game.active_phrase)
    )
    while game.state != GameState.TURN_OFF:
        character = Message.input_user()
        try:
            game.check_user_guess(character)
        except:
            Message.report_exceptions()
        Message.show_elements(
            game.lives_player,
            get_phrase_value(game.active_phrase),
            character
        )
        check_if_game_over(game)


if __name__ == "__main__":
    while True:
        playing()
        answer = Message.continue_playing()
        if answer.lower() == 'n':
            break
