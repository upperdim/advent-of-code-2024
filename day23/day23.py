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
	# Map of each computer holding a set of connected computers
	conns = {}

	edges = set()
	for conn in lines:
		c1,c2 = conn.split('-')
		if c1 not in conns: conns[c1] = set()
		if c2 not in conns: conns[c2] = set()
		conns[c1].add(c2)
		conns[c2].add(c1)
		edges.add((c1,c2))
		edges.add((c2,c1))

	nodes = []
	for conn in conns.keys():
		nodes.append(conn)
	nodes.sort()

	# Schedule a visit starting from all nodes
	to_visit = []
	for node in nodes:
		to_visit.append([node])

	largest_node_chain = ()  # target, keep track of largest circle
	while len(to_visit) > 0:
		# Visited the node
		curr_visit_node_chain = to_visit.pop()

		# Update if current node chain is longer
		if len(curr_visit_node_chain) > len(largest_node_chain):
			largest_node_chain = curr_visit_node_chain

		# Check all for eligible nodes to visit
		for check_node in nodes:
			if check_node > curr_visit_node_chain[-1]:
				is_connected = True

				# If it's not connected to any of the current chain, it's not an interconnection
				for curr_chain_node in curr_visit_node_chain:
					if (check_node, curr_chain_node) not in edges:
						is_connected = False
						break

				# Add it to the current chain
				if is_connected:
					to_visit.append(curr_visit_node_chain + [check_node])  # Append to the end of the list
	
	print('Part 2 =', str(sorted(largest_node_chain)).replace('\'', '').replace(' ', '')[1:-1])


def main():
	lines = parse_input()
	part1(lines)
	part2(lines)


if __name__ == '__main__':
	main()
