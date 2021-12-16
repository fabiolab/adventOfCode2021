import math
from heapq import heapify, heappop, heappush
from typing import List, NewType, Tuple

FILEPATH = "data/data_15.txt"
Node = NewType('Node', Tuple[int, int])


def get_neighbors(area: List[int], node: int, width: int) -> List[Tuple[int, int]]:
    neighbors = []
    if node >= width:
        neighbors.append((area[node - width], node - width))
    if node < width * width - width:
        neighbors.append((area[node + width], node + width))
    if node % width != width - 1:
        neighbors.append((area[node + 1], node + 1))
    if node % width != 0:
        neighbors.append((area[node - 1], node - 1))
    return neighbors


def update_visited(visited: List[Tuple[int, int]], node: Tuple[int, int]) -> List[Tuple[int, int]]:
    in_visited = [idx for idx, item in enumerate(visited) if item[1] == node[1]]

    if not in_visited:
        heappush(visited, node)
    else:
        visited[in_visited[0]] = node
        heapify(visited)
    return visited


def print_path(from_node: int, path: List[int], area: List[int]):
    node = from_node
    route = []
    while node:
        route.append(path[node])
        node = path[node]
    width = int(math.sqrt(len(area)))
    str_path = ""
    for i, idx in enumerate(area):
        if i in route:
            str_path += f'\033[92m{idx}\033[0m'
        else:
            str_path += str(idx)
        if i % width == width - 1:
            str_path += "\n"

    print(str_path)


def extend_cave(cave: List[List[int]], width: int) -> List[int]:
    the_big_cave = [0] * width * len(cave)

    for h in range(width):
        for idx, row in enumerate(cave):
            the_big_cave[idx + len(cave) * h] = [
                val + w + h if val + w + h <= 9 else val + w + h - 9 for w in
                range(width) for val in row]

    return [val for row in the_big_cave for val in row]


if __name__ == "__main__":
    with open(FILEPATH, 'r') as fp:
        CAVE = [int(val) for line in fp.readlines() for val in line.strip()]
    with open(FILEPATH, 'r') as fp:
        OTHER_CAVE = [[int(val) for val in line.strip()] for line in fp.readlines()]

    # For star 2, generate a big cave
    the_big_cave = extend_cave(OTHER_CAVE, 5)
    # print(the_big_cave)
    CAVE = the_big_cave
    width = int(math.sqrt(len(CAVE)))
    size = len(CAVE)
    neighbors = [get_neighbors(CAVE, index, width) for index in range(len(CAVE))]

    risks = [math.inf for i in range(len(neighbors))]
    path = [None for i in range(len(neighbors))]
    node = 0
    visited = [(0, node)]
    risks[node] = 0
    while node != size - 1:
        distance, node = heappop(visited)
        for risk, neighbor in neighbors[node]:
            total_risk = risks[node] + risk
            if total_risk < risks[neighbor]:
                risks[neighbor] = total_risk
                visited = update_visited(visited, (int(total_risk), neighbor))
                path[neighbor] = node
    print(risks[size - 1])
    print_path(size - 1, path, CAVE)
