with open("01.in") as f:
    numbers = [int(x) for x in f.read().split("\n")]

n = len(numbers)

for i, x in enumerate(numbers):
    for j, y in enumerate(numbers[i + 1 :]):
        if x + y == 2020:
            print("Part 1:")
            print(x * y)
            print("-" * 10)
        if x + y < 2020:
            for z in numbers[i + j + 1 :]:
                if x + y + z == 2020:
                    print("Part 2:")
                    print(x * y * z)
