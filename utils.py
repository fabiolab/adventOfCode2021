def read_file_as_integer(filepath: str) -> list:
    with open(filepath, 'r') as fp:
        return [int(x) for x in fp]
