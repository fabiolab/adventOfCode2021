FILEPATH = "data/data_02.txt"

if __name__ == "__main__":
    COMMANDS = {
        "forward": lambda x, depth, val, aim: (x + val, depth + aim * val, aim),
        "up": lambda x, depth, val, aim: (x, depth, aim - val),
        "down": lambda x, depth, val, aim: (x, depth, aim + val)
    }

    current_x, current_depth, current_aim = 0, 0, 0

    for command, value in [item.split() for item in open(FILEPATH, 'r')]:
        current_x, current_depth, current_aim = COMMANDS[command](current_x, current_depth, int(value), current_aim)

    print(current_x * current_depth)
