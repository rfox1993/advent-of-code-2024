import numpy as np
import pandas as pd

# part one


def is_safe(lvls: pd.Series) -> bool:
    """Check is set of levels is safe or not."""

    inc_or_dec = lvls.is_monotonic_decreasing or lvls.is_monotonic_increasing

    # smallest / biggest change
    min_change = np.abs(lvls - lvls.shift()).min()
    max_change = np.abs(lvls - lvls.shift()).max()

    return inc_or_dec and min_change >= 1 and max_change <= 3


# how many reports are safe?
safe_reports = 0

with open("day_two.txt", "r") as file:
    for line in file:
        nums = line.split()
        ser = pd.Series(nums, dtype=int)
        if is_safe(ser):
            safe_reports += 1

print(safe_reports)
# 463

# part two


def can_be_made_safe(lvls: pd.Series) -> bool:
    """Check of set of levels could be made safe by removing a level."""

    would_be_safe = 0

    for i in lvls.index:
        less_one = lvls.loc[~lvls.index.isin([i])]
        if is_safe(less_one):
            would_be_safe += 1

    return would_be_safe > 0


# how many reports are safe or could be made safe by removing a level?
could_be_safe_reports = 0

with open("day_two.txt", "r") as file:
    for line in file:
        nums = line.split()
        ser = pd.Series(nums, dtype=int)
        if is_safe(ser) or can_be_made_safe(ser):
            could_be_safe_reports += 1

print(could_be_safe_reports)
# 514
