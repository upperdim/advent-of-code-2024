# Advent of Code 2024 - Day 8


import pprint, math


def parse_input():
	with open('day8_input.txt', 'r') as file:
		grid = [line.replace('\n', '') for line in file]
	return grid


def dist(a, b):
	return math.sqrt( (b[1] - a[1])**2 + (b[0] - a[0])**2 )


def visualize_antinodes(grid, antinodes):
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if (r,c) in antinodes:
				print('#', end='')
			else:
				print('.', end='')
		print('')


def part1(grid):
	antennas = {}
	# Collect antenna information
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if ch.isalnum():
				if ch not in antennas:
					# create a key and add val
					antennas[ch] = [(r,c)]
				else:
					# append to coords val of map
					antennas[ch].append((r,c))
	pprint.pp(antennas)
	antinodes = set()
	for antenna in antennas.items(): # ('0', [(1, 8), (2, 5), (3, 7), (4, 4)])
		# Check for all antennas
		antenna_type = antenna[0]    #   0
		antenna_locs = antenna[1]    #       [(1, 8), (2, 5), (3, 7), (4, 4)]
		for i in range(len(antenna_locs)):
			for j in range(len(antenna_locs)):
				# print(f'comparing {antenna_locs[i]} and {antenna_locs[j]}')
				if i == j:
					# print(f'skipping...')
					continue
				a_loc1 = antenna_locs[i]
				a_loc2 = antenna_locs[j]
				dr = a_loc2[0] - a_loc1[0]
				dc = a_loc2[1] - a_loc1[1]

				antinode1_r = a_loc1[0] + 2*dr
				antinode1_c = a_loc1[1] + 2*dc

				antinode2_r = a_loc1[0] - dr
				antinode2_c = a_loc1[1] - dc

				if 0 <= antinode1_r < len(grid) and 0 <= antinode1_c < len(grid[0]):
					antinodes.add((antinode1_r, antinode1_c))
				if 0 <= antinode2_r < len(grid) and 0 <= antinode2_c < len(grid[0]):
					antinodes.add((antinode2_r, antinode2_c))
	visualize_antinodes(grid, antinodes)
	print('antinode count =', len(antinodes))
			

def part2(grid):
	antennas = {}
	# Collect antenna information
	for r, row in enumerate(grid):
		for c, ch in enumerate(row):
			if ch.isalnum():
				if ch not in antennas:
					# create a key and add val
					antennas[ch] = [(r,c)]
				else:
					# append to coords val of map
					antennas[ch].append((r,c))
	pprint.pp(antennas)
	antinodes = set()
	for antenna in antennas.items(): # ('0', [(1, 8), (2, 5), (3, 7), (4, 4)])
		# Check for all antennas
		antenna_type = antenna[0]    #   0
		antenna_locs = antenna[1]    #       [(1, 8), (2, 5), (3, 7), (4, 4)]
		for i in range(len(antenna_locs)):
			for j in range(len(antenna_locs)):
				# print(f'comparing {antenna_locs[i]} and {antenna_locs[j]}')
				if i == j:
					# print(f'skipping...')
					continue
				a_loc1 = antenna_locs[i]
				a_loc2 = antenna_locs[j]

				dr = a_loc2[0] - a_loc1[0]
				dc = a_loc2[1] - a_loc1[1]

				# Check + way
				check_r = a_loc1[0]
				check_c = a_loc1[1]
				while 0<=check_r<len(grid) and 0<=check_c<len(grid[0]):
					antinodes.add((check_r, check_c))
					check_r += dr
					check_c += dc

				# Check - way
				check_r = a_loc1[0]
				check_c = a_loc1[1]
				while 0<=check_r<len(grid) and 0<=check_c<len(grid[0]):
					antinodes.add((check_r, check_c))
					check_r -= dr
					check_c -= dc
				

				antinode1_r = a_loc1[0] + 2*dr
				antinode1_c = a_loc1[1] + 2*dc

				antinode2_r = a_loc1[0] - dr
				antinode2_c = a_loc1[1] - dc

				if 0 <= antinode1_r < len(grid) and 0 <= antinode1_c < len(grid[0]):
					antinodes.add((antinode1_r, antinode1_c))
				if 0 <= antinode2_r < len(grid) and 0 <= antinode2_c < len(grid[0]):
					antinodes.add((antinode2_r, antinode2_c))
	visualize_antinodes(grid, antinodes)
	print('antinode count =', len(antinodes))


def main():
	grid = parse_input()
	part1(grid)
	part2(grid)


if __name__ == '__main__':
	main()
