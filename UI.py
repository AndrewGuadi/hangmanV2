from GameLetters import GameLetters
import random

class UI(GameLetters):

    def __init__(self):
        self.game_word = self.initialize_game_word()
        self.current_letter = ''
        self.board_letters = []
        self.guessed_letters = []
        self.wrong_guesses = 0
        self.hangman_drawings = [(""),("O"),(" O\n |"),(" O\n |\n/"),(" O\n |\n/ \\"),(" O\n/|\n/ \\"),(" O\n/|\\ \n/ \\")]      
    def get_hangman_drawing(self, failed_attempts):
        
        return self.hangman_drawings[failed_attempts]

    def initialize_game_word(self):

        game_words = []

        with open('words.txt') as file:

            for line in file:
                game_words.append(line.rstrip('\r\n'))

            word = random.choice(game_words)
            return word

    def display_game_word(self):
        

        display_word = ''

        for letter in self.game_word:
            if str(letter) in self.guessed_letters:
                display_word += f"{letter} "
            elif str(letter).upper() in self.board_letters:
                display_word += "_ "
            else:
                print("ERROR: That letter isnt found")
        return display_word
    

    def guess_letter(self):

        while True:
            letter = input("GUESS: ")

            if len(letter) == 1:
                break
            print("Please Only Choose One Letter at a Time")
        letter = letter.strip().lower()
        self.guessed_letters.append(letter)
        self.current_letter = (letter)
        

    def compare_letter(self):
        
        if self.current_letter in self.game_word:
            print("This Letter was found")
            if "_" in self.display_game_word():
                return True
            else:
                print("You Won")
                return False
 
        else:
            print("This letter was most definitely not in the word")
            self.wrong_guesses += 1
            return True
            
    def display_game_state(self):
        self.board_letters.clear()
        self.board_letters = self.populate_board_letters(self.guessed_letters)
        print(f"\n\n\n{self.get_hangman_drawing(self.wrong_guesses)}\n{self.populate_board_letters(self.guessed_letters)}\n{self.display_game_word()}")
        


    