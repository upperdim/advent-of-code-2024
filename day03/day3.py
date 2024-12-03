# Advent of Code 2024 - Day 3


import re


def parse_input():
	line = ''
	with open('day3_input.txt', encoding="utf8") as f:
		for curr_line in f:
			line += curr_line
	return line


def part1(line):
	results_sum = 0
	muls = [match.start() for match in re.finditer(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line)]
	for i in muls:
		op1 = int(line[line.find('(', i) + 1 : line.find(',', i)])
		op2 = int(line[line.find(',', i) + 1 : line.find(')', i)])
		results_sum += op1 * op2
	print(f'{results_sum}')


def part2(line):
	results_sum = 0
	dos = [match.start() for match in re.finditer(r"do\(\)", line)]
	donts = [match.start() for match in re.finditer(r"don't\(\)", line)]
	muls = [match.start() for match in re.finditer(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line)]
	for i in muls:
		do_operation = True
		# Find the first instruction before current multiplication. If none, do it.
		for j in range(i - 1, -1, -1):
			if j in dos:
				break
			if j in donts:
				do_operation = False
				break
		if do_operation:
			op1 = int(line[line.find('(', i) + 1 : line.find(',', i)])
			op2 = int(line[line.find(',', i) + 1 : line.find(')', i)])
			results_sum += op1 * op2
	print(f'{results_sum}')


def main():
	line = parse_input()
	part1(line)
	part2(line)


if __name__ == '__main__':
	main()
