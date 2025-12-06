import os
from typing import List, Tuple
from utils.file_util import FileUtil


def init_grid(inputs: List[str]) -> List[List[str]]:
    grid = []

    for input in inputs:
        grid.append(list(input))

    return grid


def tp_access_search(grid: List[List[str]], starting_point: Tuple[int, int], key: str = "@") -> bool:
    """
    The forklifts can only access a roll of paper (@) if there are fewer than 4 rolls of paper in the eight adjacent positions.
    If you can figure out which rolls of paper the forklifts can access,
    they'll spend less time looking and more time breaking down the wall to the cafeteria.
    """
    row_index = starting_point[0]
    col_index = starting_point[1]
    tp_counter = 0

    if grid[row_index][col_index] != key:
        return 0

    # Search up
    if row_index > 0:
        word = grid[row_index - 1][col_index]
        if word == key:
            tp_counter += 1

    # Search down
    if row_index < len(grid) - 1:
        word = grid[row_index + 1][col_index]
        if word == key:
            tp_counter += 1

    # Search left
    if col_index > 0:
        word = grid[row_index][col_index - 1]
        if word == key:
            tp_counter += 1

    # Search right
    if col_index < len(grid[0]) - 1:
        word = grid[row_index][col_index + 1]
        if word == key:
            tp_counter += 1

    if tp_counter >= 4:
        return False

    # Search diagonal (up-left)
    if row_index > 0 and col_index > 0:
        word = grid[row_index - 1][col_index - 1]
        if word == key:
            tp_counter += 1

    if tp_counter >= 4:
        return False

    # Search diagonal (up-right)
    if row_index > 0 and col_index < len(grid[0]) - 1:
        word = grid[row_index - 1][col_index + 1]
        if word == key:
            tp_counter += 1

    if tp_counter >= 4:
        return False

    # Search diagonal (down-right)
    if row_index < len(grid) - 1 and col_index < len(grid[0]) - 1:
        word = grid[row_index + 1][col_index + 1]
        if word == key:
            tp_counter += 1

    if tp_counter >= 4:
        return False

    # Search diagonal (down-left)
    if row_index < len(grid) - 1 and col_index > 0:
        word = grid[row_index + 1][col_index - 1]
        if word == key:
            tp_counter += 1

    return False if tp_counter >= 4 else True


def find_accessible_tps(grid: List[List[str]], key: str = "@") -> tuple[int, list[tuple[int, int]]]:
    # P1
    # loop through the grid and check for the pattern "@"
    # This is up, down, left, right, and diagonals
    p1_answer = 0
    removal_tp_list = []
    for row_idx in range(len(grid)):
        for col_index in range(len(grid[0])):
            can_access = tp_access_search(grid, (row_idx, col_index))
            p1_answer += 1 if can_access else 0

            if can_access:
                #print(f"accessible '@' found at {row_idx},{col_index}")
                removal_tp_list.append((row_idx, col_index))

    return p1_answer, removal_tp_list

# Program start
inputs = FileUtil.read_file("./inputs/day4.input.txt")
grid = init_grid(inputs)

p1_answer = 0
(p1_answer, _) = find_accessible_tps(grid)
print(f"P1 answer - {p1_answer}")

p2_answer = 0
while True:
    (_, temp_list) = find_accessible_tps(grid)

    p2_answer += len(temp_list)
    for item in temp_list:
        grid[item[0]][item[1]] = "."

    if len(temp_list) == 0:
        break

print(f"P2 answer - {p2_answer}")