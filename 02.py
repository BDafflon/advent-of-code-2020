part1 = 0
part2 = 0
for line in open("02.in").readlines():
    arr = line.split()
    lower, upper = (int(x) for x in arr[0].split("-"))
    pw = arr[-1]
    req = arr[1][0]
    x, y = pw[lower - 1], pw[upper - 1]
    occurrences = pw.count(req)
    if lower <= occurrences <= upper:
        part1 += 1
    if (x == req) ^ (y == req):
        part2 += 1
print("Part 1:", part1)
print("Part 2:", part2)
