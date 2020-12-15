import re

def apply_mask(number, mask):
    # Was originally written a lot messier with iterating over
    # the number as a string. This is much better, as it lets us use
    # the bitmask as an actual bitmask.
    # Kudos to Sophie Albert:
    # https://github.com/sophiebits/adventofcode/blob/main/2020/day14.py
    number |= int(mask.replace('X', '0'), 2)
    number &= int(mask.replace('X', '1'), 2)
    return number

def all_masks(mask):
    # This function generates mask that let us reuse the apply_mask
    # function from part 1 – and is much more clever than what I did
    # on my own the first time round.
    # Again, kudos to Sophie Albert:
    # https://github.com/sophiebits/adventofcode/blob/main/2020/day14.py
    if not mask:
        yield ''
        return
    for m in all_masks(mask[1:]):
        if mask.startswith('0'):
            yield 'X' + m # Leave as is
        elif mask.startswith('1'):
            yield '1' + m # Change to 1
        else:
            yield '1' + m # Use both options
            yield '0' + m
    

with open('14.in') as f:
    lines = [x.strip() for x in f.readlines()]

mask = None
mem_1 = {}
mem_2 = {}
for line in lines:
    if line.startswith('mask'):
        mask = line.split()[-1]
    else:
        m = re.match(r"mem\[(\d+)\] = (\d+)", line)
        adress, val = [int(x) for x in m.group(1, 2)]
        mem_1[adress] = apply_mask(val, mask)
        for m in all_masks(mask):
            mem_2[apply_mask(adress, m)] = val
print(sum(mem_1.values()))
print(sum(mem_2.values()))