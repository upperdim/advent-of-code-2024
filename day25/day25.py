from pprint import pp


w=5
h=7

def parse_input():
	with open('day25_input.txt') as f:
		things = f.read().split('\n\n')
	keys = []
	locks = []
	for thing in things:
		grid = thing.split('\n')
		
		if grid[0] == '#####':
			# Lock
			heights = []
			# Get height
			for c in range(w):
				height = 0
				for r in range(h):
					if grid[r][c] == '#':
						height += 1
				heights.append(height)
			locks.append(heights)
		else:
			# Key
			heights = []
			# Get height
			for c in range(w):
				height = 0
				for r in range(h):
					if grid[r][c] == '#':
						height += 1
				heights.append(height)
			keys.append(heights)
	return keys, locks


def part1(keys, locks):
	total_fitting = 0
	for k in keys:
		for l in locks:
			fits = True
			# For every column
			for c in range(w):
				if k[c] + l[c] > h:
					fits = False
					break
			if fits: total_fitting += 1
	print(total_fitting)


def part2(keys, locks):
	pass


def main():
	keys, locks = parse_input()
	part1(keys, locks)
	part2(keys, locks)


if __name__ == '__main__':
	main()
