import pandas as pd

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


def add_offsuit_cards_percents(offsuit_values, cards_matrix):
    """add offsuit cards in cards matrix"""
    n = 0
    for row in cards_matrix:
        row[:n] = offsuit_values[:n]
        del offsuit_values[:n]
        n += 1


def add_pair_cards(pair_values, cards_matrix):
    """add pair cards in cards matrix"""
    for n in range(13):
        cards_matrix[n][n] = pair_values[n]


def add_suit_cards_percents(suit_values, cards_matrix):
    """add suit cards in cards matrix"""
    n = 1
    for row in cards_matrix:
        row[n:] = suit_values[:n]
        del suit_values[:n]
        n += 1


def convert_into_crev_format():
    """rounds weights of percents  into crev format(5 weights)"""
    pass


def write_crev_format_in_excel():
    """writes crev weighted data in excel's table for handy usage"""
    pass


data = h2n_text_parser("input.txt")
matrix = [['' for x in range(13)] for x in range(13)]  # create empty matrix 13*13
offsuit_cards_in_percent = convert_into_percents(get_offsuit_cards(data))
pair_cards_in_percent = convert_into_percents(get_pair_cards(data))
suit_cards_in_percent = convert_into_percents(get_suit_cards(data))

print("p: " + str(pair_cards_in_percent))
print("o: " + str(offsuit_cards_in_percent))

add_offsuit_cards_percents(offsuit_cards_in_percent, matrix)
add_pair_cards(pair_cards_in_percent, matrix)
add_suit_cards_percents(suit_cards_in_percent, matrix)
show_matrix(matrix)
