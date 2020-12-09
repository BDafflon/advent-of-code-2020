from collections import deque

with open("09.in") as f:
    lines = [int(x.strip()) for x in f.readlines()]

preamble_length = 25
preamble = deque(lines[:preamble_length])


def preamble_sums_to(i, preamble):
    seen = set()
    for j in preamble:
        if i - j in seen:
            return True
        seen.add(j)
    return False


invalid = 0
for i in lines[preamble_length:]:
    if not preamble_sums_to(i, preamble):
        invalid = i
        break
    preamble.popleft()
    preamble.append(i)

summation_queue = deque([])
summation = 0
for x in lines:
    while summation > invalid:
        summation -= summation_queue.popleft()
    if summation == invalid:
        break
    summation_queue.append(x)
    summation += x

print("Part 1:", invalid)
print("Part 2:", max(summation_queue) + min(summation_queue))
