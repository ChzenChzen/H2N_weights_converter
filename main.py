def h2n_text_parser(filename):
    """parses text from file"""
    weights = [[int(weight) for weight in line.split()] for line in open(filename)]  # create hand matrix from file
    return weights


def get_offsuit_cards(cards_matrix):
    """returns list of offsuit cards"""
    offsuits = []
    offsuit_cards_length = 0
    # take only values of offsuit cards from matrix
    for cards_matrix_row in cards_matrix[1:]:
        offsuit_cards_length += 1
        for card_weight in cards_matrix_row[:offsuit_cards_length]:
            offsuits.append(card_weight)
    return offsuits


def get_suit_cards(cards_matrix):
    """returns list of suit cards"""
    suits = []
    suit_cards_length = 0
    # take only values of suit cards from matrix
    for cards_matrix_row in cards_matrix[:-1]:
        suit_cards_length += 1
        for card_weight in cards_matrix_row[suit_cards_length:]:
            suits.append(card_weight)
    return suits


def get_pair_cards(cards_matrix):
    """returns list of pair cards"""
    pairs = [cards_matrix[i][i] for i in range(13)]  # take only values of pair cards from matrix
    return pairs


def convert_into_percents(cards_range):
    """converts only offsuits cards into percents from card matrix"""
    max_cards_range_value = max(cards_range)
    percent_values = [round(card_value / max_cards_range_value, 2) for card_value in cards_range]
    return percent_values


def show_matrix(matrix):
    for row in matrix:
        print(str(row) + "\n")


def convert_into_crev_format():
    """rounds weights of percents  into crev format(5 weights)"""
    pass


def write_crev_format_in_excel():
    """writes crev weighted data in excel's table for handy usage"""
    pass


def pair_cards(values):
    """does dict of pair cards with value"""
    pair_cards_val_in_percent = convert_into_percents(get_pair_cards(values))  # list of pair cards
    pair_card_labels = ['AA', 'KK', 'QQ', 'JJ', 'TT', '99', '88', '77', '66', '55', '44', '33', '22']
    pair_cards_dict = {}
    for index, pair_card_label in enumerate(pair_card_labels):
        pair_cards_dict[pair_card_label] = pair_cards_val_in_percent[index]
    return pair_cards_dict


def offsuit_cards(values):
    """does dict of pair cards with value"""
    offsuit_cards_val_in_percent = convert_into_percents(get_offsuit_cards(values))  # list of pair cards
    offsuit_card_labels = ['AKo',
                           'AQo', 'KQo',
                           'AJo', 'KJo', 'QJo',
                           'ATo', 'KTo', 'QTo', 'JTo',
                           'A9o', 'K9o', 'Q9o', 'J9o', 'T9o',
                           'A8o', 'K8o', 'Q8o', 'J8o', 'T8o', '98o',
                           'A7o', 'K7o', 'Q7o', 'J7o', 'T7o', '97o', '87o',
                           'A6o', 'K6o', 'Q6o', 'J6o', 'T6o', '96o', '86o', '76o',
                           'A5o', 'K5o', 'Q5o', 'J5o', 'T5o', '95o', '85o', '75o', '65o',
                           'A4o', 'K4o', 'Q4o', 'J4o', 'T4o', '94o', '84o', '74o', '64o', '54o',
                           'A3o', 'K3o', 'Q3o', 'J3o', 'T3o', '93o', '83o', '73o', '63o', '53o', '43o',
                           'A2o', 'K2o', 'Q2o', 'J2o', 'T2o', '92o', '82o', '72o', '62o', '52o', '42o', '32o']
    offsuit_cards_dict = {}
    for index, offsuit_card_label in enumerate(offsuit_card_labels):
        offsuit_cards_dict[offsuit_card_label] = offsuit_cards_val_in_percent[index]
    return offsuit_cards_dict


def suit_cards(values):
    """does dict of pair cards with value"""
    suit_cards_val_in_percent = convert_into_percents(get_suit_cards(values))  # list of pair cards
    suit_card_labels = ['AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s',
                        'KQs', 'KJs', 'KTs', 'K9s', 'K8s', 'K7s', 'K6s', 'K5s', 'K4s', 'K3s', 'K2s',
                        'QJs', 'QTs', 'Q9s', 'Q8s', 'Q7s', 'Q6s', 'Q5s', 'Q4s', 'Q3s', 'Q2s',
                        'JTs', 'J9s', 'J8s', 'J7s', 'J6s', 'J5s', 'J4s', 'J3s', 'J2s',
                        'T9s', 'T8s', 'T7s', 'T6s', 'T5s', 'T4s', 'T3s', 'T2s',
                        '98s', '97s', '96s', '95s', '94s', '93s', '92s',
                        '87s', '86s', '85s', '84s', '83s', '82s',
                        '76s', '75s', '74s', '73s', '72s',
                        '65s', '64s', '63s', '62s',
                        '54s', '53s', '52s',
                        '43s', '42s',
                        '32s']
    suit_cards_dict = {}
    for index, suit_card_label in enumerate(suit_card_labels):
        suit_cards_dict[suit_card_label] = suit_cards_val_in_percent[index]
    return suit_cards_dict

data = h2n_text_parser("input.txt")

all_cards = dict(**pair_cards(data), **offsuit_cards(data), **suit_cards(data))
range0_19, range20_39, range40_59, range60_79, range80_100 = [], [], [], [], []

for key, value in all_cards.items():
    if value < 0.2:
        range0_19.append(key)
    elif 0.2 <= value < 0.4:
        range20_39.append(key)
    elif 0.4 <= value < 0.6:
        range40_59.append(key)
    elif 0.6 <= value < 0.8:
        range60_79.append(key)
    elif 0.8 <= value <= 1:
        range80_100.append(key)

range_output = '[20]' + ', '.join(range0_19) + '[/20],' + '[40]' + ', '.join(
    range20_39) + '[/40],' + '[60]' + ', '.join(range40_59) + '[/60],' + '[80]' + ', '.join(
    range60_79) + '[/80],' + '[100]' + ', '.join(range80_100) + '[/100]'
print(range_output)

end = input()
