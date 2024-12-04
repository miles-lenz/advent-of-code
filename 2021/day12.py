import copy as c


def search(data, curr_node, path, all_paths, visited, limit):

    if curr_node in visited.keys():

        cond1 = limit[1] and visited[curr_node] < 1
        cond2 = not limit[1] and visited[curr_node] < 2

        if cond1 or cond2:
            visited[curr_node] += 1
        else:
            return

        if visited[curr_node] == limit[0]:
            limit[1] = True

    path.append(curr_node)

    if curr_node == "end":
        all_paths.append(','.join(path))
        return

    for edge in data:

        node1, node2 = edge.split("-")

        if curr_node in [node1, node2]:

            c_path, c_visited = c.copy(path), c.copy(visited)
            c_limit = c.copy(limit)

            if node1 == curr_node and node2 != "start":
                search(data, node2, c_path, all_paths, c_visited, c_limit)

            elif node1 != curr_node and node1 != "start":
                search(data, node1, c_path, all_paths, c_visited, c_limit)


def main():

    with open("input.txt") as f:
        data = f.readlines()
    data = [item.strip() for item in data]

    nodes = set()
    for edge in data:
        nodes.add(edge.split("-")[0])
        nodes.add(edge.split("-")[1])
    nodes = list(nodes)

    visited = {}
    for node in nodes:
        if node not in ["start", "end"] and node.islower():
            visited[node] = 0

    all_paths1, all_paths2 = [], []
    search(data, "start", [], all_paths1, visited, [1, False])
    search(data, "start", [], all_paths2, visited, [2, False])

    print(f"Part One: {len(all_paths1)}")
    print(f"Part Two: {len(all_paths2)}")


if __name__ == "__main__":
    main()
