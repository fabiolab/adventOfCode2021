from typing import List, Tuple


def fold_matrix_by_height(matrix: List[List[bool]], row: int):
    return [[x1 or x2 for x1, x2 in zip(matrix[i], matrix[-1 - i])] for i in range(row)]


def fold_matrix_by_width(matrix: List[List[bool]], col: int):
    return [[y1 or y2 for y1, y2 in zip(line[0:col], reversed(line[col:]))] for line in matrix]


def display_area(area: List[List[bool]]):
    for y in area:
        print("".join(['#' if x else '.' for x in y]))


# COLS = 11
# ROWS = 15
COLS = 655 * 2 + 1
ROWS = 447 * 2 + 1

if __name__ == "__main__":
    FILEPATH = "data/data_13.txt"

    with open(FILEPATH, 'r') as fp:
        DATA = [line.strip() for line in fp.readlines()]

    fold: List[List[bool]] = [[False] * COLS for i in range(ROWS)]
    instructions: List[Tuple[str, int]] = []
    for line in DATA:
        if not line:
            continue
        if "fold" in line:
            instructions.append((line.split('=')[0][-1], int(line.split('=')[1]),))
        else:
            fold[int(line.split(',')[1])][int(line.split(',')[0])] = True

    for direction, value in instructions:
        match direction:
            case 'y':
                fold = fold_matrix_by_height(fold, value)
            case 'x':
                fold = fold_matrix_by_width(fold, value)
        print(len([col for row in fold for col in row if col]))
        display_area(fold)
