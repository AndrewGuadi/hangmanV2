from Letters import Letters

class GameLetters():

    def __init__(self):
        pass       

    def populate_board_letters(self, guessed_letters):

        for letter in Letters:
            if letter.unused.lower() in guessed_letters:
                self.board_letters.append(letter.dead)
            else:
                self.board_letters.append(letter.unused)

        return self.board_letters

    



