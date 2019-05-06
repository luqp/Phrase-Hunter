import os


class Canvas():
    
    NO_STYLES = "\x1b[0m"
    HL_BLUE = "\x1b[0;44m"
    HL_CYAN = "\x1b[1;30;46m"
    COLOR_CYAN = "\x1b[1;36m"
    COLOR_BLUE = "\x1b[1;34m"
    COLOR_GRAY = "\x1b[1;30m"
    COLOR_RED = "\x1b[1;31m"
    EMOJI_HEART = "\u2764"
    EMOJI_START = "\u2B50"
    EMOJI_BOMB = "\U0001F4A3"
    EMOJI_GHOST = "\U0001F47B"



    @classmethod
    def clear_screen(cls):
        os.system('cls' if os.name == 'nt' else 'clear')


    @classmethod
    def show_banner(cls):
        is_h = False
        while not is_h:
            cls.clear_screen()
            numer_quart = 8
            print(f'{cls.HL_CYAN}  {cls.HL_BLUE}  ' * numer_quart)
            print(
                f'{cls.HL_BLUE}  {cls.HL_CYAN}  {cls.NO_STYLES}'
                'P _ R A S E  _ U N T E R'
                f'{cls.HL_BLUE}  {cls.HL_CYAN}  '
                )
            print(f'{cls.HL_CYAN}  {cls.HL_BLUE}  {cls.NO_STYLES}' * numer_quart)
            print()
            answer = input(f"Insert {cls.COLOR_BLUE}[H]{cls.NO_STYLES} to continue... ")
            is_h = True if answer.lower() == 'h' else False


    @classmethod
    def show_elements(cls, lives_player, phrase, user_input="_"):
        cls.clear_screen()
        print(f"{cls.COLOR_GRAY}Guess the Phrase:")
        print(f"{cls.COLOR_BLUE}")
        phrase.display()
        print(f"{cls.NO_STYLES}")
        print(
            f"{cls.COLOR_GRAY}Last input:{cls.NO_STYLES} {user_input}"
            f"{cls.COLOR_GRAY} · Total lives:{cls.NO_STYLES} {lives_player}")
        print(
            " " * 15,
            f"{cls.COLOR_RED}{cls.EMOJI_HEART}  {cls.NO_STYLES}" * lives_player)
            

    @classmethod
    def input_user(cls):
        return input("Insert a letter -> ")

    
    @classmethod
    def print_game_over(cls, positive_end):
        print()
        if positive_end:
            print(
                f"{cls.COLOR_CYAN}Congratulations!!{cls.NO_STYLES} "
                f"{cls.EMOJI_START} You win {cls.EMOJI_START}")
        else:
            print(
                f"{cls.COLOR_RED}You stayed without hearts!!{cls.NO_STYLES} "
                f"{cls.EMOJI_BOMB} You loss {cls.EMOJI_BOMB}")
        print()

    
    @classmethod
    def show_exceptions(cls):
        print("You must input only a single string character")
        input("Press enter to continue...")


    @classmethod
    def end_message(cls):
        cls.clear_screen()
        print(f"See you next game ... {cls.EMOJI_GHOST}")
        print()