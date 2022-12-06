import sys

input = sys.stdin.read().strip()
def find(part):
    substr_length = 14 if part == 2 else 4
    for n in range(len(input)):
        if n < substr_length: continue
        substring, found = input[n - substr_length:n], True
        for c in substring:
            if substring.index(c) != substring.rindex(c):
                found = False
        if found: return n

print(f'part {1}: {find(1)}')
print(f'part {2}: {find(2)}')