from copy import deepcopy
from collections import defaultdict

with open('11.in') as f:
    seats = [list(x.strip()) for x in f]

directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

m, n = len(seats), len(seats[0])
old = deepcopy(seats)
while True:
    for r in range(m):
        for c in range(n):
            current = old[r][c]
            if current == '.':
                continue
            occupied_neighbours = 0
            for dr, dc in directions:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < m and 0 <= cc < n:
                    if old[rr][cc] == '#':
                        occupied_neighbours += 1
            if current == 'L' and occupied_neighbours == 0:
                seats[r][c] = '#'
            elif current == '#' and occupied_neighbours >= 4:
                seats[r][c] = 'L'
    if seats == old:
        break
    else:
        old = deepcopy(seats)
ans = 0
for row in seats:
    ans += row.count('#')

print("Part 1:", ans)