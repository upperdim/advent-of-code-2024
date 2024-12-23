from pprint import pp


def parse_input():
	with open('day20_input.txt', 'r') as file:
		grid = [line.replace('\n', '') for line in file]
	return grid


dir_offsets = {(-1, 0), (0, 1), (1, 0), (0, -1)}


def part1(grid):
	sr,sc,er,ec=0,0,0,0
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if ch == 'S': sr,sc = r,c
			if ch == 'E': er,ec = r,c
	
	visited = set()
	to_visit = []
	soln_paths = []
	
	path = []
	to_visit.append((sr, sc, 0, path))

	while len(to_visit) > 0:
		# Parse cell data
		cell = to_visit.pop()
		cell_r, cell_c, cell_dist, cell_path = cell[0], cell[1], cell[2], cell[3]

		# Recursion terminal condition (reached target)
		if grid[cell_r][cell_c] == 'E':
			soln_paths.append(cell_path + [(cell_r, cell_c, cell_dist+1)])
			continue

		# Recursion terminal condition (prevent infinite loop)
		if (cell_r, cell_c) in visited:
			continue
		visited.add((cell_r,cell_c))

		# Visit/recurse
		for dr,dc in dir_offsets:
			nr,nc = cell_r+dr, cell_c+dc
			if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] in '.E':
				to_visit.append((nr, nc, cell_dist+1, cell_path+[(cell_r, cell_c, cell_dist+1)]))
	
	# Find shortest solution path
	min_dist_soln = soln_paths[0]
	for soln_path in soln_paths:
		if len(soln_path) < len(min_dist_soln):
			min_dist_soln = soln_path

	cheating_spot_count = 0
	# Compare saved cell pairs c1,c2 to find eligible cheating spots
	for i in range(len(min_dist_soln)):
		for j in range(i+1, len(min_dist_soln)):
			c1, c2 = min_dist_soln[i], min_dist_soln[j]

			c1r, c1c, c1d = c1[0], c1[1], c1[2]
			c2r, c2c, c2d = c2[0], c2[1], c2[2]

			dr = abs(c1r - c2r)
			dc = abs(c1c - c2c)
			dd = abs(c1d - c2d) - 2  # idk why my results are 2 larger...

			if dd>=100:
				if dr==1 and dc==1:
					# print(f'Found cheating point near {c1} and {c2} saving {dd} - dr==dc==1')
					cheating_spot_count += 1
				elif dr==2 and dc==0:
					# print(f'Found cheating point near {c1} and {c2} saving {dd} - dr==2')
					cheating_spot_count += 1
				elif dr==0 and dc==2:
					# print(f'Found cheating point near {c1} and {c2} saving {dd} - dc==2')
					cheating_spot_count += 1
	print(cheating_spot_count)



def part2(grid):
	sr,sc,er,ec=0,0,0,0
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if ch == 'S': sr,sc = r,c
			if ch == 'E': er,ec = r,c
	
	visited = set()
	to_visit = []
	soln_paths = []
	
	path = []
	to_visit.append((sr, sc, 0, path))

	while len(to_visit) > 0:
		# Parse cell data
		cell = to_visit.pop()
		cell_r, cell_c, cell_dist, cell_path = cell[0], cell[1], cell[2], cell[3]

		# Recursion terminal condition (reached target)
		if grid[cell_r][cell_c] == 'E':
			soln_paths.append(cell_path + [(cell_r, cell_c, cell_dist+1)])
			continue

		# Recursion terminal condition (prevent infinite loop)
		if (cell_r, cell_c) in visited:
			continue
		visited.add((cell_r,cell_c))

		# Visit/recurse
		for dr,dc in dir_offsets:
			nr,nc = cell_r+dr, cell_c+dc
			if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] in '.E':
				to_visit.append((nr, nc, cell_dist+1, cell_path+[(cell_r, cell_c, cell_dist+1)]))
	
	# Find shortest solution path
	min_dist_soln = soln_paths[0]
	for soln_path in soln_paths:
		if len(soln_path) < len(min_dist_soln):
			min_dist_soln = soln_path

	cheating_spot_count = 0
	# Compare saved cell pairs c1,c2 to find eligible cheating spots
	for i in range(len(min_dist_soln)):
		for j in range(i+1, len(min_dist_soln)):
			c1, c2 = min_dist_soln[i], min_dist_soln[j]

			c1r, c1c, c1d = c1[0], c1[1], c1[2]
			c2r, c2c, c2d = c2[0], c2[1], c2[2]

			dr = abs(c1r - c2r)
			dc = abs(c1c - c2c)
			dd = abs(c1d - c2d) - 2  # idk why my results are 2 larger...

			if dd>=100:
				if dr + dc <= 20:
					# print(f'Found cheating point near {c1} and {c2} saving {dd} - duration = {dr+dc}')
					cheating_spot_count += 1
	print(cheating_spot_count)


def main():
	grid = parse_input()
	part1(grid)
	part2(grid)


if __name__ == '__main__':
	main()
