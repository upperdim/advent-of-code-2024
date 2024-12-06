# Advent of Code 2024 - Day 6


def parse_input():
	with open('day6_input.txt', 'r') as file:
		grid = [line.replace('\n', '') for line in file]
	return grid


def create_2d_arr(r, c):
	arr = []
	for rr in range(r):
		arr.append([False for cc in range(c)])
	return arr


def is_in_bounds(grid, pos2d):
	return pos2d[0] >= 0 and pos2d[0] < len(grid) and pos2d[1] >= 0 and pos2d[1] < len(grid[0])


def get_guard_pos_dir(grid):
	guard_pos = []
	guard_dir = ''
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if ch == '>':
				guard_pos = [r,c]
				guard_dir = 'right'
			elif ch == '^':
				guard_pos = [r,c]
				guard_dir = 'up'
			elif ch == '<':
				guard_pos = [r,c]
				guard_dir = 'left'
			elif ch == 'v':
				guard_pos = [r,c]
				guard_dir = 'down'
	return guard_pos, guard_dir


dir_pos_diffs = {
	'up': [-1, 0],
	'down': [1, 0],
	'right': [0, 1],
	'left': [0, -1]
}


dir_update = {
	'right': 'down',
	'down': 'left',
	'left': 'up',
	'up': 'right'
}


def part1(grid):
	guard_pos, guard_dir = get_guard_pos_dir(grid)
	is_visited = create_2d_arr(len(grid), len(grid[0]))

	# Simulate until guard leaves the grid
	while is_in_bounds(grid, guard_pos):
		# Save location
		is_visited[guard_pos[0]][guard_pos[1]] = True

		# Check ahead
		pos_diff = dir_pos_diffs[guard_dir]
		pos_ahead = [guard_pos[0] + pos_diff[0], guard_pos[1] + pos_diff[1]]
		if is_in_bounds(grid, pos_ahead) and grid[pos_ahead[0]][pos_ahead[1]] == '#':
			guard_dir = dir_update[guard_dir]  # update direction
		else:
			# Move guard
			pos_diff = dir_pos_diffs[guard_dir]
			guard_pos = [guard_pos[0] + pos_diff[0], guard_pos[1] + pos_diff[1]]
	
	# Count visited locations
	visited_count = 0
	for r, row in enumerate(is_visited):
		for c, val in enumerate(row):
			if val:
				visited_count += 1
	print(visited_count)


def part2(grid):
	init_guard_pos, init_guard_dir = get_guard_pos_dir(grid)
	inf_loop_situation_count = 0

	# Brute force putting walls for each cell, check if guard ends up at the same location
	for wr, wall_row in enumerate(grid):
		print(f'trying row {wr} / {len(grid)}. found {inf_loop_situation_count}')
		for wc, ch in enumerate(wall_row):
			# Can't put wall on guard spawn
			if wr == init_guard_pos[0] and wc == init_guard_pos[1]:
				continue
			guard_pos = init_guard_pos.copy()
			guard_dir = init_guard_dir
			is_visited = set()  # 3rd dim for storing direction
			# Simulate guard
			while is_in_bounds(grid, guard_pos):
				# If imaginary wall is right in front, we have to fix the direction
				# Look ahead in order to turn around or move
				pos_diff = dir_pos_diffs[guard_dir]
				pos_ahead = [guard_pos[0] + pos_diff[0], guard_pos[1] + pos_diff[1]]
				# Move or turn
				if is_in_bounds(grid, pos_ahead) and (grid[pos_ahead[0]][pos_ahead[1]] == '#' or (pos_ahead[0] == wr and pos_ahead[1] == wc)):
					guard_dir = dir_update[guard_dir]
				else:
					guard_pos = pos_ahead.copy()
				# Check if visited before with same direction
				if (guard_pos[0], guard_pos[1], guard_dir) in is_visited:
					inf_loop_situation_count += 1
					break
				# Save the visit
				is_visited.add((guard_pos[0], guard_pos[1], guard_dir))
	print(inf_loop_situation_count)


def main():
	grid = parse_input()
	part1(grid)
	part2(grid)


if __name__ == '__main__':
	main()
