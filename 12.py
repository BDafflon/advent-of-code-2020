with open("12.in") as f:
    lines = [x.strip() for x in f]

directions = {"N": 0 + 1j, "E": 1 + 0j, "S": 0 - 1j, "W": -1 + 0j}

current_position = 0 + 0j
current_heading = 1 + 0j

for line in lines:
    direction, steps = line[0], line[1:]
    steps = int(steps)
    if direction == "F":
        current_position += steps * current_heading
    elif direction == "R":
        turns = int(steps / 90)
        for _ in range(turns):
            current_heading *= -1j
    elif direction == "L":
        turns = int(steps / 90)
        for _ in range(turns):
            current_heading *= 1j
    else:
        current_position += directions[direction] * steps

print("Part 1:", abs(current_position.real) + abs(current_position.imag))

current_position = 0 + 0j
waypoint = 10 + 1j
current_heading = 1 + 0j

for line in lines:
    direction, steps = line[0], line[1:]
    steps = int(steps)
    if direction == "F":
        current_position += steps * waypoint
    elif direction == "R":
        turns = int(steps / 90)
        for _ in range(turns):
            waypoint *= -1j
    elif direction == "L":
        turns = int(steps / 90)
        for _ in range(turns):
            waypoint *= 1j
    else:
        waypoint += directions[direction] * steps

print("Part 2:", abs(current_position.real) + abs(current_position.imag))
