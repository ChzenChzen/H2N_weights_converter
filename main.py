def h2n_text_parser(filename):
    """parses text from file"""
    weights = [[int(weight) for weight in line.split()] for line in open(filename)]  # create hand matrix from file
    return weights


def offsuit_cards(cards_matrix):
    """returns list of offsuit cards"""
    offsuits = []
    offsuit_cards_length = 0
    # take only values of offsuits cards from matrix
    for cards_matrix_line in cards_matrix[1:]:
        offsuit_cards_length += 1
        for card_weight in cards_matrix_line[:offsuit_cards_length]:
            offsuits.append(card_weight)
    return offsuits


def suit_cards(cards_matrix):
    """returns list of suit cards"""
    suits = []
    suit_cards_length = 0
    # take only values of suits cards from matrix
    for cards_matrix_line in cards_matrix[:-1]:
        suit_cards_length += 1
        for card_weight in cards_matrix_line[suit_cards_length:]:
            suits.append(card_weight)
    return suits

def convert_into_percents_offsuits(cards_matrix):
    """converts only offsuits cards into percents from card matrix"""
    max_offsuit_cards_value = max(offsuit_cards(cards_matrix))
    percent_value_offsuits = [round(offsuit_card_value / max_offsuit_cards_value, 2) for offsuit_card_value in
                              offsuit_cards(cards_matrix)]
    return percent_value_offsuits


def convert_into_percents(weights):
    """converts weights of raw h2n into percents"""
    print(weights)
    pass


def convert_into_crev_format():
    """rounds weights of percents  into crev format(5 weights)"""
    pass


def write_crev_format_in_excel():
    """writes crev weighted data in excel's table for handy usage"""
    pass


weights = h2n_text_parser("input.txt")
print(suit_cards(weights))