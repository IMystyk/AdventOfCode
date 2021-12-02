
def day2_1(file):
    horizontal = 0
    vertical = 0
    with open(file, 'r') as file:
        for line in file:
            data = line.split()
            if data[0] == 'forward':
                horizontal += int(data[1])
            elif data[0] == 'up':
                vertical += int(data[1])
            elif data[0] == 'down':
                vertical -= int(data[1])
    return horizontal * abs(vertical)  # absolute, because of depth


def day2_2(file):
    horizontal = 0
    vertical = 0
    aim = 0
    with open(file, 'r') as file:
        for line in file:
            data = line.split()
            if data[0] == 'forward':
                horizontal += int(data[1])
                vertical += aim * int(data[1])
            elif data[0] == 'up':
                aim += int(data[1])
            elif data[0] == 'down':
                aim -= int(data[1])
    return horizontal * abs(vertical)  # absolute, because of depth
