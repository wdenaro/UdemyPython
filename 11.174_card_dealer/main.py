from random import shuffle

cards = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']

hand1 = []
hand2 = []

def deal_cards():

    shuffle(cards)

    for i in range(5):
        hand1.append(cards.pop(0))
        hand2.append(cards.pop(0))

    print(f'\nHand 1:\n{hand1}')
    print(f'Hand 2:\n{hand2}')

deal_cards()