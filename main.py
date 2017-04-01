def h2n_text_parser(filename):
    """parses text from file"""
    weights = [[int(weight) for weight in line.split()] for line in open(filename)]  # create hand matrix from file
    return weights


def offsuit_cards(cards_matrix):
    """returns list of offsuit cards"""
    offsuits = []
    offsuit_cards_length = 0
    # take only values of offsuit cards from matrix
    for cards_matrix_line in cards_matrix[1:]:
        offsuit_cards_length += 1
        for card_weight in cards_matrix_line[:offsuit_cards_length]:
            offsuits.append(card_weight)
    return offsuits


def suit_cards(cards_matrix):
    """returns list of suit cards"""
    suits = []
    suit_cards_length = 0
    # take only values of suit cards from matrix
    for cards_matrix_line in cards_matrix[:-1]:
        suit_cards_length += 1
        for card_weight in cards_matrix_line[suit_cards_length:]:
            suits.append(card_weight)
    return suits


def pair_cards(cards_matrix):
    """returns list of pair cards"""
    pairs = [cards_matrix[i][i] for i in range(len(cards_matrix))]  # take only values of pair cards from matrix
    return pairs


def convert_into_percents(cards_range):
    """converts only offsuits cards into percents from card matrix"""
    max_cards_range_value = max(cards_range)
    percent_values = [round(card_value / max_cards_range_value, 2) for card_value in cards_range]
    return percent_values


def convert_into_crev_format():
    """rounds weights of percents  into crev format(5 weights)"""
    pass


def write_crev_format_in_excel():
    """writes crev weighted data in excel's table for handy usage"""
    pass


weights = h2n_text_parser("input.txt")

print(convert_into_percents(suit_cards(weights)))
print(convert_into_percents(offsuit_cards(weights)))
print(convert_into_percents(pair_cards(weights)))
