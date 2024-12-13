# Advent of Code 2024 - Day 13


import pprint
from math import floor


def parse_input():
	a = []
	b = []
	p = []
	state = 'a'
	with open('day13_input.txt', encoding="utf8") as f:
		for line in f.readlines():
			if line == '\n':
				continue
			dx_start = line.find('X')
			dx, dy = line[dx_start:].split(', ')
			dx = int(dx[2:])
			dy = int(dy[2:])
			if state == 'a':
				a.append([dx, dy])
				state = 'b'
			elif state == 'b':
				b.append([dx, dy])
				state = 'p'
			elif state == 'p':
				p.append([dx, dy])
				state = 'a'
		return [a, b, p]


# na * dx_a + nb * dx_b = px
# na * dy_a + nb * dy_b = py
# na <= 100
# nb <= 100
def part1(arr):
	total_min_toks = 0
	for i in range(len(arr[0])):
		dx_a, dy_a = arr[0][i][0], arr[0][i][1]
		dx_b, dy_b = arr[1][i][0], arr[1][i][1]
		px  , py   = arr[2][i][0], arr[2][i][1]
		
		min_tok = None
		for na in range(100):
			for nb in range(100):
				# print(f'Checking {na}*{dx_a} + {nb}*{dx_b} == {px} and {na}*{dy_a} + {nb}*{dy_b} == {py}')
				if na*dx_a + nb*dx_b == px and na*dy_a + nb*dy_b == py:
					# print(f'FOUND:  {na}*{dx_a} + {nb}*{dx_b} == {px} and {na}*{dy_a} + {nb}*{dy_b} == {py}')
					curr_tok = (3 * na + nb)

					if min_tok is None or curr_tok < min_tok:
						min_tok = curr_tok

		if min_tok is not None:
			total_min_toks += min_tok
	print(total_min_toks)


def part2(arr):
	total_min_toks = 0
	for i in range(len(arr[0])):
		dx_a, dy_a = arr[0][i][0], arr[0][i][1]
		dx_b, dy_b = arr[1][i][0], arr[1][i][1]
		px  , py   = arr[2][i][0] + 10000000000000, arr[2][i][1] + 10000000000000

		na = (px * dy_b - py * dx_b) / (dx_a * dy_b - dy_a * dx_b)
		nb = (px - dx_a * na) / dx_b
		if floor(na) == na and floor(nb) == nb:
			curr_toks = na * 3 + nb
			total_min_toks += int(curr_toks)
	print(total_min_toks)


def main():
	arr = parse_input()
	part1(arr)
	part2(arr)


if __name__ == '__main__':
	main()