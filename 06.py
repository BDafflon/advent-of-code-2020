with open("06.in") as f:
    groups = [x.strip() for x in f.read().split("\n\n")]

part1 = 0
part2 = 0
for group in groups:
    some_yes = None
    all_yes = None
    people = group.split("\n")
    for person in people:
        if some_yes is None:
            some_yes = set(person)
        else:
            some_yes |= set(person)
        if all_yes is None:
            all_yes = set(person)
        else:
            all_yes &= set(person)
    part1 += len(some_yes)
    part2 += len(all_yes)

print("Part 1:", part1)
print("Part 2:", part2)
