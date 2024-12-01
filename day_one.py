import numpy as np
import pandas as pd

# part one

eg_list_one = [3, 4, 2, 1, 3, 3]
eg_list_two = [4, 3, 5, 3, 9, 3]


def sort_and_compare(a: list, b: list) -> int:
    """Sort lists and sum pairwise differences."""

    a = np.sort(a)
    b = np.sort(b)

    diffs = np.abs(a - b)

    return np.sum(diffs)


print(sort_and_compare(eg_list_one, eg_list_two))
# 11

puzzle_input = pd.read_table(
    "day_one_lists.txt", sep="\s+", header=None, names=["list_one", "list_two"]
)

print(sort_and_compare(puzzle_input["list_one"], puzzle_input["list_two"]))
# 1,590,491

# part two

# count occurrences of left number in right list
puzzle_input["count"] = puzzle_input["list_one"].apply(
    lambda x: (puzzle_input["list_two"] == x).sum()
)

# multiply left number by right list occurences
puzzle_input["sim_score"] = puzzle_input["list_one"] * puzzle_input["count"]

print(puzzle_input["sim_score"].sum())
# 22,588,371
