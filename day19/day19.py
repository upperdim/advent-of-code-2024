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


possibility_counts = {}
def get_possibility_count(pattern, towels):
	if pattern in possibility_counts:
		return possibility_counts[pattern]

	possibility_count = 0
	for towel in towels:
		if pattern == towel:
			possibility_count += 1
		if towel == pattern[:len(towel)]:
			possibility_count += get_possibility_count(pattern[len(towel):], towels)
	
	possibility_counts[pattern] = possibility_count
	return possibility_count


def part2(towels, patterns):
	total_possibility_count = 0
	for pattern in patterns:
		possibility_count = get_possibility_count(pattern, towels)
		total_possibility_count += possibility_count
	print(f'Total Possibility Count = {total_possibility_count}')


def main():
	towels, patterns = parse_input()
	part1(towels, patterns)
	part2(towels, patterns)


if __name__ == '__main__':
	main()
