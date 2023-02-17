def rank_hands(cards, suits, game_data):

    def high_card():
        for player in game_data:
            # The hand comes pre-sorted low to high, look at the last card index
            player['hand_rank'] = 'High Card (' + cards[player['hand'][4][0]][1] + ')'
            _rank = '1.' + str(player['hand'][4][0]).rjust(2, '0') + str(player['hand'][3][0]).rjust(2, '0') + str(player['hand'][2][0]).rjust(2, '0') + str(player['hand'][1][0]).rjust(2, '0') + str(player['hand'][0][0]).rjust(2, '0')
            player['rank_score'] = float(_rank)

    def pairs():
        for player in game_data:

            card_values = []

            # Populate a list of just the card index
            li = []
            for i in player['hand']:
                li.append(i[0])

            # Search for duplicates in the list
            for i in li:
                if li.count(i) > 1 and card_values.count(i) == 0:
                    card_values.append(i)

            card_values.sort(reverse=True)

            if len(card_values) == 2:
                player['hand_rank'] = 'Two Pair (' + cards[card_values[0]][1]
                suffix = 'es and ' if cards[card_values[0]][0] == '6' else 's and '
                player['hand_rank'] += suffix + cards[card_values[1]][1]
                suffix = 'es)' if cards[card_values[1]][0] == '6' else 's)'
                player['hand_rank'] += suffix
                player['rank_score'] = 3

            elif len(card_values) == 1:
                player['hand_rank'] = 'Pair (' + cards[card_values[0]][1]
                suffix = 'es)' if cards[card_values[0]][0] == '6' else 's)'
                player['hand_rank'] += suffix
                player['rank_score'] = 2

    def three_kind():
        for player in game_data:

            card_values = []

            # Populate a list of just the card index
            li = []
            for i in player['hand']:
                li.append(i[0])

            # Search for three-of-a-kind in the list
            for i in li:
                if li.count(i) > 2:
                    card_values.append(i)
                    break

            if len(card_values):
                player['hand_rank'] = 'Three-of-a-Kind (' + cards[card_values[0]][1]
                suffix = 'es)' if cards[card_values[0]][0] == '6' else 's)'
                player['hand_rank'] += suffix
                player['rank_score'] = 4

    def straight():
        for player in game_data:

            # Populate a list of just the card index
            li = []
            for i in player['hand']:
                li.append(i[0])

            # Search for straight in the list
            li.sort()
            if li[1] == li[0] + 1 and li[2] == li[1] + 1 and li[3] == li[2] + 1 and li[4] == li[3] + 1:
                player['hand_rank'] = 'Straight (' + cards[li[4]][1] + ' High)'
                player['rank_score'] = 5

    def flush():
        for player in game_data:

            # Populate a list of just the card index
            li = []
            for i in player['hand']:
                li.append(i[0])

            li.sort()

            # Populate a list of just the suit index
            su = []
            for i in player['hand']:
                su.append(i[1])

            # Search for flush in the list
            if su.count(su[0]) == 5:
                player['hand_rank'] = 'Flush (' + suits[su[0]][0] + ', ' + cards[li[4]][1] + ' High)'
                player['rank_score'] = 6

    def full_house():
        for player in game_data:

            card_values = [None, None]

            # Populate a list of just the card index
            li = []
            for i in player['hand']:
                li.append(i[0])

            # Search list for three-of-a-kind
            for i in li:
                if li.count(i) == 3:
                    card_values[0] = i
                    break

            # Search list for pair
            for i in li:
                if li.count(i) == 2:
                    card_values[1] = i
                    break

            if card_values[0] is not None and card_values[1] is not None:
                player['hand_rank'] = 'Full House (' + cards[card_values[0]][1]
                suffix = 'es over ' if cards[card_values[0]][0] == '6' else 's over '
                player['hand_rank'] += suffix + cards[card_values[1]][1]
                suffix = 'es)' if cards[card_values[1]][0] == '6' else 's)'
                player['hand_rank'] += suffix
                player['rank_score'] = 7

    def four_kind():
        for player in game_data:

            card_values = []

            # Populate a list of just the card index
            li = []
            for i in player['hand']:
                li.append(i[0])

            # Search for three-of-a-kind in the list
            for i in li:
                if li.count(i) > 3:
                    card_values.append(i)
                    break

            if len(card_values):
                player['hand_rank'] = 'Four-of-a-Kind (' + cards[card_values[0]][1]
                suffix = 'es)' if cards[card_values[0]][0] == '6' else 's)'
                player['hand_rank'] += suffix
                player['rank_score'] = 8

    def straight_flush():
        for player in game_data:

            _flush = False

            # Populate a list of just the card index
            li = []
            for i in player['hand']:
                li.append(i[0])

            # Populate a list of just the suit index
            su = []
            for i in player['hand']:
                su.append(i[1])

            if su.count(su[0] == 5):
                _flush = True

            # Search for straight in the list
            li.sort()
            if _flush and li[1] == li[0] + 1 and li[2] == li[1] + 1 and li[3] == li[2] + 1 and li[4] == li[3] + 1:

                if li[4] == len(cards) - 1:
                    player['hand_rank'] = 'Royal Flush (' + suits[su[4]][1] + ')'
                    player['rank_score'] = 10

                else:
                    player['hand_rank'] = 'Straight Flush (' + suits[su[4]][1] + ' ' + cards[li[4]][1] + ' High)'
                    player['rank_score'] = 9

    def compare_hands():
        if game_data[0]['rank_score'] > game_data[1]['rank_score']:
            game_data[0]['result'] = '\033[95mWIN!'

        elif game_data[0]['rank_score'] < game_data[1]['rank_score']:
            game_data[1]['result'] = '\033[95mWIN!'

        else:
            # Same hand rank, determine best of the two
            pass

    # Evaluate hands for:
    high_card() 
    pairs()
    three_kind()
    straight()
    flush()
    full_house()
    four_kind()
    straight_flush()

    compare_hands()

    return True
