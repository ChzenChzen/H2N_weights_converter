def h2n_text_parser(filename):
    """parses text from file"""
    weights = [[int(weight) for weight in line.split()] for line in open(filename)]  # create hand matrix from file
    return weights


def convert_into_percents():
    """converts weights of raw h2n into percents"""
    pass


def convert_into_crev_format():
    """rounds weights of percents  into crev format(5 weights)"""
    pass


def write_crev_format_in_excel():
    """writes crev weighted data in excel's table for handy usage"""
    pass


print(h2n_text_parser("input.txt"))


