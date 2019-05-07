import os


class Message():

    STYLE_END = "\x1b[0m"
    BLUE_SQUARE = "\x1b[0;44m" + "  "
    CYAN_SQUARE = "\x1b[1;30;46m" + "  "
    COLOR_CYAN = "\x1b[1;36m"
    COLOR_BLUE = "\x1b[1;34m"
    COLOR_GRAY = "\x1b[1;30m"
    COLOR_RED = "\x1b[1;31m"
    EMOJI_HEART = "\u2764" + " "
    EMOJI_START = "\u2B50"
    EMOJI_BOMB = "\U0001F4A3"
    EMOJI_GHOST = "\U0001F47B"

    @classmethod
    def clear_screen(cls):
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def add_style(cls, phrase, style, phrase_no_style=""):
        return f"{style}{phrase}{cls.STYLE_END}{phrase_no_style}"

    @classmethod
    def input_user(cls):
        print()
        return input("Insert a letter -> ")

    @classmethod
    def continue_playing(cls):
        print(cls.add_style("Would you like to continue playing?", cls.COLOR_GRAY))
        print("Press enter to continue... or")
        print(cls.add_style("[n] ", cls.COLOR_CYAN, "to end play:"))
        return input("> ")

    @classmethod
    def report_exceptions(cls):
        print("You must input only a single string character")
        input("Press enter to continue...")

    @classmethod
    def end_message(cls):
        cls.clear_screen()
        print(f"See you next game ... {cls.EMOJI_GHOST}")
        print()

    @classmethod
    def show_banner(cls):
        cls.clear_screen()
        phrase_hunter = "P _ R A S E  _ U N T E R"
        times = (len(phrase_hunter) // 4) + 2
        BLUE_CYAN_SQUARE = f"{cls.BLUE_SQUARE}{cls.CYAN_SQUARE}{cls.STYLE_END}"
        CY_BL_MANY_TIMES = f"{cls.CYAN_SQUARE}{cls.BLUE_SQUARE}{cls.STYLE_END}" * times

        print(CY_BL_MANY_TIMES)
        print(BLUE_CYAN_SQUARE + f"{phrase_hunter}" + BLUE_CYAN_SQUARE)
        print(CY_BL_MANY_TIMES)
        print()
        print(cls.add_style("> [H] ", cls.COLOR_BLUE,
              "press enter to continue ..."))
        input()

    @classmethod
    def show_elements(cls, lives_player, phrase, user_input="_"):
        cls.clear_screen()
        print(cls.add_style("Guess the Phrase:", cls.COLOR_GRAY))
        print()
        print(cls.add_style(phrase, cls.COLOR_BLUE))
        print()
        if lives_player == 0:
            value, style = lives_player, cls.STYLE_END
        else:
            value, style = cls.EMOJI_HEART * lives_player, cls.COLOR_RED
        print(
            cls.add_style("Last input: ", cls.COLOR_GRAY, user_input),
            cls.add_style("· Total lives: ", cls.COLOR_GRAY),
            cls.add_style(value, style)
            )

    @classmethod
    def print_game_over(cls, positive_end):
        print()
        if positive_end:
            print(cls.add_style(
                "Congratulations!! ", cls.COLOR_CYAN,
                cls.EMOJI_START + " You win " + cls.EMOJI_START
            ))
        else:
            print(cls.add_style(
                "You stayed without hearts!! ", cls.COLOR_RED,
                cls.EMOJI_BOMB + " You loss " + cls.EMOJI_BOMB
            ))
        print()
