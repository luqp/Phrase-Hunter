# Import your Game class
from phrasehunter.game import Game
from phrasehunter.canvas import Canvas 

phrases = [
    "Game class",
    "method calls",
    "Phrase object",
    "punctuation or numbers",
    "displayed again"
]


def playing():
    prompting_user = True

    while prompting_user:
        game = Game(phrases)
        game.start_game()
        answer = input("Play again? yes / [n]o: ")

        if answer.lower() == 'n':
            Canvas.end_message()
            prompting_user = False


if __name__ == "__main__":
    Canvas.show_banner()
    playing()
