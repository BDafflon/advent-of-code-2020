from functools import reduce
from operator import mul

with open("03.in") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


def find_trees(right, down=1, slope=lines):
    width = len(slope[0])
    trees = 0
    for n, line in enumerate(slope[::down]):
        if line[(n * right) % width] == "#":
            trees += 1
    return trees


print("Part 1")
print(find_trees(3))

patterns = [(1,), (3,), (5,), (7,), (1, 2)]
found_trees = [find_trees(*x) for x in patterns]
print("Part 2")
print(reduce(mul, found_trees, 1))