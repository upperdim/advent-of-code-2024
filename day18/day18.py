from pprint import pp


def parse_input():
	with open('day18_input.txt', encoding="utf8") as f:
		lines = [line.strip() for line in f.readlines()]
	return lines


dir_offsets = {(-1, 0), (0, 1), (1, 0), (0, -1)}


def change_char(grid, r, c, replacement):
	row = grid[r]
	l = list(row)
	l[c] = replacement
	grid[r] = ''.join(l)


def print_grid(grid):
	for row in grid:
		print(row)


def part1(lines):
	# Prepare map
	w = h = 71
	row = '.' * w
	grid = [row for i in range(h)]
	# Test
	# for i in range(12):
	# 	c, r = lines[i].split(',')
	# 	r, c = int(r), int(c)
	# 	change_char(grid, r, c, '#')
	# Real
	for i in range(1024):
		c, r = lines[i].split(',')
		r, c = int(r), int(c)
		change_char(grid, r, c, '#')
	
	# Start solution
	visited = set()
	to_visit = [(0,0,0,)]  # r,c,dist
	while len(to_visit) > 0:
		# Explore all elements that were pushed earlier
		# Explore distances n before n+1 = BFS for shortest path
		r, c, dist = to_visit.pop(0)

		if r == h-1 and c == w-1:
			print(f'Exit in {dist} moves')
			continue

		if (r, c) in visited:
			continue
		visited.add((r, c))
		
		for dr, dc in dir_offsets:
			nr, nc = r+dr, c+dc
			if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '.':
				to_visit.append((nr, nc, dist+1))


def exit_map(grid, w, h):
	visited = set()
	to_visit = [(0,0,0,)]  # r,c,dist
	while len(to_visit) > 0:
		# Explore all elements that were pushed earlier
		# Explore distances n before n+1 = BFS for shortest path
		r, c, dist = to_visit.pop(0)

		if r == h-1 and c == w-1:
			return dist

		if (r, c) in visited:
			continue
		visited.add((r, c))
		
		for dr, dc in dir_offsets:
			nr, nc = r+dr, c+dc
			if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '.':
				to_visit.append((nr, nc, dist+1))
	return -1


def part2(lines):
	# Prepare map
	w = h = 71
	row = '.' * w
	grid = [row for i in range(h)]
	# Test
	# for i in range(12):
	# 	c, r = lines[i].split(',')
	# 	r, c = int(r), int(c)
	# 	change_char(grid, r, c, '#')
	# Real
	for i in range(len(lines)):
		exit_steps = exit_map(grid, w, h)
		if exit_steps == -1:
			print(f'{i} bytes fallen, {exit_steps} steps')
			# Byte index i hasn't fallen yet,
			# Last fallen byte index is i-1 from previous iteration
			print(f'Byte at {lines[i-1]} blocks the exit')
			return
		c, r = lines[i].split(',')
		r, c = int(r), int(c)
		change_char(grid, r, c, '#')


def main():
	lines = parse_input()
	part1(lines)
	part2(lines)


if __name__ == '__main__':
	main()
