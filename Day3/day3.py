

def list_diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))


def day3_1(file):
    one_counter = [0 for _ in range(12)]
    zero_counter = [0 for _ in range(12)]
    with open(file, 'r') as file:
        for line in file:
            line = line.strip()
            for i, bit in enumerate(line):
                if bit == '1':
                    one_counter[i] += 1
                else:
                    zero_counter[i] += 1
    gamma_rate = '0b'
    epsilon_rate = '0b'
    for ones, zeros in zip(one_counter, zero_counter):
        gamma_rate += '1' if ones > zeros else '0'
        epsilon_rate += '1' if ones < zeros else '0'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def day3_2(file):
    data = []
    with open(file, 'r') as file:
        for line in file:
            line = line.strip()
            data.append(line)

    oxygen_rating = data.copy()
    co2_rating = data.copy()

    for i in range(12):
        ox_one_counter = 0
        ox_zero_counter = 0
        co_one_counter = 0
        co_zero_counter = 0
        for record in oxygen_rating:
            if record[i] == '1':
                ox_one_counter += 1
            else:
                ox_zero_counter += 1
        for record in co2_rating:
            if record[i] == '1':
                co_one_counter += 1
            else:
                co_zero_counter += 1
        if ox_one_counter >= ox_zero_counter and len(oxygen_rating) > 1:
            oxygen_rating = [record for record in oxygen_rating if record[i] == '1']
        elif len(oxygen_rating) > 1:
            oxygen_rating = [record for record in oxygen_rating if record[i] == '0']

        if co_one_counter >= co_zero_counter and len(co2_rating) > 1:
            co2_rating = [record for record in co2_rating if record[i] != '1']
        elif len(co2_rating) > 1:
            co2_rating = [record for record in co2_rating if record[i] == '1']

        if len(oxygen_rating) == len(co2_rating) == 1:
            break

    return int(oxygen_rating[0], 2) * int(co2_rating[0], 2)


if __name__ == '__main__':
    print(day3_1('input1.txt'))
