import numpy as np
import collections


def read_file(file):
    data = np.genfromtxt(file, delimiter=',', dtype=int)
    return data


def day6_1(data_set):
    for _ in range(256):
        data_set = data_set - 1
        parents = collections.Counter(data_set)
        children = [8 for _ in range(parents[-1])]
        data_set = np.where(data_set == -1, 6, data_set)
        data_set = np.append(data_set, children)

    return data_set.size


def day6_2(data_set):
    fishes = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    counter = collections.Counter(data_set)
    for key in counter.keys():
        fishes[key] = counter[key]
    tmp_dict = fishes.copy()
    for _ in range(256):
        tmp_num = 0
        for key, number in fishes.items():
            if key == 0:
                tmp_dict[8] = number
                tmp_num = number
            elif key == 7:
                tmp_dict[key - 1] = number + tmp_num
            else:
                tmp_dict[key - 1] = number
        fishes = tmp_dict.copy()
    fish_sum = 0
    for fish in fishes.values():
        fish_sum += fish

    return fish_sum


if __name__ == '__main__':
    data = read_file('input.txt')
    print(day6_2(data))
