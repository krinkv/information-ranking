def read_file_lines(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file]


def read_testing_data(path):
    testing_dict = {}
    lines = read_file_lines(path)

    for line in lines:
        correct_to_mistakes = line.split(':')
        correct = correct_to_mistakes[0]
        mistakes = correct_to_mistakes[1].split()

        for mistake in mistakes:
            testing_dict[mistake.lower()] = correct.lower()

    return testing_dict
