import itertools
import random

def deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    suits = ['c', 'd', 'h', 's']
    return [(rank, suit) for rank, suit in itertools.product(ranks, suits)]

def shuffle_deck(deck):
    shuffled_deck = deck[:]
    random.shuffle(shuffled_deck)
    return shuffled_deck

def deal(deck, n):
    hands = []
    for _ in range(n):
        hand = []
        for _ in range(5):
            card = deck.pop()
            hand.append(card)
        hands.append(hand)
    return hands

# Testowanie funkcji
print("Stwórz talię:")
my_deck = deck()
print(my_deck)

print("\nPotasuj talię:")
shuffled_deck = shuffle_deck(my_deck)
print(shuffled_deck)

print("\nRozdaj karty graczom:")
hands = deal(shuffled_deck, 4)
for i, hand in enumerate(hands):
    print(f"Gracz {i+1}: {hand}")
