import random
import score

# Short | Text | Nickname | Rank
cards = [
    ('2',  'Two',   'Deuce',     2),
    ('3',  'Three', 'Crab',      3),
    ('4',  'Four',  'Sharp Top', 4),
    ('5',  'Five',  'Nickel',    5),
    ('6',  'Six',   'Sax',       6),
    ('7',  'Seven', 'Fishhook',  7),
    ('8',  'Eight', 'Snowman',   8),
    ('9',  'Nine',  'Neener',    9),
    ('10', 'Ten',   'X',        10),
    ('J',  'Jack',  'Jake',     11),
    ('Q',  'Queen', 'Queenie',  12),
    ('K',  'King',  'Cowboy',   13),
    ('A',  'Ace',   'Bullet',   14)
]

# Text | Character | Entity | Color | ANSI | Rank # End Ansi with '\033[0m'
suits = [
    ('Clubs',    '♣', '&clubs',   'Black', '\033[94m', 1),
    ('Diamonds', '♦', '&diams;',  'Red',   '\033[91m', 2),
    ('Hearts',   '♥', '&hearts;', 'Red',   '\033[91m', 3),
    ('Spades',   '♠', '&spades;', 'Black', '\033[94m', 4)
]

hand_rankings = (
    'High Card',
    'Pair',
    'Two Pair',
    'Three-of-a-Kind',
    'Straight',
    'Flush',
    'Full House',
    'Four-of-a-Kind',
    'Straight Flush',
    'Royal Flush'
)

deck = []

game_data = [
    {
        'player': 'Player 1',
        'hand': [],
        'display': '',
        'hand_rank': '',
        'rank_score': float(0),
        'result': ''
    },
    {
        'player': 'Player 2',
        'hand': [],
        'display': '',
        'hand_rank': '',
        'rank_score': float(0),
        'result': ''
    }
]


def build_deck():

    deck.clear()

    x = 0
    for card in cards:
        y = 0
        for suit in suits:
            # 52 Tuples (card index, suit index)
            deck.append((x, y))
            y += 1
        x += 1


def shuffle(times):

    # Shuffle the cards
    for i in range(times):
        random.shuffle(deck)


def deal_cards():

    game_data[0]['hand'].clear()
    game_data[1]['hand'].clear()

    shuffle(6)

    # A hand is 5 tuples (card, suit)
    for i in range(5):
        _card = deck.pop(0)
        game_data[0]['hand'].append(_card)
        _card = deck.pop(0)
        game_data[1]['hand'].append(_card)

    # Hands are sorted by card, low to high
    game_data[0]['hand'].sort()
    game_data[1]['hand'].sort()

    score.rank_hands(cards, suits, game_data)

    # Each hand is built up into a fancy string of text
    for i in range(5):
        game_data[0]['display'] += suits[game_data[0]['hand'][i][1]][4] + cards[game_data[0]['hand'][i][0]][0] + suits[game_data[0]['hand'][i][1]][1] + '\033[0m '
        game_data[1]['display'] += suits[game_data[1]['hand'][i][1]][4] + cards[game_data[1]['hand'][i][0]][0] + suits[game_data[1]['hand'][i][1]][1] + '\033[0m '

    # Finally more fancy strings used to print the hands
    print('\n\033[93m' + game_data[0]['player'] + ': ' + game_data[0]['result'] + '\033[0m\n' + game_data[0]['display'] + '\n' + game_data[0]['hand_rank'])
    print('\n\033[93m' + game_data[1]['player'] + ': ' + game_data[1]['result'] + '\033[0m\n' + game_data[1]['display'] + '\n' + game_data[1]['hand_rank'])


build_deck()
deal_cards()
