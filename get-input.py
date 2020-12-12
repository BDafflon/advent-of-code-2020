import sys
import requests

day = int(sys.argv[1])

with open(".session") as f:
    session_cookie = f.read()

cookies = {
    "session": session_cookie,
}

puzzle_response = requests.get(
    f"https://adventofcode.com/2020/day/{day}/input", cookies=cookies
)
puzzle = puzzle_response.text.rstrip()

zeropad = "" if day > 9 else "0"
filename = zeropad + str(day) + ".in"
with open(filename, "w") as f:
    f.write(puzzle)
