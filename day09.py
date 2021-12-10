from typing import List, Set

FILEPATH = "data/data_09.txt"

with open(FILEPATH, 'r') as fp:
    DATA = [[int(val) for val in line.strip()] for line in fp.readlines()]


def get_neighbors(area: List[List[int]], row_pos: int, col_pos: int) -> List[int]:
    previous_row = max(0, row_pos - 1)
    previous_col = max(0, col_pos - 1)
    next_row = min(row_pos + 1, len(area) - 1)
    next_col = min(col_pos + 1, len(area[0]) - 1)

    return [item for a_row in area[previous_row:next_row + 1] for item in
            a_row[previous_col:next_col + 1]]


def get_horizonal_flow(area: List[List[int]], row_pos: int, col_pos: int) -> Set:
    current_basin: List[(int, int, int)] = []
    index = col_pos
    # Rightside search
    while True:
        if index - len(area[0]) + 1 and 9 > area[row_pos][index + 1] > area[row_pos][index]:
            current_basin.append((row_pos, index + 1, area[row_pos][index + 1]))
            current_basin += get_horizonal_flow(area, row_pos, index + 1)
            current_basin += get_vertical_flow(area, row_pos, index + 1)
            index += 1
        else:
            break

    index = col_pos
    # Leftside search
    while True:
        if index and 9 > area[row_pos][index - 1] > area[row_pos][index]:
            current_basin.append((row_pos, index - 1, area[row_pos][index - 1]))
            current_basin += get_horizonal_flow(area, row_pos, index - 1)
            current_basin += get_vertical_flow(area, row_pos, index - 1)
            index -= 1
        else:
            break

    return set(current_basin)


def get_vertical_flow(area: List[List[int]], row_pos: int, col_pos: int) -> Set:
    current_basin: List[(int, int, int)] = []
    index = row_pos
    # Downside search
    while True:
        if index - len(area) + 1 and 9 > area[index + 1][col_pos] > area[index][col_pos]:
            current_basin.append((index + 1, col_pos, area[index + 1][col_pos]))
            current_basin += get_horizonal_flow(area, index + 1, col_pos)
            current_basin += get_vertical_flow(area, index + 1, col_pos)
            index += 1
        else:
            break

    index = row_pos
    # upside search
    while True:
        if index and 9 > area[index - 1][col_pos] > area[index][col_pos]:
            current_basin.append((index - 1, col_pos, area[index - 1][col_pos]))
            current_basin += get_horizonal_flow(area, index - 1, col_pos)
            current_basin += get_vertical_flow(area, index - 1, col_pos)
            index -= 1
        else:
            break

    return set(current_basin)


def get_basin(area: List[List[int]], row_pos: int, col_pos: int) -> Set:
    return get_vertical_flow(area, row_pos, col_pos).union(get_horizonal_flow(area, row_pos, col_pos))


if __name__ == "__main__":
    lowest_points = []
    basins = []
    for row_idx, row in enumerate(DATA):
        for col_idx, col in enumerate(row):
            neighbors = get_neighbors(DATA, row_idx, col_idx)
            if DATA[row_idx][col_idx] <= min(neighbors):
                lowest_points.append(DATA[row_idx][col_idx] + 1)
                basin = get_basin(DATA, row_idx, col_idx).union({(row_idx, col_idx, DATA[row_idx][col_idx])})
                basins.append(basin)
    print(sum(lowest_points))

    basins = sorted(basins, key=len, reverse=True)
    print(len(basins[0]) * len(basins[1]) * len(basins[2]))
