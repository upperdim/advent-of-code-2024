# Advent of Code 2024 - Day 7


from itertools import product, repeat


def parse_input():
	with open('day7_input.txt', 'r') as f:
		lines = [line.strip() for line in f.readlines()]
	return lines


def part1(lines):
	sum_of_correct_eqns = 0
	for eqn in lines:
		actual_result, operands = eqn.split(':')
		actual_result = int(actual_result)
		operands = [int(o) for o in operands[1:].split(' ')]

		operators = [0, 1]
		possibilities = list(product(  *([operators] * (len(operands)-1))  ))

		is_eqn_correct = False
		for possibility in possibilities:
			result = operands[0]
			for i in range(1, len(operands)):
				if possibility[i - 1] == 0:
					result = result + operands[i]
				if possibility[i - 1] == 1:
					result = result * operands[i]
			if result == actual_result:
				is_eqn_correct = True
				print(f'Correct eqn = {eqn}')
				break
		if is_eqn_correct:
			sum_of_correct_eqns += actual_result
	print(sum_of_correct_eqns)


def part2(lines):
	sum_of_correct_eqns = 0
	for eqn in lines:
		actual_result, operands = eqn.split(':')
		actual_result = int(actual_result)
		operands = [int(o) for o in operands[1:].split(' ')]

		operators = [0, 1, 2] # add, mult, concat
		possibilities = list(product(  *([operators] * (len(operands)-1))  ))

		is_eqn_correct = False
		for possibility in possibilities:
			result = operands[0]
			for i in range(1, len(operands)):
				if possibility[i - 1] == 0:
					result = result + operands[i]
				if possibility[i - 1] == 1:
					result = result * operands[i]
				if possibility[i - 1] == 2:
					result = int(str(result) + str(operands[i]))
			if result == actual_result:
				is_eqn_correct = True
				print(f'Correct eqn = {eqn}')
				break
		if is_eqn_correct:
			sum_of_correct_eqns += actual_result
	print(sum_of_correct_eqns)


def main():
	lines = parse_input()
	part1(lines)
	part2(lines)


if __name__ == '__main__':
	main()
