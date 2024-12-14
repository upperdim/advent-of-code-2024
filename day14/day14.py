# Advent of Code 2024 - Day 14


def parse_input():
	ps = []
	vs = []
	with open('day14_input.txt', encoding="utf8") as f:
		lines = [line.strip() for line in f.readlines()]
	for line in lines:
		p_str, v_str = line.split(' ')

		p_str_mid_idx = p_str.find(',')
		ps.append([int(p_str[2:p_str_mid_idx]), int(p_str[p_str_mid_idx+1:])])

		v_str_mid_idx = v_str.find(',')
		vs.append([int(v_str[2:v_str_mid_idx]), int(v_str[v_str_mid_idx+1:])])
	return ps, vs


def part1(ps, vs):
	w = 101  # width
	h = 103  # height
	t = 100  # time
	for i in range(len(ps)):
		ps[i][0] = (ps[i][0] + vs[i][0] * t) % w
		ps[i][1] = (ps[i][1] + vs[i][1] * t) % h
	vert_mid_idx = h // 2
	horiz_mid_idx = w // 2
	q1 = q2 = q3 = q4 = 0
	for i in range(len(ps)):
		if ps[i][0] < horiz_mid_idx and ps[i][1] < vert_mid_idx:
			q2 += 1
		elif ps[i][0] > horiz_mid_idx and ps[i][1] < vert_mid_idx:
			q1 += 1
		elif ps[i][0] < horiz_mid_idx and ps[i][1] > vert_mid_idx:
			q3 += 1
		elif ps[i][0] > horiz_mid_idx and ps[i][1] > vert_mid_idx:
			q4 += 1
	safety_factor = q1 * q2 * q3 * q4
	print(f"{safety_factor}")


def check_robot_at(ps, x, y):
	for i in range(len(ps)):
		if ps[i][0] == x and ps[i][1] == y:
			return True
	return False


def is_xmas_tree(ps, w, h):
	tree_height = 7
	# Check entire grid
	for y in range(h - tree_height):
		for x in range(w):
			# For each coordinate, check for a vertical line
			is_tree = True
			for y_offset in range(tree_height):
				if check_robot_at(ps, x, y + y_offset) == False:
					is_tree = False
					break
			if is_tree:
				return True
			else:
				continue
	return False


def print_map(ps, w, h):
	for y in range(h):
		for x in range(w):
			if check_robot_at(ps, x, y):
				print('#', end='')
			else:
				print('.', end='')
		print('')


def part2(ps, vs):
	w = 101  # width
	h = 103  # height
	t = 100  # time
	while not is_xmas_tree(ps, w, h):
		for i in range(len(ps)):
			ps[i][0] = (ps[i][0] + vs[i][0]) % w
			ps[i][1] = (ps[i][1] + vs[i][1]) % h
		t += 1
	print_map(ps, w, h)
	print(f"{t}")


def main():
	ps, vs = parse_input()
	part1(ps, vs)
	part2(ps, vs)


if __name__ == '__main__':
	main()
