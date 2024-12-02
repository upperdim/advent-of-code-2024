with open('grid.txt', 'r') as file:
    grid = [list(map(int, line.split())) for line in file]

print(grid)
