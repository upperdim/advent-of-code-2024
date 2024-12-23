from pprint import pp


def parse_input():
	with open('day19_input.txt', encoding="utf8") as f:
		lines = [line.strip() for line in f.readlines()]
	towels = lines[0].split(', ')
	patterns = [line for line in lines[2:]]
	return towels, patterns


def is_possible(pattern, towels):
	if pattern == '':
		return True
	for towel in towels:
		if towel == pattern[:len(towel)]:
			if is_possible(pattern[len(towel):], towels):
				return True
	return False


def part1(towels, patterns):
	possible_count = 0
	for pattern in patterns: 
		if is_possible(pattern, towels):
			possible_count += 1
	print(f'Possible = {possible_count}')


def part2(towels, patterns):
	pass


def main():
	towels, patterns = parse_input()
	part1(towels, patterns)
	part2(towels, patterns)


if __name__ == '__main__':
	main()
