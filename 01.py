with open("01.in") as f:
    numbers = [int(x) for x in f.read().split("\n")]

# Part 1, O(n)
s = set()
for n in numbers:
    if 2020 - n not in s:
        s.add(n)
    else:
        print(n * (2020 - n))

# Part 2, O(n^2)
s = set()
for i, x in enumerate(numbers):
    for y in numbers[i + 1 :]:
        if 2020 - x - y not in s:
            s.add(x)
            s.add(y)
        else:
            print(x * y * (2020 - x - y))
            exit()