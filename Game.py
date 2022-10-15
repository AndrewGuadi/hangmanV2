from UI import UI


class Game:
    def run(self):
        self.game = UI()

        keep_playing = True
        while keep_playing:

            self.game.display_game_state()
            self.game.guess_letter()
            keep_playing = self.game.compare_letter()
            if self.game.wrong_guesses >= len(self.game.hangman_drawings):
                print("Your man has Hanged. Please Try again!")
                break