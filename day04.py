from typing import Dict, List

FILEPATH = "data/data_04.txt"
NUMBERS = "62,55,98,93,48,28,82,78,19,96,31,42,76,25,34,4,18,80,66,6,14,17,57,54,90,27,40,47,9,36,97,56,87,61,91,1," \
          "64,71,99,38,70,5,94,85,49,59,69,26,21,60,0,79,2,95,11,84,20,24,8,51,46,44,88,22,16,53,7,32,89,67,15,86,41," \
          "92,10,77,68,63,43,75,33,30,81,37,83,3,39,65,12,45,23,73,72,29,52,58,35,50,13,74"

'''
Base idea: getting an inverted index where we can access all the grids containing a given number. From a number you get
all the grids that contain it and the col and row number matching its location in the grid.
Each time we get a number, we update a score dictionnary for all the grids. Once a row or a line is completed, the grid
has won.
'''


def read_grids(filepath: str) -> List:
    with open(filepath, 'r') as fp:
        return [[[int(i) for i in line.split()] for line in grid.strip().split('\n')] for grid in
                fp.read().split('\n\n')]


def read_indexed_nums(filepath: str) -> Dict:
    with open(filepath, 'r') as fp:
        dictionnary: Dict = dict()
        current_grid = 0
        current_line = 0
        for x in fp:
            if x != '\n':
                line = x.strip().split()
                for index, num in enumerate(line):
                    try:
                        dictionnary[num].append({'grid_id': current_grid, 'row': current_line, 'col': index})
                    except KeyError:
                        dictionnary[num] = [{'grid_id': current_grid, 'row': current_line, 'col': index}]
                current_line += 1
            else:
                current_line = 0
                current_grid += 1
        return dictionnary


def is_grid_completed(grid_score: Dict) -> bool:
    return 5 in grid_score['rows'] or 5 in grid_score['cols']


if __name__ == "__main__":
    indexed_nums = read_indexed_nums(FILEPATH)
    grids = read_grids(FILEPATH)
    scores = {grid_id: {'rows': [0] * 5, 'cols': [0] * 5, 'checked': 0} for grid_id in range(0, len(grids))}
    completed_grids = []

    # Get the numbers by order
    for num in NUMBERS.split(','):

        # Get all the grid that contain the number
        for num_in_grid in indexed_nums.get(num):
            # increment score for the grid containing num for the matching row/col
            scores[num_in_grid['grid_id']]['rows'][num_in_grid['row']] += 1
            scores[num_in_grid['grid_id']]['cols'][num_in_grid['col']] += 1
            scores[num_in_grid['grid_id']]['checked'] += int(num)

            if is_grid_completed(scores[num_in_grid['grid_id']]):
                winning_num = int(num)
                grid_sum = sum([sum(sublist) for sublist in grids[num_in_grid['grid_id']]])
                checked_nums_sum = scores[num_in_grid['grid_id']]['checked']
                score = winning_num * (grid_sum - checked_nums_sum)

                if num_in_grid['grid_id'] not in completed_grids:
                    completed_grids.append(num_in_grid['grid_id'])
                    print(f"board {num_in_grid['grid_id']} won with {num} and score {score}")
                    # exit(0)
