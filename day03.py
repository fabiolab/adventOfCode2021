FILEPATH = "data/data_03.txt"

if __name__ == "__main__":
    # Star 1: 3687446
    POWER = [item for item in open(FILEPATH, 'r')]
    inverted = [item for item in zip(*POWER)]
    gama_rate = "".join([max(col, key=col.count) for col in inverted])
    epsilon_rate = "".join([min(col, key=col.count) for col in inverted])
    print(int(gama_rate, 2) * int(epsilon_rate, 2))

    # Star 2: 4406844
    oxygen_power = POWER
    for i in range(0, len(POWER[0])):
        inverted = [item for item in zip(*oxygen_power)]
        max_bit = max(sorted(inverted[i], reverse=True), key=inverted[i].count)
        oxygen_power = [item for item in oxygen_power if item[i] == max_bit]
    co2 = POWER
    for i in range(0, len(POWER[0])):
        inverted = [item for item in zip(*co2)]
        min_bit = min(sorted(inverted[i]), key=inverted[i].count)
        co2 = [item for item in co2 if item[i] == min_bit]
    print(int(oxygen_power[0], 2) * int(co2[0], 2))
