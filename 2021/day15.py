import numpy as np
import heapq


def get_neighbors(data, y, x):

    neighbors = []

    if x > 0:
        neighbors.append((y, x - 1))
    if y < data.shape[0] - 1:
        neighbors.append((y + 1, x))
    if x < data.shape[1] - 1:
        neighbors.append((y, x + 1))
    if y > 0:
        neighbors.append((y - 1, x))

    return neighbors


def dijkstra(data):

    dist = np.full(data.shape, np.inf)
    dist[0, 0] = 0

    prev = dict()
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            prev[(y, x)] = None

    unvisited = [(0, 0, 0)]

    while unvisited:

        _, u_y, u_x = heapq.heappop(unvisited)

        for n_y, n_x in get_neighbors(data, u_y, u_x):

            alt = dist[u_y, u_x] + data[n_y, n_x]
            if alt < dist[n_y, n_x]:
                dist[n_y, n_x] = alt
                prev[(n_y, n_x)] = (u_y, u_x)
                heapq.heappush(unvisited, (alt, n_y, n_x))

    lowest_risk = 0
    p_y, p_x = data.shape[0] - 1, data.shape[1] - 1
    while prev[p_y, p_x]:
        lowest_risk += data[p_y, p_x]
        p_y, p_x = prev[p_y, p_x]

    return lowest_risk


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [list(item.strip()) for item in data]
    data = np.array(data, dtype=int)

    modified_data = np.empty((data.shape[0]*5, data.shape[1]*5), dtype=int)
    for y in range(5):
        for x in range(5):
            s_y, s_x = data.shape[0], data.shape[1]
            n_data = data + y + x
            n_data[n_data >= 10] -= 9
            modified_data[y*s_y:y*s_y+s_y, x*s_x:x*s_x+s_x] = n_data

    print(f"Part One: {dijkstra(data)}")
    print(f"Part Two: {dijkstra(modified_data)}")


if __name__ == "__main__":
    main()
