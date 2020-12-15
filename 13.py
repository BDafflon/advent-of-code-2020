from math import ceil
from itertools import count

with open("13.in") as f:
    lines = f.readlines()
    earliest_departure = int(lines[0].strip())
    times = [x.strip() for x in lines[1].split(',')]

for i, time in enumerate(times):
    if time != 'x':
        times[i] = int(time)

idno = -1
wait_time = float('inf')
for time in times:
    if time != 'x':
        next_departure = ceil(earliest_departure / time) * time
        this_wait_time = next_departure - earliest_departure
        if this_wait_time < wait_time:
            wait_time = this_wait_time
            idno = time
print("Part 1:", wait_time*idno)

ans = 1
step = 1
for i, x in enumerate(times):
    if isinstance(x, int):
        # This works because the numbers are co-prime:
        ans = next(c for c in count(ans, step) if (c + i) % x == 0)
        step *= x
print('Part 2:', ans)