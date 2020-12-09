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

summation_set = set()
for i, x in enumerate(lines):
    summed = x
    summation_set = set([x])
    j = i + 1
    while summed < invalid:
        summed += lines[j]
        summation_set.add(lines[j])
        j += 1
    if summed == invalid:
        break

print("Part 1:", invalid)
print("Part 2:", max(summation_set) + min(summation_set))
