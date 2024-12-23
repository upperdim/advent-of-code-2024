from pprint import pp


def parse_input():
	with open('demo.txt', 'r') as file:
		grid = [line.replace('\n', '') for line in file]
	return grid


dir_offsets = {(-1, 0), (0, 1), (1, 0), (0, -1)}


def dfs_with_distance(grid):
	sr,sc,er,ec=0,0,0,0
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if ch == 'S': sr,sc = r,c
			if ch == 'E': er,ec = r,c
	visited = set()
	to_visit = []
	soln_paths = []
	path = []
	to_visit.append((sr,sc,0,path))
	while len(to_visit) > 0:
		# Parse cell data
		cell = to_visit.pop()
		cell_r, cell_c, cell_dist, cell_path = cell[0], cell[1], cell[2], cell[3]

		# Recursion terminal condition (reached target)
		if grid[cell_r][cell_c] == 'E':
			soln_paths.append(cell_path + [(cell_r,cell_c,cell_dist)])
			continue
		
		# Recursion terminal condition (prevent infinite loop)
		if (cell_r, cell_c) in visited:
			continue
		visited.add((cell_r,cell_c))

		# Visit/recurse
		for dr,dc in dir_offsets:
			nr,nc = cell_r + dr, cell_c + dc
			if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] in '.E':
				to_visit.append((nr, nc, cell_dist + 1, cell_path + [(cell_r, cell_c, cell_dist)]))
	pp(soln_paths)


def main():
	grid = parse_input()
	dfs_with_distance(grid)


if __name__ == '__main__':
	main()
