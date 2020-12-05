with open("05.in") as f:
    lines = [x.strip() for x in f.readlines()]

ids = []
for line in lines:
    binary = ""
    for c in line:
        binary += "1" if c in "BR" else "0"
    ids.append(int(binary, 2))
print("Part 1:", max(ids))

for x in ids:
    if x + 1 not in ids and x + 2 in ids:
        print("Part 2:", x + 1)
