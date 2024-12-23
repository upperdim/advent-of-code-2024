from pprint import pp


def parse_input():
	with open('day23_input.txt', encoding="utf8") as f:
		lines = [line.strip() for line in f.readlines()]
	return lines


def part1(lines):
	# Map of each computer holding a set of connected computers
	conns = {}
	for conn in lines:
		c1,c2 = conn.split('-')
		if c1 not in conns: conns[c1] = set()
		if c2 not in conns: conns[c2] = set()
		conns[c1].add(c2)
		conns[c2].add(c1)
	circles = set()
	for c1 in conns:
		for c2 in conns[c1]:
			for c3 in conns[c2]:
				if c1 in conns[c3] and c3 != c1:
					if c1[0] == 't' or c2[0] == 't' or c3[0] == 't':
						circle = [c1, c2, c3]
						circle.sort()  # Avoid duplicates
						circles.add(tuple(circle))
	print(f'Part 1 = {len(circles)}')


def part2(lines):
	pass


def main():
	lines = parse_input()
	part1(lines)
	part2(lines)


if __name__ == '__main__':
	main()
