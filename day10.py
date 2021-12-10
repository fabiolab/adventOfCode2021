MISFORMATED_SCORE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

UNCOMPLETED_SCORE = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

MISFORMATED = ['(]', '(}', '(>', '{)', '{]', '{>', '[)', '[}', '[>', '<)', '<}', '<]']
PAIRS = ['()', '{}', '[]', '<>']

if __name__ == "__main__":
    FILEPATH = "data/data_10.txt"

    with open(FILEPATH, 'r') as fp:
        DATA = [line.strip() for line in fp.readlines()]

    # Star 1
    uncompleted = []
    score = 0
    for code in DATA:
        # Loop to remove all pairs. It remains misformated pairs.
        while True:
            if any(pair in code for pair in PAIRS):
                for pair in PAIRS:
                    code = code.replace(pair, '')
            else:
                break
        code_score = sum([MISFORMATED_SCORE[mis[1]] for mis in MISFORMATED if mis in code])
        score += code_score
        if code and not code_score:
            uncompleted.append(code)
    print(score)

    # Star 2
    scores = []
    for code in uncompleted:
        score = 0
        for char in reversed(code):
            score = score * 5 + UNCOMPLETED_SCORE[char]
        scores.append(score)
    print(sorted(scores)[int(len(scores) / 2):int(len(scores) / 2) + 1][0])
