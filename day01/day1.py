def parse_input():
	with open('day1_input.txt', encoding="utf8") as f:
		lines = [line.strip() for line in f.readlines()]
	l_list = []
	r_list = []
	for line in lines:
		splits = line.split('   ')
		l_list.append(int(splits[0]))
		r_list.append(int(splits[1]))
	return l_list, r_list


def part1(l_list, r_list):
	total_diff = 0
	for l, r in zip(l_list, r_list):
		diff = abs(l - r)
		total_diff += diff
	print(total_diff)


def part2(l_list, r_list):
	total_diff = 0
	for l, r in zip(l_list, r_list):
		r_list_occurrance_count = 0
		i = 0
		while i < len(r_list) and r_list[i] <= l:
			if r_list[i] == l:
				r_list_occurrance_count += 1
			i += 1
		new_diff = l * r_list_occurrance_count
		total_diff += new_diff
	print(total_diff)


def main():
	l_list, r_list = parse_input()
	l_list.sort()
	r_list.sort()
	part1(l_list, r_list)
	part2(l_list, r_list)


if __name__ == '__main__':
	main()
