from typing import Dict, List


def guess_number(encoding: Dict[int, List[str]], encoded: str) -> int:
    match len(encoded):
        case 2:
            return 1
        case 3:
            return 7
        case 4:
            return 4
        case 7:
            return 8
        case 6:
            if len(set(encoding[4]).union(encoded)) == 6:
                return 9
            if len(set(encoding[2]).union(encoded)) == 7:
                return 6
            return 0
        case 5:
            if len(set(encoding[2]).union(encoded)) == 5:
                return 3
            if len(set(encoding[4]).union(encoded)) == 7:
                return 2
            return 5


if __name__ == "__main__":
    FILEPATH = "data/data_08.txt"

    # Star 1
    with open(FILEPATH, 'r') as fp:
        DATA = [len(item) for line in fp.readlines() for item in line.split('|')[1].strip().split()]

    res = [item for item in DATA if item in [7, 4, 3, 2]]
    print(len([item for item in DATA if item in [7, 4, 3, 2]]))

    # Star 2
    with open(FILEPATH, 'r') as fp:
        DATA = [line.strip() for line in fp.readlines()]

    total = 0
    for line in DATA:
        digits, code = line.split('|')
        encoding = {len(d): d for d in digits.split()}
        val = int("".join([str(guess_number(encoding, num)) for num in code.split()]))
        total += val
    print(total)
