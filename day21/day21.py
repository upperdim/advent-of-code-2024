from pprint import pp


def parse_input():
	with open('day21_input.txt', encoding="utf8") as f:
		lines = [line.strip() for line in f.readlines()]
	return lines


door_keys_r_c = {
	'7': (0,0), '8': (0,1), '9': (0,2),
	'4': (1,0), '5': (1,1), '6': (1,2),
	'1': (2,0), '2': (2,1), '3': (2,2),
	' ': (3,0), '0': (3,1), 'A': (3,2)
}


dpad_keys_r_c = {
	' ': (0,0), '^': (0,1), 'A': (0,2),
	'<': (1,0), 'v': (1,1), '>': (1,2)
}


seqs = {}
def get_seq(src, dst):
	if (src, dst) in seqs:
		return seqs[(src, dst)]
	
	keypad = None
	if src in door_keys_r_c and dst in door_keys_r_c:
		keypad = door_keys_r_c
	else:
		keypad = dpad_keys_r_c
	
	src_r, src_c = keypad[src][0], keypad[src][1]
	dst_r, dst_c = keypad[dst][0], keypad[dst][1]
	
	dr = dst_r - src_r
	dc = dst_c - src_c
	
	r_str, c_str = None, None
	
	if dst_r >= src_r: r_str = 'v' * dr
	else:             r_str = '^' * -dr

	if dst_c >= src_c: c_str = '>' * dc
	else:             c_str = '<' * -dc
	
	bad_dr, bad_dc = keypad[' '][0] - src_r, keypad[' '][1] - src_c
	
	result = ''
	if (dc > 0 or (bad_dr == 0 and bad_dc == dc)) and (bad_dc != 0 or bad_dr != dr):
		result = r_str + c_str + 'A'
	else:
		result = c_str + r_str + 'A'
	
	seqs[(src, dst)] = result
	return result


lens = {}
def get_len(seq, depth):
	if (seq, depth) in lens:
		return lens[(seq, depth)]
	
	if depth == 0:
		return len(seq)
	
	l = 0
	for i, ch in enumerate(seq):
		subseq_for_char = None
		if i == 0:
			subseq_for_char = get_seq('A', ch)
		else:
			subseq_for_char = get_seq(seq[i-1], ch)
		l += get_len(subseq_for_char, depth-1)
	
	lens[(seq, depth)] = l
	return l


def part1(lines):
	sum_of_complexities = 0
	for door_seq in lines:
		l = get_len(door_seq, 3)
		numeric_part = int(door_seq[:3])
		sum_of_complexities += l * numeric_part
	print(f'Part 1 = {sum_of_complexities}')


def part2(lines):
	sum_of_complexities = 0
	for door_seq in lines:
		l = get_len(door_seq, 26)
		numeric_part = int(door_seq[:3])
		sum_of_complexities += l * numeric_part
	print(f'Part 2 = {sum_of_complexities}')


def main():
	lines = parse_input()
	part1(lines)
	part2(lines)


if __name__ == '__main__':
	main()
