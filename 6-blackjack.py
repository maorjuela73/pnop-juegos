import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} de {self.suit}"

class Deck:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["Corazones", "Diamantes", "Tréboles", "Picas"]

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        num_aces = 0

        for card in self.cards:
            if card.rank in ["K", "Q", "J"]:
                value += 10
            elif card.rank == "A":
                value += 11
                num_aces += 1
            else:
                value += int(card.rank)

        while num_aces > 0 and value > 21:
            value -= 10
            num_aces -= 1

        return value

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def play(self):
        print("¡Bienvenido al juego de Blackjack!")
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

        while True:
            print("Tus cartas: ", ", ".join(str(card) for card in self.player_hand.cards))
            print("Valor de tu mano:", self.player_hand.get_value())

            if self.player_hand.get_value() > 21:
                print("¡Te has pasado de 21! Pierdes.")
                break

            action = input("¿Quieres 'Pedir' o 'Plantarte'? ").lower()

            if action == "pedir":
                self.player_hand.add_card(self.deck.deal())
            elif action == "plantarte":
                while self.dealer_hand.get_value() < 17:
                    self.dealer_hand.add_card(self.deck.deal())
                print("Cartas del crupier: ", ", ".join(str(card) for card in self.dealer_hand.cards))
                print("Valor de la mano del crupier:", self.dealer_hand.get_value())
                if self.dealer_hand.get_value() > 21 or self.dealer_hand.get_value() < self.player_hand.get_value():
                    print("¡Ganaste!")
                elif self.dealer_hand.get_value() == self.player_hand.get_value():
                    print("Empate.")
                else:
                    print("El crupier gana.")
                break

if __name__ == "__main__":
    game = BlackjackGame()
    game.play()
