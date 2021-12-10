from typing import Dict, Iterator, NewType, Tuple

FILEPATH = "data/data_05.txt"
OverlapedPoints = NewType('OverlapedPoints', Dict[Tuple[int, int], int])


def read_lines(filepath: str) -> Iterator:
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            start, end = line.split(' -> ')
            x1, y1 = [int(i) for i in start.split(',')]
            x2, y2 = [int(i) for i in end.split(',')]
            yield x1, y1, x2, y2


def add_points(matrix: OverlapedPoints, x1: int, y1: int, x2: int, y2: int) -> OverlapedPoints:
    if x1 != x2 and y1 == y2:
        for iter_x in range(min(x1, x2), max(x1, x2) + 1):
            matrix[(iter_x, y1)] = matrix.get((iter_x, y1), 0) + 1
    elif y1 != y2 and x1 == x2:
        for iter_y in range(min(y1, y2), max(y1, y2) + 1):
            matrix[(x1, iter_y)] = matrix.get((x1, iter_y), 0) + 1
    else:
        # Deals with diagonals for star 2
        x_range = list(range(min(x1, x2), max(x1, x2) + 1))
        y_range = list(range(min(y1, y2), max(y1, y2) + 1))
        if x1 > x2:
            x_range.reverse()
        if y1 > y2:
            y_range.reverse()
        for (x, y) in zip(x_range, y_range):
            matrix[(x, y)] = matrix.get((x, y), 0) + 1
    return matrix


if __name__ == "__main__":
    overlap: OverlapedPoints = OverlapedPoints({})
    for points in read_lines(FILEPATH):
        overlap = add_points(overlap, *points)

    counter = len([item for item in overlap.values() if item >= 2])
    print(counter)
