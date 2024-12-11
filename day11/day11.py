# Advent of Code 2024 - Day 11


import pprint


def parse_input():
	with open('day11_input.txt', encoding="utf8") as f:
		lines = [line.strip() for line in f.readlines()]
	return lines


def part1(lines):
	line = lines[0]
	stones = [int(num) for num in line.split(' ')]
	for blink in range(25):
		i = 0
		while i < len(stones):
			if stones[i] == 0:
				stones[i] = 1
			elif len(str(stones[i])) % 2 ==0:
				stone_str = str(stones[i])
				l = stone_str[:len(stone_str) // 2]
				r = stone_str[len(stone_str) // 2:]
				stones[i] = int(l)
				stones.insert(i+1, int(r))
				i += 1
			else:
				stones[i] *= 2024
			i += 1
	print(f'stone count = {len(stones)}')


stone_counts = {}
def get_stone_count(stone, blink_count):
	result = None
	# Memory
	if (stone, blink_count) in stone_counts:
		return stone_counts[(stone, blink_count)]
	# Terminal condition
	if blink_count == 0:
		result = 1
	# Calculation
	elif stone == 0:
		result = get_stone_count(1, blink_count - 1)
	elif len(str(stone)) % 2 == 0:
		stone_str = str(stone)
		l = stone_str[:len(stone_str) // 2]
		r = stone_str[len(stone_str) // 2:]
		result =  get_stone_count(int(l), blink_count - 1) + get_stone_count(int(r), blink_count - 1)
	else:
		result = get_stone_count(stone * 2024, blink_count - 1)
	# Save
	stone_counts[(stone, blink_count)] = result
	return result


def part2(lines):
	# print(f'began')
	line = lines[0]
	stones = [int(num) for num in line.split(' ')]
	stone_count = 0
	# print(stones)
	for stone in stones:
		# print(f'calculating for stone {stone} = ', end='')
		result = get_stone_count(stone, 75)
		stone_count += result
		# print(f'{result}')
	print(f'stone count = {stone_count}')


def main():
	lines = parse_input()
	part1(lines)
	part2(lines)


if __name__ == '__main__':
	main()
