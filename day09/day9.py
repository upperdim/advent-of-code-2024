# Advent of Code 2024 - Day 8


import pprint, math


def parse_input():
	with open('day9_input.txt', encoding="utf8") as f:
		lines = [line.strip() for line in f.readlines()]
	return lines


def part1(lines):
	line = lines[0]

	file_id = 0
	disk = []
	for i, ch in enumerate(line):
		if i % 2 == 0:
			# File
			n_times = int(ch)
			for n in range(n_times):
				disk.append(file_id)
			file_id += 1
		else:
			# Space
			n_times = int(ch)
			for n in range(n_times):
				disk.append('.')
	move_file_to_idx = 0
	for i in range(len(disk)):
		if disk[i] == '.':
			move_file_to_idx = i
			break
	for i in range(len(disk) - 1, -1, -1):
		if i > move_file_to_idx and disk[i] != '.':
			disk[move_file_to_idx] = disk[i]
			disk[i] = '.'
			for j in range(move_file_to_idx + 1, len(disk)):
				if disk[j] == '.':
					move_file_to_idx = j
					break
	checksum = 0
	for i in range(len(disk)):
		if disk[i] != '.':
			checksum += disk[i] * i
	print(checksum)


def part2(lines):
	pass


def main():
	lines = parse_input()
	part1(lines)
	part2(lines)


if __name__ == '__main__':
	main()
