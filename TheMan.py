

class TheMan:

    def __init__(self):
        self.hangman_drawings =[("O\n|\n\m"),("O\n|\m"),("O\n|\m"),("O\n|\m"),("O\n|\m"),("O\n|\m"),("O\n|\m"),("O\n|\m")]
    def get_hangman_drawing(self, failed_attempts):
        
        return self.hangman_drawings[failed_attempts]


man = TheMan()

print(man.get_hangman_drawing(2))