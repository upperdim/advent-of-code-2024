# Advent of Code 2024 - Day 16


import pprint


def parse_input():
	with open('day16_input.txt', 'r') as file:
		grid = [line.replace('\n', '') for line in file]
	return grid


dir_offsets = {
	'r': [0, 1],
	'u': [1, 0],
	'l': [0, -1],
	'd': [-1, 0],
}


def part1(grid):
	start = None
	end = None
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if ch == 'S':
				start = (r, c)
			elif ch == 'E':
				end = (r, c)

	# [coords, cost, direction]
	to_visit = [(start, 0, 'r')]
	
	# (r,c,dir): cost
	visited = {}
	
	while len(to_visit) > 0:
		if len(to_visit) % 500 == 0:
			print(f'list len = {len(to_visit)}')
		# To visit to visited
		(r, c), cost, dir = to_visit.pop()
		visited[(r, c, dir)] = cost

		# Terminal condition
		if (r, c) == end:
			print(cost)
			break

		# Visit
		for dir_offset in dir_offsets:
			if dir == 'u' and dir_offset == 'd': continue
			if dir == 'd' and dir_offset == 'u': continue
			if dir == 'r' and dir_offset == 'l': continue
			if dir == 'l' and dir_offset == 'r': continue
			dr, dc = dir_offsets[dir_offset][0], dir_offsets[dir_offset][1]
			if grid[r+dr][c+dc] != "#" and (r+dr, c+dc, dir_offset) not in visited:
				if dir == dir_offset:
					to_visit.append(((r+dr, c+dc), cost+1, dir_offset))
				else:
					to_visit.append(((r+dr, c+dc), cost+1001, dir_offset))

		# Sort descending on cost, wanna visit the lowest cost with pop()
		to_visit.sort(key=lambda x: x[1], reverse=True)


def print_ans(soln_paths):
	# Find min cost in the solution paths
	min_cost = soln_paths[0][-1][2]
	for soln_path in soln_paths:
		if min_cost > soln_path[-1][2]:
			min_cost = soln_path[-1][2]
	
	# Get a list of solution paths with the minimum cost
	min_cost_paths = []
	for soln_path in soln_paths:
		if min_cost == soln_path[-1][2]:
			min_cost_paths.append(soln_path)
	
	# Form a set of tiles of paths with the minimum cost
	best_tiles = set()
	for path in min_cost_paths:
		for tile in path:
			best_tiles.add(tile)
	print(f'ans = {len(best_tiles)}')


def part2(grid):
	sr = sc = er = ec = None
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if   ch == 'S': sr, sc = r, c
			elif ch == 'E': er, ec = r, c

	soln_paths = []

	# to_visit: Contains information of cells to visit:
	# row:                       row    coord of the cell
	# col:                       column coord of the cell
	# cost:                      accumulated cost of ongoing traversal at this cell
	# direction:                 direction at given cell
	# path_history_list:         a coordinates and cost list containing the
	#                            visited cells for the ongoing traversal (row, col, cost)
	# visited_set_per_traversal: a coordinates set containing visited
	#                            cells for the ongoing traversal
	to_visit = [(sr,sc,0,'r',[(sr,sc, 0)], set())]
	while len(to_visit) > 0:
		# if len(to_visit) % 500 == 0:
			# print(f'list len = {len(to_visit)}')

		r, c, cost, direction, path, visited = to_visit.pop()
		
		if r == er and c == ec:
			print(f'Found exit with cost {cost}')
			soln_paths.append(path)
			# print_ans(soln_paths)
			continue
		
		if (r,c) in visited:
			continue
		visited.add((r,c))

		for d in dir_offsets:
			if direction == 'u' and d == 'd': continue
			if direction == 'd' and d == 'u': continue
			if direction == 'r' and d == 'l': continue
			if direction == 'l' and d == 'r': continue
			dr, dc = dir_offsets[d]
			nr, nc = r+dr, c+dc
			if grid[nr][nc] != "#":
				if direction == d:
					to_visit.append((nr, nc, cost+1,    d, path + [(nr, nc, cost+1)], visited.copy()))
				else:
					to_visit.append((nr, nc, cost+1001, d, path + [(nr, nc, cost+1001)], visited.copy()))
		
		# Sort descending on cost, wanna visit the lowest cost with pop()
		to_visit.sort(key=lambda x: x[2], reverse=True)

	# Find min cost in the solution paths
	min_cost = soln_paths[0][-1][2]
	for soln_path in soln_paths:
		if min_cost > soln_path[-1][2]:
			min_cost = soln_path[-1][2]
	
	# Get a list of solution paths with the minimum cost
	min_cost_paths = []
	for soln_path in soln_paths:
		if min_cost == soln_path[-1][2]:
			min_cost_paths.append(soln_path)
	
	# Form a set of tiles of paths with the minimum cost
	best_tiles = set()
	for path in min_cost_paths:
		for tile in path:
			best_tiles.add(tile)
	
	print(f'Part 2 = {len(best_tiles)}')


def main():
	grid = parse_input()
	part1(grid)
	part2(grid)


if __name__ == '__main__':
	main()
