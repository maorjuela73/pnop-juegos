import random

# Definimos la clase Game
class WordGuessGame:
    def __init__(self):
        self.words = ["python", "programacion", "computadora", "juego", "adivinanza"]
        self.secret_word = random.choice(self.words).lower()
        self.guesses = []
        self.attempts = 0

    def play(self):
        print("¡Bienvenido al juego de adivinanza de palabras!")
        while True:
            display_word = self.display_word()
            print("Palabra a adivinar: " + display_word)
            if display_word == self.secret_word:
                print(f"¡Felicidades! Adivinaste la palabra '{self.secret_word}' en {self.attempts} intentos.")
                break
            guess = self.get_guess()
            self.guesses.append(guess)
            self.attempts += 1
            if guess not in self.secret_word:
                print("¡Incorrecto! La letra no está en la palabra.")

    def get_guess(self):
        while True:
            guess = input("Adivina una letra: ").lower()
            if len(guess) == 1 and guess.isalpha() and guess not in self.guesses:
                return guess
            else:
                print("Entrada inválida. Ingresa una letra no adivinada.")

    def display_word(self):
        display = ""
        for letter in self.secret_word:
            if letter in self.guesses:
                display += letter
            else:
                display += "_"
        return display

# Creamos una instancia del juego y lo iniciamos
if __name__ == "__main__":
    game = WordGuessGame()
    game.play()
