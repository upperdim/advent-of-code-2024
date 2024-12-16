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


def part2(grid):
	pass


def main():
	grid = parse_input()
	part1(grid)
	part2(grid)


if __name__ == '__main__':
	main()
