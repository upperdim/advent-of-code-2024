# Advent of Code 2024 - Day 12


import pprint


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


def get_side(grid, r, c):
	if r == 0:              return 'u'
	if r == len(grid)-1:    return 'd'
	if c == 0:              return 'l'
	if c == len(grid[0])-1: return 'r'

	curr_cell = grid[r][c]
	if grid[r-1][c] != curr_cell: return 'u'
	if grid[r+1][c] != curr_cell: return 'd'
	if grid[r][c-1] != curr_cell: return 'l'
	if grid[r][c+1] != curr_cell: return 'r'
	return None


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
	side = get_side(grid,r,c)
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
			# for edge in region_sides_map['u']:
			# It is a single side as long as it is continuous
			for i in range(1, len(region_sides_map['u'])):
				prev = region_sides_map['u'][i - 1]
				curr = region_sides_map['u'][i]
				print(f'prev = {prev} , curr = {curr}')
				if prev[0] == curr[0] and prev[1]+1 == curr[1]:
					continue
				else:
					print(f'side!')
					count += 1
			if len(region_sides_map['u']) >= 2:
				last = region_sides_map['u'][-1]
				second_last = region_sides_map['u'][-2]
				if second_last[0] != last[0] and second_last[1] != last[1]:
					print(f'side (aftercheck)')
					count += 1
					
		print(f'found {count - before_count} sides')

		if 'd' in region_sides_map.keys():
			# Sort horizontal sides' edges by their row coordinates (same row coords near each other)
			region_sides_map['d'] = sorted(region_sides_map['d'], key=lambda x: (x[0], x[1]))
			for i in range(1, len(region_sides_map['d'])):
				prev = region_sides_map['d'][i - 1]
				curr = region_sides_map['d'][i]
				if prev[0] == curr[0] or prev[1]+1 != curr[1]:
					count += 1
			if len(region_sides_map['d']) >= 2:
				last = region_sides_map['d'][-1]
				second_last = region_sides_map['d'][-2]
				if second_last[0] != last[0] and second_last[1] != last[1]:
					print(f'side (aftercheck)')
					count += 1

		if 'l' in region_sides_map.keys():
			# Sort vertical sides' edges by their column coordinates (same col coords near each other)
			region_sides_map['l'] = sorted(region_sides_map['l'], key=lambda x: (x[1], x[0]))
			for i in range(1, len(region_sides_map['l'])):
				prev = region_sides_map['l'][i - 1]
				curr = region_sides_map['l'][i]
				if prev[0]+1 == curr[0] or prev[1] != curr[1]:
					count += 1
			if len(region_sides_map['l']) >= 2:
				last = region_sides_map['l'][-1]
				second_last = region_sides_map['l'][-2]
				if second_last[0] != last[0] and second_last[1] != last[1]:
					print(f'side (aftercheck)')
					count += 1

		if 'r' in region_sides_map.keys():
			# Sort vertical sides' edges by their column coordinates (same col coords near each other)
			region_sides_map['r'] = sorted(region_sides_map['r'], key=lambda x: (x[1], x[0]))
			for i in range(1, len(region_sides_map['r'])):
				prev = region_sides_map['r'][i - 1]
				curr = region_sides_map['r'][i]
				if prev[0]+1 == curr[0] or prev[1] != curr[1]:
					count += 1
			if len(region_sides_map['r']) >= 2:
				last = region_sides_map['r'][-1]
				second_last = region_sides_map['r'][-2]
				if second_last[0] != last[0] and second_last[1] != last[1]:
					print(f'side (aftercheck)')
					count += 1
					
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
