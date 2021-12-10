import statistics


def sum_integer(n: int) -> int:
    return sum([i for i in range(n + 1)])


if __name__ == "__main__":
    FILEPATH = "data/data_07.txt"
    with open(FILEPATH, 'r') as fp:
        DATA = [int(i.strip()) for i in fp.readline().split(',')]

    # Star 1
    print(sum([abs(statistics.median(sorted(DATA)) - i) for i in DATA]))

    # Star 2
    # A bit long but works ...
    print(min([sum([sum_integer(abs(pos - i)) for pos in DATA]) for i in range(min(DATA), max(DATA)) for pos in DATA]))
    #
    # for i in range(min(DATA), max(DATA)):
    #     moves = [sum_integer(abs(pos - i)) for pos in DATA]
    #     print(i, sum(moves))
