from typing import List, Tuple
from tile import Tile


class PNode:
    """A node class used for the astar algorithm"""

    def __init__(self, pos: Tuple[int, int], p=None):
        self.parent = p
        self.pos = pos

        # Variables used for balancing/heuristics
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other) -> bool:
        return self.pos == other.pos

    def __hash__(self) -> int:
        return self.pos.__hash__()


def a_star(board: List[List[Tile]],
           start: Tuple[int, int],
           end: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Perform the a_star algorithm and return the resultant path. Based
    on the psuedocode from
    https://en.wikipedia.org/wiki/A*_search_algorithm"""
    # Initialize variables
    open_list = []
    closed_children = set()
    start_node = PNode(start)
    end_node = PNode(end)

    # Start the algorithm with the start node
    open_list.append(start_node)
    while len(open_list) > 0:
        node = open_list[0]
        index = 0

        # Find smallest f value and its index
        for i in range(len(open_list)):
            if open_list[i].f < node.f:
                index = i
                node = open_list[i]

        # Remove the index from the open list and add the node to
        # the closed list
        open_list.pop(index)
        closed_children.add(node)

        # End logic: if our node is our end node, we've won! Return the path.
        if node == end_node:
            path = []
            while node:
                path.append(node.pos)
                node = node.parent
            return path[::-1]

        # Get all valid neighbors (i.e., a neighbor of the agent_model index
        # that is not None)
        neighbors = []
        for v in get_valid_neighbor_indexes(node.pos, len(board)):
            if not board[v[0]][v[1]].is_wall and \
                    board[v[0]][v[1]].agent is None:
                neighbors.append(PNode(v, node))

        # Loop through neighbors
        for neighbor in neighbors:

            # If the current node is closed, continue
            if neighbor in closed_children:
                continue

            # Balance the moves
            # TODO: Optimise heuristic
            neighbor.g = node.g + 1
            neighbor.h = ((neighbor.pos[0] - end_node.pos[0])
                          ** 2) + ((neighbor.pos[1] - end_node.pos[1]) ** 2)
            neighbor.f = neighbor.g + neighbor.h

            # If the neighbor is on the open list, ignore it
            if check_open_list(neighbor, open_list):
                continue

            # Add the neighbor to the open list
            open_list.append(neighbor)

    # Should never get here, but throw an error if so
    raise ValueError


def get_valid_neighbor_indexes(pos: Tuple[int, int],
                               board_width: int) -> List[Tuple[int, int]]:
    neighbor_indexes = []
    i = pos[0]
    j = pos[1]
    # Logic to attach tiles
    # If "not on north side, has north neighbor" = greater than 4
    # If "not on south side, has south neighbor" = less than 20
    # If "not on west side, has west neighbor" = mod 5 != 0
    # If "not on east side, has east neighbor" = mod (4 + 1) != 0

    if j - 1 >= 0:
        neighbor_indexes.append((i, j - 1))
    if j + 1 < board_width:
        neighbor_indexes.append((i, j + 1))
    if i + 1 < board_width:
        neighbor_indexes.append((i + 1, j))
    if i - 1 >= 0:
        neighbor_indexes.append((i - 1, j))

    return neighbor_indexes


def check_open_list(node: PNode, open_list: List[PNode]) -> bool:
    """
    Checks to see if a node exists in the open list
    Args:
        node: The node to check the open list for
        open_list: The open list

    Returns: True if the node is in the open list
    """
    for open_node in open_list:
        if node == open_node and node.g > open_node.g:
            return True
    return False
