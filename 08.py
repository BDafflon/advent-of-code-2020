with open("08.in") as f:
    lines = [x.strip() for x in f.readlines()]


def run_program(prog, part):
    assert part in (1, 2)
    acc = 0
    i = 0
    n = len(prog)
    seen = set()
    while True:
        if i == n and part == 2:
            return acc
        if i in seen:
            if part == 1:
                return acc
            if part == 2:
                return None
        seen.add(i)
        op, arg = prog[i].split()
        arg = int(arg)
        if op == "acc":
            acc += arg
            i += 1
        elif op == "jmp":
            i += arg
        else:
            i += 1


print("Part 1:", run_program(lines, 1))

for i in range(len(lines)):
    prog = lines[:]
    if lines[i].startswith("jmp"):
        prog[i] = prog[i].replace("jmp", "nop")
    elif lines[i].startswith("nop"):
        prog[i] = prog[i].replace("nop", "jmp")
    x = run_program(prog, 2)
    if x:
        print("Part 2:", x)
        exit()
