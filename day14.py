from math import floor
from typing import Dict

FILEPATH = "data/data_14.txt"


def count_pairs(counter: Dict) -> Dict:
    new_counter = counter.copy()
    # All the existing pairs disapear as they are split while applying the rules
    for pair in counter.keys():
        new_counter[pair] = 0
    # Increment the pair counter: from a given pair, two new pairs are generated
    for pair, nb_pair in counter.items():
        new_counter[f"{pair[0]}{PAIR_INSERTION[pair]}"] = new_counter.get(f"{pair[0]}{PAIR_INSERTION[pair]}",
                                                                          0) + nb_pair
        new_counter[f"{PAIR_INSERTION[pair]}{pair[1]}"] = new_counter.get(f"{PAIR_INSERTION[pair]}{pair[1]}",
                                                                          0) + nb_pair
    return new_counter


if __name__ == "__main__":
    input_template = "HHKONSOSONSVOFCSCNBC"

    # Init the "pair" counter with the initial sentence
    pair_counter = {}
    for a_pair in zip(input_template, input_template[1:]):
        pair_counter["".join(a_pair)] = pair_counter.get("".join(a_pair), 0) + 1

    with open(FILEPATH, 'r') as fp:
        PAIR_INSERTION = {line.strip().split(' -> ')[0]: line.strip().split(' -> ')[1] for line in fp.readlines()}

    for i in range(40):
        pair_counter = count_pairs(pair_counter)

    # Count chars from pairs
    char_counter = {}
    for pair in pair_counter.keys():
        char_counter[pair[0]] = char_counter.get(pair[0], 0) + pair_counter[pair]
        char_counter[pair[1]] = char_counter.get(pair[1], 0) + pair_counter[pair]

    print(floor(char_counter[max(char_counter, key=char_counter.get)] / 2) - floor(
        char_counter[min(char_counter, key=char_counter.get)] / 2) - 1)
