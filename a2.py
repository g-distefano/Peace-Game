import random

ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

deck = [(suit,rank) for suit in suits for rank in ranks]
random.shuffle(deck)
print(deck)
Hand1 = deck[:26]
Hand2 = [26:]

