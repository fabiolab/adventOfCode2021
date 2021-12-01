from typing import List

FILEPATH = "data/data_01.txt"


def get_increment(a_list: List[int]) -> int:
    return len([x1 for x1, x2 in zip(a_list[::1], a_list[1::1]) if x2 > x1])


if __name__ == "__main__":
    numbers = [int(x) for x in open(FILEPATH, 'r')]

    # Star 1: 1583
    print(get_increment(numbers))

    # Star 2: 1627
    sum_by_3 = [sum(item) for item in zip(numbers[:], numbers[1:], numbers[2:])]
    print(get_increment(sum_by_3))
