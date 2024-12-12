# Advent of Code 2024 - Day 12


import pprint


def parse_input():
	with open('day12_input.txt', encoding="utf8") as f:
		grid = [line.replace('\n', '') for line in f]
	return grid


# [region, area, perim]
p1_region_area_perim = []
p1_idx = 0

def visit(grid, r, c, visited, prev_cell):
	global p1_idx

	if (r,c) in visited:
		return
	visited.add((r,c))
	
	curr_cell = grid[r][c]
	if prev_cell != curr_cell:
		p1_region_area_perim.append([curr_cell,0,0])
		p1_idx += 1
	
	p1_region_area_perim[p1_idx][1] += 1  # increase area

	# Up
	if r >= 1 and grid[r-1][c] == curr_cell:
		visit(grid,r-1,c,visited, curr_cell)
	else:
		p1_region_area_perim[p1_idx][2] += 1  # increase perim

	# Down
	if r <= len(grid)-2 and grid[r+1][c] == curr_cell:
		visit(grid,r+1,c,visited, curr_cell)
	else:
		p1_region_area_perim[p1_idx][2] += 1  # increase perim

	# Left
	if c >= 1 and grid[r][c-1] == curr_cell:
		visit(grid,r,c-1,visited, curr_cell)
	else:
		p1_region_area_perim[p1_idx][2] += 1  # increase perim

	# Right
	if c <= len(grid[0])-2 and grid[r][c+1] == curr_cell:
		visit(grid,r,c+1,visited, curr_cell)
	else:
		p1_region_area_perim[p1_idx][2] += 1  # increase perim


def part1(grid):
	visited = set()
	p1_region_area_perim.append([grid[0][0], 0, 0])

	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			visit(grid, r,c, visited, grid[0][0])
			
	result = 0
	for region in p1_region_area_perim:
		# print(region)
		result += region[1] * region[2]
	print(result)


def part2(grid):
	pass


def main():
	grid = parse_input()
	part1(grid)
	part2(grid)


if __name__ == '__main__':
	main()
