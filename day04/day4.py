# Advent of Code 2024 - Day 4


def parse_input():
	with open('day4_input.txt', 'r') as file:
		grid = [line.replace('\n', '') for line in file]
	return grid


def is_out_of_bounds(grid, r, c):
	return r < 0 or r >= len(grid[0]) or c < 0 or c >= len(grid)


# except Exception as e:
# 	print(f'{e}')
# 	print(f'r = {r}, c = {c}, grid[r][c] = {grid[r][c]}, dir_offset = {dir_offset}, new_r = {new_r}, new_c = {new_c}')
# 	exit(0)
def part1(grid):
	dir_offsets = [
		[-1, -1],  # up left
		[-1,  0],  # up
		[-1,  1],  # up right
		[ 0,  1],  # right
		[ 1,  1],  # down right
		[ 1,  0],  # down
		[ 1, -1],  # down left
		[ 0, -1]   # left
	]
	xmas_count = 0
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if ch == 'X':
				for dir_offset in dir_offsets:
					new_r = r + dir_offset[0]
					new_c = c + dir_offset[1]
					if is_out_of_bounds(grid, new_r, new_c):
						continue
					if grid[new_r][new_c] == 'M':
						new_r += dir_offset[0]
						new_c += dir_offset[1]
						if is_out_of_bounds(grid, new_r, new_c):
							continue
						
						if grid[new_r][new_c] == 'A':
							new_r += dir_offset[0]
							new_c += dir_offset[1]
							if is_out_of_bounds(grid, new_r, new_c):
								continue

							if grid[new_r][new_c] == 'S':
								# print(f'found XMAS at [{new_r}, {new_c}] in direction {dir_offset}')
								xmas_count += 1
							# end of S if
						# end of A if
					# end of M if
				# end of dir_offsets for
			# end of X if
	print(xmas_count)


def part2(grid):
	dir_offsets = [
		[-1, -1],  # up left
		[-1,  0],  # up
		[-1,  1],  # up right
		[ 0,  1],  # right
		[ 1,  1],  # down right
		[ 1,  0],  # down
		[ 1, -1],  # down left
		[ 0, -1]   # left
	]
	x_mas_count = 0
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if ch == 'A':
				diag1_ok = False
				diag2_ok = False
				# Check diagonal 1
				if is_out_of_bounds(grid, r -1, c - 1) or is_out_of_bounds(grid, r + 1, c + 1):
					continue
				if (grid[r-1][c-1] == 'M' and grid[r+1][c+1] == 'S') or (grid[r-1][c-1] == 'S' and grid[r+1][c+1] == 'M'):
					diag1_ok = True
				# Check diagonal 2
				if is_out_of_bounds(grid, r -1, c + 1) or is_out_of_bounds(grid, r + 1, c - 1):
					continue
				if (grid[r-1][c+1] == 'M' and grid[r+1][c-1] == 'S') or (grid[r-1][c+1] == 'S' and grid[r+1][c-1] == 'M'):
					diag2_ok = True
				if diag1_ok and diag2_ok:
					x_mas_count += 1
	print(x_mas_count)


def main():
	grid = parse_input()
	part1(grid)
	part2(grid)


if __name__ == '__main__':
	main()
