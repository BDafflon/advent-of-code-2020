from collections import defaultdict

with open("10.in") as f:
    jolts = [int(x.strip()) for x in f]

jolts.sort()
jolts.append(jolts[-1] + 3)
jolts.insert(0, 0)

count = defaultdict(int)
for i in range(1, len(jolts)):
    count[jolts[i] - jolts[i - 1]] += 1


def ways_to_target(jolts):
    memo = {}
    return _ways_from_index(0, jolts, memo)


def _ways_from_index(i, jolts, memo):
    if i == len(jolts) - 1:
        # We are at the end, and we are done
        return 1
    if i in memo:
        return memo[i]
    ans = 0
    j = i + 1
    while j < len(jolts) and jolts[j] - jolts[i] <= 3:
        ans += _ways_from_index(j, jolts, memo)
        j += 1
    memo[i] = ans
    return ans


print("Part 1:", count[1] * count[3])
print("Part 2:", ways_to_target(jolts))
