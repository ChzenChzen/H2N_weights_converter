def h2n_text_parser(filename):
    """parses text from file"""
    weights = [[int(weight) for weight in line.split()] for line in open(filename)]  # create hand matrix from file
    return weights


def max_offsuit(cards_matrix):
    """get max value from offsuit cards"""
    for cards_matrix_line in cards_matrix[1:]:
        line_number = 0
        for card_weight in cards_matrix_line[:line_number]:
            line_number += 1
            print(card_weight)


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

max_offsuit(weights)
