def read_file_to_list(file):
    with open(file, 'r') as fh:
        directions = []
        for line in fh.readlines():
            directions.append(line)
        return directions


def dive(directions):
    coordinate = [0, 0]
    for direction in directions:
        steering, amount = direction.split()
        if steering == "forward":
            coordinate[0] += int(amount)
        elif steering == "down":
            coordinate[1] += int(amount)
        elif steering == "up":
            coordinate[1] -= int(amount)
    print(coordinate)
    print(coordinate[0] * coordinate[1])


def start_here():
    # filename = "test_input"
    filename = "puzzle_input"
    dive(read_file_to_list(filename))


if __name__ == '__main__':
    start_here()
