# Advent of Code 2024 - Day 12


import pprint
from itertools import groupby


def parse_input():
	with open('day12_test.txt', encoding="utf8") as f:
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
	# Group tuples by their first element (x)
	groups = {key: [y for _, y in group] for key, group in groupby(edges_arr, key=lambda x: x[0])}

	# Calculate the total number of continuous sequences
	total_sequences = 0
	for ys in groups.values():
		sequences = 0
		in_sequence = False

		for i in range(1, len(ys)):
			if ys[i] == ys[i - 1] + 1:  # Continuation of a sequence
				if not in_sequence:
					sequences += 1
					in_sequence = True
			else:
				in_sequence = False  # Break in the sequence

		if len(ys) > 0 and not in_sequence:
			sequences += 1  # Account for single numbers as sequences

		total_sequences += sequences
	return total_sequences

def count_vert_sides(edges_arr):
    # Group tuples by their second element (y)
    groups = {key: [x for x, _ in group] for key, group in groupby(edges_arr, key=lambda x: x[1])}

    # Calculate the total number of continuous sequences
    total_sequences = 0
    for xs in groups.values():
        sequences = 0
        in_sequence = False

        for i in range(1, len(xs)):
            if xs[i] == xs[i - 1] + 1:  # Continuation of a sequence
                if not in_sequence:
                    sequences += 1
                    in_sequence = True
            else:
                in_sequence = False  # Break in the sequence

        if len(xs) > 0 and not in_sequence:
            sequences += 1  # Account for single numbers as sequences

        total_sequences += sequences
    return total_sequences


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
		
		before_count = count
		# Iterate up facing edge cells, determine how many sides there are
		if 'u' in region_sides_map.keys():
			# Sort horizontal sides' edges by their row coordinates (same row coords near each other)
			region_sides_map['u'] = sorted(region_sides_map['u'], key=lambda x: (x[0], x[1]))
			print('sorted up sides =', end='')
			pprint.pp(region_sides_map['u'])
			# It is a single side as long as it is continuous
			count += count_horiz_sides(region_sides_map['u'])			
		print(f'found {count - before_count} sides')

		before_count = count
		if 'd' in region_sides_map.keys():
			# Sort horizontal sides' edges by their row coordinates (same row coords near each other)
			region_sides_map['d'] = sorted(region_sides_map['d'], key=lambda x: (x[0], x[1]))
			print('sorted down sides =', end='')
			pprint.pp(region_sides_map['d'])	
			count += count_horiz_sides(region_sides_map['d'])
		print(f'found {count - before_count} sides')
		

		before_count = count
		if 'l' in region_sides_map.keys():
			# Sort vertical sides' edges by their column coordinates (same col coords near each other)
			region_sides_map['l'] = sorted(region_sides_map['l'], key=lambda x: (x[1], x[0]))
			print('sorted left sides =', end='')
			pprint.pp(region_sides_map['l'])
			count += count_vert_sides(region_sides_map['l'])
		print(f'found {count - before_count} sides')

		before_count = count
		if 'r' in region_sides_map.keys():
			# Sort vertical sides' edges by their column coordinates (same col coords near each other)
			region_sides_map['r'] = sorted(region_sides_map['r'], key=lambda x: (x[1], x[0]))
			print('sorted right sides =', end='')
			pprint.pp(region_sides_map['r'])
			count += count_vert_sides(region_sides_map['r'])
		print(f'found {count - before_count} sides')
					
		region_side_counts.append(count)

	# pprint.pp(p2_region_area_sides)
	pprint.pp(region_side_counts)

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
