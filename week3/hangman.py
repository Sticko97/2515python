import random

class SecretWord:
    def __init__(self, word=None):
        if word:
            self.secret_word = word.upper() #
        else:
            with open("words.txt", "r") as file:
                words = file.read().splitlines()
                self.secret_word = random.choice(words).upper()
        self.letters_tried = []

    def show_letters(self, letters):
        revealed_word = ""
        for i, letter in enumerate(self.secret_word):
            if letter in letters:
                revealed_word += letter
            else:
                revealed_word += "_"
            if i != len(self.secret_word) - 1:
                revealed_word += " "
        return revealed_word

    def check_letters(self, letters):
        for letter in self.secret_word:
            if letter not in letters:
                return False
        return True

    def check(self, word):
        return word.upper() == self.secret_word

class Game:
    def __init__(self, turns=10):
        self.secret_word = SecretWord()
        self.turns = turns
        self.letters_tried = []

    def play_one_round(self):
        letter = input("Guess a letter: ", "A").upper()
        if letter in self.letters_tried:
            print("You already tried that letter. Try again.")
        else:
            self.letters_tried.append(letter)
            print(self.secret_word.show_letters(self.letters_tried))
            if self.secret_word.check_letters(self.letters_tried):
                print("Congratulations! You found the word.")
                self.turns -= 1
                return True
            elif len(self.letters_tried) == self.turns:
                print("You ran out of turns. The word was", self.secret_word.secret_word)
                return False
            else:
                self.turns -= 1
                return True
        return self.play_one_round()

    def play(self):
        while self.turns > 0:
            if "_" not in self.show_letters:
                print("You win the word was", self.secret_word)
                return True
            if not self.play_one_round():
                self.turns -= 1
        print("You lose. The word was", self.secret_word.secret_word)
        return False

if __name__ == "__main__":
    game = Game(10)
    game.play()
    word = input("Give a word")
    s = SecretWord()