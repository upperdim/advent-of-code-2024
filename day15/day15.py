# Advent of Code 2024 - Day 15


import pprint


def parse_input():
	grid = []
	moves = ''
	with open('day15_input.txt', encoding="utf8") as f:
		lines = [line.strip() for line in f.readlines()]
	state = 'g'
	for line in lines:
		if line == '':
			state = 'm'
			continue
		if state == 'g':
			grid.append(line.replace('\n', ''))
		elif state == 'm':
			moves += line
	return grid, moves


dir_offsets = {
	'>': [ 0,  1],
	'<': [ 0, -1],
	'^': [-1,  0],
	'v': [ 1,  0],
}


def change_char(grid, r, c, replacement):
	row = grid[r]
	l = list(row)
	l[c] = replacement
	grid[r] = ''.join(l)


def part1(grid, moves):
	# Find robot
	rr = rc = 0
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if ch == '@':
				rr, rc = r, c
	# Move boxes
	for move in moves:
		# pprint.pp(grid)
		# print('Move', move)
		dr, dc = dir_offsets[move][0], dir_offsets[move][1]
		check_r, check_c = rr + dr, rc + dc
		num_boxes_in_front = 0
		if grid[check_r][check_c] == '.':
			change_char(grid, rr, rc, '.')  # move the robot
			change_char(grid, check_r, check_c, '@')
			rr, rc = check_r, check_c
			continue
		elif grid[check_r][check_c] == '#':
			continue
		elif grid[check_r][check_c] == 'O':
			# Count number of boxes in front
			i = 1
			while grid[rr + (i * dr)][rc + (i * dc)] == 'O':
				num_boxes_in_front = i
				i += 1
			# Check behind the boxes
			if grid[rr + (i * dr)][rc + (i * dc)] == '#':
				continue  # there is a wall behind the boxes, do nothing
			elif grid[rr + (i * dr)][rc + (i * dc)] == '.':
				change_char(grid, rr + (i * dr), rc + (i * dc), 'O')  # push the boxes
				change_char(grid, rr, rc, '.')                        # move the robot
				change_char(grid, check_r, check_c, '@')
				rr, rc = check_r, check_c
	# pprint.pp(grid)
	# Find result
	gps_sum = 0
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if ch == 'O':
				gps_sum += r * 100 + c
	print(gps_sum)


def check_boxes(grid, check_r, check_c, dr, dc, to_move):
	second_r = check_r
	second_c = check_c + 1 if grid[check_r][check_c] == '[' else check_c - 1
	
	box_char = grid[check_r][check_c]
	second_char = grid[second_r][second_c]

	to_move.append((check_r, check_c, box_char))       # add first bracket
	to_move.append((second_r, second_c, second_char))  # add second bracket

	is_movable = True

	# Checks for verticals
	if dr != 0:
		# Check behind the first bracket
		if grid[check_r + dr][check_c + dc] == '#':
			is_movable = False
		elif grid[check_r + dr][check_c + dc] == '.':
			pass
		elif grid[check_r + dr][check_c + dc] in '[]':
			if check_boxes(grid, check_r + dr, check_c + dc, dr, dc, to_move) == False:
				is_movable = False
		
		# Check behind the second bracket
		if grid[second_r + dr][second_c + dc] == '#':
			is_movable = False
		elif grid[second_r + dr][second_c + dc] == '.':
			pass
		elif grid[second_r + dr][second_c + dc] in '[]':
			if check_boxes(grid, second_r + dr, second_c + dc, dr, dc, to_move) == False:
				is_movable = False
	# Checks for horizontals
	elif dc != 0:
		# Second bracket is always behind the first bracket in horizontal moves
		# So to check behind the box, just check behind the second bracket
		if grid[second_r + dr][second_c + dc] == '#':
			is_movable = False
		elif grid[second_r + dr][second_c + dc] == '.':
			pass
		elif grid[second_r + dr][second_c + dc] in '[]':
			if check_boxes(grid, second_r + dr, second_c + dc, dr, dc, to_move) == False:
				is_movable = False
	return is_movable


def part2(grid, moves):
	# Process map
	new_grid = []
	for r, row in enumerate(grid):
		new_row = ''
		for c, ch in enumerate(row):
			if ch == '#': new_row += '##'
			elif ch == 'O': new_row += '[]'
			elif ch == '.': new_row += '..'
			elif ch == '@': new_row += '@.'
		new_grid.append(new_row)
	# pprint.pp(grid)
	grid = new_grid
	# Find robot
	rr = rc = 0
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if ch == '@':
				rr, rc = r, c
	# Move boxes
	for move in moves:
		# pprint.pp(grid)
		# print('Move', move)
		dr, dc = dir_offsets[move][0], dir_offsets[move][1]
		check_r, check_c = rr + dr, rc + dc
		if grid[check_r][check_c] == '.':
			change_char(grid, rr, rc, '.')  # move the robot
			change_char(grid, check_r, check_c, '@')
			rr, rc = check_r, check_c
			continue
		elif grid[check_r][check_c] == '#':
			continue
		elif grid[check_r][check_c] in '[]':
			to_move = []
			is_movable = check_boxes(grid, check_r, check_c, dr, dc, to_move)
			if is_movable:
				# Move all boxes
				for movable in to_move:
					change_char(grid, movable[0], movable[1], '.')
				for movable in to_move:
					change_char(grid, movable[0] + dr, movable[1] + dc, movable[2])
				# Move the robot
				change_char(grid, rr, rc, '.')
				change_char(grid, check_r, check_c, '@')
				rr, rc = check_r, check_c
	# pprint.pp(grid)
	# Find result
	gps_sum = 0
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if ch == '[':
				gps_sum += r * 100 + c
	print(gps_sum)


def main():
	original_grid, moves = parse_input()
	part1(original_grid.copy(), moves)
	part2(original_grid.copy(), moves)


if __name__ == '__main__':
	main()
