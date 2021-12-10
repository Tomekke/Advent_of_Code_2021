def read_file_to_list(file):
    with open(file, 'r') as fh:
        numbers = []
        for line in fh.readlines():
            numbers.append(int(line))
        return numbers


def count_numbers(numbers):
    increase_counter = 0
    for index in range(1, len(numbers)):
        increase_counter = increase_counter+1 if numbers[index] - numbers[index - 1] > 0 else increase_counter+0
    return increase_counter


def start_here():
    # filename = "Test_file"
    filename = "puzzle_input"
    print(count_numbers(read_file_to_list(filename)))


if __name__ == '__main__':
    start_here()