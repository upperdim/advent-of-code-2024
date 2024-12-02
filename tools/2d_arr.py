with open('grid.txt', 'r') as file:
    grid = [list(map(int, line.split())) for line in file]

print(grid)

# Iterate grid and neighbours of each element
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        print(f'Grid element = {grid[r][c]}')
        
        for adj_r in range(r - 1, r + 2):
            for adj_c in range(c - 1, c + 2):
                if adj_r < 0 or adj_r >= len(grid) or adj_c < 0 or adj_c >= len(grid[adj_r]):
                    continue
                print(f'Neighbour {grid[adj_r][adj_c]}')
