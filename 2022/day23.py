# WARNING: This implementation is rather slow (1-2 minutes) and inefficient.

import numpy as np


def extend_map(map_):

    # Add a layer of empty ground around the map.
    map_ = np.pad(map_, 1)
    map_[map_ == "0"] = "."

    return map_


def remove_edges(map_):

    to_delete = []

    for j in range(map_.shape[0]):
        if np.all(map_[j, :] == "."):
            to_delete.append(j)
            continue
        break

    for j in range(map_.shape[0])[::-1]:
        if np.all(map_[j, :] == "."):
            to_delete.append(j)
            continue
        break

    map_ = np.delete(map_, to_delete, 0)

    to_delete = []

    for i in range(map_.shape[1]):
        if np.all(map_[:, i] == "."):
            to_delete.append(i)
            continue
        break

    for i in range(map_.shape[1])[::-1]:
        if np.all(map_[:, i] == "."):
            to_delete.append(i)
            continue
        break

    map_ = np.delete(map_, to_delete, 1)

    return map_


def check_edges(map_):

    # Check if at least one elf is on any of the edges.
    if np.any(np.where(map_[0, :] == "#")):
        return True
    if np.any(np.where(map_[-1, :] == "#")):
        return True
    if np.any(np.where(map_[:, 0] == "#")):
        return True
    if np.any(np.where(map_[:, -1] == "#")):
        return True

    return False


def get_neighbors(map_, j, i):

    # Define all adjacent neighbor indices.
    neighbors_ind = [
        (j-1, i-1),
        (j-1, i),
        (j-1, i+1),
        (j, i-1),
        (j, i+1),
        (j+1, i-1),
        (j+1, i),
        (j+1, i+1)
    ]

    # Initialize a little map for the neighbors.
    neighbors_map = np.zeros(9, dtype=str)
    neighbors_map[4] = "Y"

    # Fill in the neighbor map.
    for n, ind in zip([0, 1, 2, 3, 5, 6, 7, 8], neighbors_ind, ):
        neighbors_map[n] = map_[ind[0], ind[1]]

    # Make the map 2D.
    neighbors_map = neighbors_map.reshape((3, 3))

    # Store all neighbors based on the different directions.
    # [North, South, West, East]
    neighbors = np.array([
        neighbors_map[0, :],
        neighbors_map[-1, :],
        neighbors_map[:, 0],
        neighbors_map[:, -1],
    ])

    return neighbors


def sort_neighbors(neighbors, first_direction):

    # Sort the neighbors based on the first direction
    # that should be looked at.
    neighbors_sorted = np.concatenate(
        (neighbors[first_direction:], neighbors[:first_direction])
    )

    return neighbors_sorted


def at_least_one_neighbor(neighbors):

    for neighbor in neighbors:

        # Check if there is one neighbor.
        if np.any(neighbor == "#"):
            return True

    return False


def get_proposal(pos, first_direction, x):

    direction = (first_direction + x) % 4
    j, i = pos

    if direction == 0:
        return (j-1, i)
    if direction == 1:
        return (j+1, i)
    if direction == 2:
        return (j, i-1)
    if direction == 3:
        return (j, i+1)

    raise Exception("Unknown direction.")


def get_all_proposals(map_, first_direction, new_map):

    proposals = []
    originals = []

    for j in range(map_.shape[0]):
        for i in range(map_.shape[1]):

            # Skip empty ground.
            if map_[j, i] == ".":
                continue

            # Get neighbors.
            neighbors = get_neighbors(map_, j, i)

            # Sort the neighbors.
            neighbors = sort_neighbors(neighbors, first_direction)

            # Check if there is at least one neighbor.
            if not at_least_one_neighbor(neighbors):
                new_map[j, i] = "#"
                continue

            # Check every direction of neighbors.
            proposed = False
            for x, neighbor in enumerate(neighbors):

                if np.all(neighbor == "."):

                    # Propose movement.
                    proposal = get_proposal((j, i), first_direction, x)

                    # Store proposal and original position.
                    proposals.append(proposal)
                    originals.append((j, i))

                    proposed = True
                    break

            # Stay still if no direction is free.
            if not proposed:
                new_map[j, i] = "#"

    return proposals, originals, new_map


def part_one(map_):

    first_direction = 0

    # Simulate ten rounds.
    for _ in range(10):

        # Extend the map if any elf is on an edge.
        if check_edges(map_):
            map_ = extend_map(map_)

        # Create a copy of the map.
        new_map = np.zeros(map_.shape, dtype=str)
        new_map[:, :] = "."

        # Get all proposals.
        proposals, originals, new_map = get_all_proposals(
            map_, first_direction, new_map)

        # Rule out duplicates.
        for n, proposal in enumerate(proposals):

            if proposals.count(proposal) > 1:
                oj, oi = originals[n]
                new_map[oj, oi] = "#"
            else:
                pj, pi = proposal
                new_map[pj, pi] = "#"

        # Update the first direction proposal.
        first_direction = (first_direction + 1) % 4

        # Update the map.
        map_ = np.copy(new_map)

    # Remove empty edges.
    map_ = remove_edges(map_)

    return np.count_nonzero(map_ == ".")


def part_two(map_):

    first_direction = 0

    # Simulate ten rounds.
    round_ = 1
    while True:

        # Extend the map if any elf is on an edge.
        if check_edges(map_):
            map_ = extend_map(map_)

        # Create a copy of the map.
        new_map = np.zeros(map_.shape, dtype=str)
        new_map[:, :] = "."

        # Get all proposals.
        proposals, originals, new_map = get_all_proposals(
            map_, first_direction, new_map)

        # Rule out duplicates.
        for n, proposal in enumerate(proposals):

            if proposals.count(proposal) > 1:
                oj, oi = originals[n]
                new_map[oj, oi] = "#"
            else:
                pj, pi = proposal
                new_map[pj, pi] = "#"

        # Update the first direction proposal.
        first_direction = (first_direction + 1) % 4

        # Check if new map is equal to the old one.
        if np.array_equal(map_, new_map):
            break

        # Update the map.
        map_ = np.copy(new_map)

        round_ += 1

    return round_


def main():

    # Get the input data.
    with open("input.txt") as func:
        data = func.readlines()
    data = [item.strip() for item in data]

    # Transform data.
    data = [list(item) for item in data]
    data = np.array(data)

    # Solve part one.
    result1 = part_one(data)

    # Solve part two.
    result2 = part_two(data)

    # Print the results for the day.
    print(f"Part One: {result1}")
    print(f"Part Two: {result2}")


if __name__ == "__main__":
    main()
