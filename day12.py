if __name__ == "__main__":
    FILEPATH = "data/data_11.txt"

    with open(FILEPATH, 'r') as fp:
        DATA = [line.strip() for line in fp.readlines()]
