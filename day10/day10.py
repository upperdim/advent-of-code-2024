# Advent of Code 2024 - Day 10


import pprint


def parse_input():
	with open('day10_input.txt', 'r') as file:
		grid = [line.replace('\n', '') for line in file]
	num_grid = []
	for row in grid:
		curr_row = []
		for col in row:
			curr_row.append(int(col))
		num_grid.append(curr_row)
	# pprint.pp(num_grid)
	return num_grid


part1_score = 0
part2_score = 0


def check_cell(grid, r, c, peaks, is_part2):
	global part1_score
	global part2_score

	cell_val = grid[r][c]
	# print(f'checking {cell_val} at ({r},{c})')

	if cell_val == 9:
		if is_part2:
			part2_score += 1
		if (r,c) not in peaks:
			# print(f'peaked at ({r},{c})')
			part1_score += 1
			peaks.add((r,c))
		return

	if r >= 1 and grid[r-1][c] == cell_val+1:
		check_cell(grid, r-1, c, peaks, is_part2)

	if c >= 1 and grid[r][c-1] == cell_val+1:
		check_cell(grid, r, c-1, peaks, is_part2)

	if r <= len(grid)-2 and grid[r+1][c] == cell_val+1:
		check_cell(grid, r+1, c, peaks, is_part2)

	if c <= len(grid[0])-2 and grid[r][c+1] == cell_val+1:
		check_cell(grid, r, c+1, peaks, is_part2)


def part1(grid):
	global part1_score
	for r, row in enumerate(grid):
		for c, n in enumerate(row):
			if n == 0:
				init_part1_score = part1_score
				peaks = set()
				check_cell(grid, r, c, peaks, False)
				# print(f'trail ({r},{c}) scored {part1_score - init_part1_score}')
	print(part1_score)


def part2(grid):
	global part2_score
	for r, row in enumerate(grid):
		for c, n in enumerate(row):
			if n == 0:
				init_part2_score = part2_score
				peaks = set()
				check_cell(grid, r, c, peaks, True)
				# print(f'trail ({r},{c}) scored {part2_score - init_part2_score}')
	print(part2_score)


def main():
	grid = parse_input()
	part1(grid)
	part2(grid)


if __name__ == '__main__':
	main()
