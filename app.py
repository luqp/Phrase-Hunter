# Import your Game class
from phrasehunter.game import Game

phrases = [
    "Game class",
    "method calls",
    "Phrase object",
    "punctuation or numbers",
    "displayed again"
]

# Create your Dunder Main statement.
if __name__ == "__main__":
    game = Game(phrases)
    game.start_game()
