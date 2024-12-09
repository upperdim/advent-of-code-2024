# Advent of Code 2024 - Day 8


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
	# Sarch files
	for i in range(len(disk) - 1, -1, -1):
		# Found file
		if i > move_file_to_idx and disk[i] != '.':
			# Move file
			disk[move_file_to_idx] = disk[i]
			disk[i] = '.'
			# Update available space idx
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
	# Move files starting from the end
	i = len(disk) - 1
	while i >= 0:
		# print(f'{disk} i={i} len={len(disk)}')
		# print(f'old i = {i} pointing at {disk[i]}')

		# Found file 
		if disk[i] != '.':
			file_id_to_move = disk[i]
			# Find length of the file
			file_len = 0
			for j in range(i, -1, -1):
				if disk[j] == disk[i]:
					file_len += 1
				else:
					break
			# Discover fitting space from the beginning
			found_suiting_space = False
			space_begin_idx = 0
			space_end_idx = 0
			inside_space = False
			for j in range(0, len(disk)):
				if j >= i:
					break
				if not inside_space and disk[j] == '.':
					inside_space = True
					space_begin_idx = j
					continue
				if inside_space and disk[j] != '.':
					inside_space = False
					space_end_idx = j - 1
					space_len = space_end_idx - space_begin_idx + 1
					if space_len >= file_len:
						# Found suiting space
						# print(f'found suitable space [{space_begin_idx}, {space_end_idx}]')
						found_suiting_space = True
						break
			if found_suiting_space:
				# Copy files to space
				if file_len > space_len:
					print(f'file len > space len!')
					exit(0)
				for j in range(file_len):
					# print(f'Copying file {disk[i-j]} from {i-j} to {space_begin_idx+j}')
					disk[space_begin_idx + j] = disk[i - j]
					disk[i - j] = '.'
			else:
				# print(f'couldn\'t find suitable place')
				i -= file_len
				continue
		# print(f'new i = {i} pointing at {disk[i]}')
		i -= 1
	checksum = 0
	for i in range(len(disk)):
		if disk[i] != '.':
			checksum += disk[i] * i
	print(checksum)


def main():
	lines = parse_input()
	part1(lines)
	part2(lines)


if __name__ == '__main__':
	main()
