from typing import List, Tuple


def fold_matrix_by_height(matrix: List[List[bool]], row: int):
    return [[x1 or x2 for x1, x2 in zip(matrix[i], matrix[-1 - i])] for i in range(row)]


def fold_matrix_by_width(matrix: List[List[bool]], col: int):
    return [[y1 or y2 for y1, y2 in zip(line[0:col], reversed(line[col:]))] for line in matrix]


def display_area(area: List[List[bool]]):
    for y in area:
        print("".join(['#' if x else '.' for x in y]))


def read_instructions(filepath: str) -> List[Tuple[str, int]]:
    with open(filepath, 'r') as fp:
        instructions_raw = [line.strip() for line in fp.readlines()]

        instructions_builder: List[Tuple[str, int]] = []
        for line in instructions_raw:
            if line and "fold" in line:
                instructions_builder.append((line.split('=')[0][-1], int(line.split('=')[1]),))
        return instructions_builder


def read_positions(filepath: str) -> List[List[bool]]:
    with open(filepath, 'r') as fp:
        positions_raw = [line.strip() for line in fp.readlines()]

        positions_builder: List[List[bool]] = [[False] * COLS for i in range(ROWS)]
        for line in positions_raw:
            if line and "fold" not in line:
                positions_builder[int(line.split(',')[1])][int(line.split(',')[0])] = True
        return positions_builder


# Hard coded matrix size
COLS = 655 * 2 + 1
ROWS = 447 * 2 + 1

FILEPATH = "data/data_13.txt"

if __name__ == "__main__":

    instructions = read_instructions(FILEPATH)
    positions = read_positions(FILEPATH)

    for direction, value in instructions:
        match direction:
            case 'y':
                fold = fold_matrix_by_height(positions, value)
            case 'x':
                positions = fold_matrix_by_width(positions, value)
        print(len([col for row in positions for col in row if col]))
        display_area(positions)
