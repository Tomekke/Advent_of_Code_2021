def read_file_to_list(file):
    with open(file, 'r') as fh:
        directions = []
        for line in fh.readlines():
            directions.append(line)
        return directions


def dive(directions):
    coordinate = [0, 0]
    aim = 0
    for direction in directions:
        steering, amount = direction.split()
        amount = int(amount)
        if steering == "forward":
            coordinate[0] += amount
            coordinate[1] += amount * aim
        elif steering == "down":
            aim += amount
        elif steering == "up":
            aim -= amount
    print(coordinate)
    print(coordinate[0] * coordinate[1])


def start_here():
    # filename = "test_input"
    filename = "puzzle_input"
    dive(read_file_to_list(filename))


if __name__ == '__main__':
    start_here()
