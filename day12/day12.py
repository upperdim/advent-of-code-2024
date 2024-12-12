# Advent of Code 2024 - Day 12


import pprint
from itertools import groupby


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
	
	return curr_cell


def part1(grid):
	visited = set()
	p1_region_area_perim.append([grid[0][0], 0, 0])

	prev_cell = grid[0][0]
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			prev_cell = visit(grid, r,c, visited, prev_cell)

	result = 0
	for region in p1_region_area_perim:
		# print(region)
		result += region[1] * region[2]
	print(result)


# [
#   region, 
#   area, 
#   sides = {
#     'u'= [ (r,c) , ...]
#   }
# ]
p2_region_area_sides = []
p2_idx = 0


def count_horiz_sides(edges_arr):
	sequences = 0
	i = 0
	while i < len(edges_arr):
		# j = index where sequence ends
		init_i = i
		j = i + 1
		while j < len(edges_arr) and edges_arr[i][0] == edges_arr[j][0] and edges_arr[i][1]+1 == edges_arr[j][1]:
			i += 1
			j += 1
		sequences += 1
		i = init_i + (j-init_i)
	return sequences


def count_vert_sides(edges_arr):
	sequences = 0
	i = 0
	while i < len(edges_arr):
		# j = index where sequence ends
		init_i = i
		j = i + 1
		while j < len(edges_arr) and edges_arr[i][1] == edges_arr[j][1] and edges_arr[i][0]+1 == edges_arr[j][0]:
			i += 1
			j += 1
		sequences += 1
		i = init_i + (j-init_i)
	return sequences


def get_sides(grid, r, c):
	apparent_in_sides = []
	if r == 0:              apparent_in_sides.append('u')
	if r == len(grid)-1:    apparent_in_sides.append('d')
	if c == 0:              apparent_in_sides.append('l')
	if c == len(grid[0])-1: apparent_in_sides.append('r')

	curr_cell = grid[r][c]
	if r >= 1              and grid[r-1][c] != curr_cell: apparent_in_sides.append('u')
	if r <= len(grid)-2    and grid[r+1][c] != curr_cell: apparent_in_sides.append('d')
	if c >= 1              and grid[r][c-1] != curr_cell: apparent_in_sides.append('l')
	if c <= len(grid[0])-2 and grid[r][c+1] != curr_cell: apparent_in_sides.append('r')
	return apparent_in_sides


def visit2(grid, r, c, visited, prev_cell):
	global p2_idx
	
	if (r,c) in visited:
		return
	visited.add((r,c))
	
	curr_cell = grid[r][c]
	if prev_cell != curr_cell:
		p2_region_area_sides.append([curr_cell,0,{}])
		p2_idx += 1
	
	p2_region_area_sides[p2_idx][1] += 1  # increase area

	# For each region, keep cells of sides of each direction (u,d,l,r) in a map
	apparent_in_sides = get_sides(grid,r,c)  # can be apparent in a corner, being in 2 sides
	for side in apparent_in_sides:
		if side != None:
			if side in p2_region_area_sides[p2_idx][2]:
				p2_region_area_sides[p2_idx][2][side].append((r,c))
			else:
				p2_region_area_sides[p2_idx][2][side] = [(r,c)]

	# Up
	if r >= 1 and grid[r-1][c] == curr_cell:
		visit2(grid,r-1,c,visited, curr_cell)

	# Down
	if r <= len(grid)-2 and grid[r+1][c] == curr_cell:
		visit2(grid,r+1,c,visited, curr_cell)

	# Left
	if c >= 1 and grid[r][c-1] == curr_cell:
		visit2(grid,r,c-1,visited, curr_cell)

	# Right
	if c <= len(grid[0])-2 and grid[r][c+1] == curr_cell:
		visit2(grid,r,c+1,visited, curr_cell)
	
	return curr_cell


def part2(grid):
	visited = set()
	p2_region_area_sides.append([grid[0][0], 0, {}])

	prev_cell = grid[0][0]
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			prev_cell = visit2(grid, r,c, visited, prev_cell)
	
	# For each region
	region_side_counts = []
	for region_idx in range(len(p2_region_area_sides)):
		count = 0

		region_sides_map = p2_region_area_sides[region_idx][2]
		
		# Iterate up facing edge cells, determine how many sides there are
		if 'u' in region_sides_map.keys():
			# Sort horizontal sides' edges by their row coordinates (same row coords near each other)
			region_sides_map['u'] = sorted(region_sides_map['u'], key=lambda x: (x[0], x[1]))
			# It is a single side as long as it is continuous
			count += count_horiz_sides(region_sides_map['u'])			

		if 'd' in region_sides_map.keys():
			# Sort horizontal sides' edges by their row coordinates (same row coords near each other)
			region_sides_map['d'] = sorted(region_sides_map['d'], key=lambda x: (x[0], x[1]))
			count += count_horiz_sides(region_sides_map['d'])
		

		if 'l' in region_sides_map.keys():
			# Sort vertical sides' edges by their column coordinates (same col coords near each other)
			region_sides_map['l'] = sorted(region_sides_map['l'], key=lambda x: (x[1], x[0]))
			count += count_vert_sides(region_sides_map['l'])

		if 'r' in region_sides_map.keys():
			# Sort vertical sides' edges by their column coordinates (same col coords near each other)
			region_sides_map['r'] = sorted(region_sides_map['r'], key=lambda x: (x[1], x[0]))
			count += count_vert_sides(region_sides_map['r'])
					
		region_side_counts.append(count)

	result = 0
	for i in range(len(p2_region_area_sides)):
		res = p2_region_area_sides[i][1] * region_side_counts[i]
		result += res
		# print(f'{p2_region_area_sides[i][1]} * {region_side_counts[i]} = {res}')
	print(result)


def main():
	grid = parse_input()
	part1(grid)
	part2(grid)


if __name__ == '__main__':
	main()
