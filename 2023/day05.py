import copy


def getLowestNum(seeds, maps):

    for seed in seeds.keys():

        for map_ in maps.values():

            currentVal = seeds[seed][-1]

            mapUseful = False
            for line in map_:

                dest, src, len_ = line

                if currentVal in range(src, src + len_ + 1):
                    seeds[seed].append(dest + (currentVal - src))
                    mapUseful = True
                    break

            if not mapUseful:
                seeds[seed].append(currentVal)

    lowest_num = float("inf")
    for list_ in seeds.values():
        num = list_[-1]
        if num < lowest_num:
            lowest_num = num

    return lowest_num


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [item.strip() for item in data]

    seeds = dict()
    for seed in data[0].split(": ")[1].split(" "):
        seeds[seed] = [int(seed)]

    maps, currentMap = dict(), ""
    for line in data[2:]:

        if currentMap == "":
            currentMap = line[:-1]
            maps[currentMap] = []
            continue

        if line == "":
            currentMap = ""
            continue

        maps[currentMap].append([int(item) for item in line.split(" ")])

    print(f"Part One: {getLowestNum(copy.deepcopy(seeds), copy.deepcopy(maps))}")  # noqa: E501


if __name__ == "__main__":
    main()
