# Dominant Cells
grid = [
    [1, 2, 3],
    [3, 4, 5],
    [1, 6, 7]
]

freq = {}
for row in grid:
    for val in row:
        freq[val] = freq.get(val, 0) + 1

count = 0
for v in freq.values():
    if v > 1:
        count += v

print(count)
# output : 4
