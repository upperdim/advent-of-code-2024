# Advent of Code - Day 17


from pprint import pp


a = -1
b = -1
c = -1
p = None
ip = 0
def parse_input():
	with open('day17_input.txt', encoding="utf8") as f:
		lines = [line.strip() for line in f.readlines()]
	a=b=c=p=None
	state = 'a'
	for line in lines:
		if line == '':
			continue
		
		if state == 'a':
			a = int(line.split(': ')[1])
			state = 'b'
			continue
		if state == 'b':
			b = int(line.split(': ')[1])
			state = 'c'
			continue
		if state == 'c':
			c = int(line.split(': ')[1])
			state = 'p'
			continue
		if state == 'p':
			p_str = line.split(': ')[1]
			p = [int(num_str) for num_str in p_str.split(',')]
	return a,b,c,p


def sim_computer(a, b, c, p):
	def get_combo_operand_val(operand):
		if operand in [0,1,2,3]: 	return operand
		elif operand == 4: 			return a
		elif operand == 5: 			return b
		elif operand == 6: 			return c
		elif operand == 7: 			raise Exception('operand 7 encountered!')

	ip = 0
	output = []
	part2_output_count = 0
	while ip < len(p):
		# Fetch
		opcode = p[ip]
		# print(f'Fetched instruction {opcode} from {ip}')

		# Decode & execute
		if opcode == 0:
			a = a // 2**get_combo_operand_val(p[ip+1])
		elif opcode == 1:
			b = b ^ p[ip+1]
		elif opcode == 2:
			b = get_combo_operand_val(p[ip+1]) % 8
		elif opcode == 3:
			if a != 0:
				ip = p[ip+1]
				continue  # don't increment IP
		elif opcode == 4:
			b = b ^ c
		elif opcode == 5:
			output_num = get_combo_operand_val(p[ip+1]) % 8
			output.append(output_num)
		elif opcode == 6:
			b = a // 2**get_combo_operand_val(p[ip+1])
		elif opcode == 7:
			c = a // 2**get_combo_operand_val(p[ip+1])
		ip += 2
	return output


def part1(a,b,c,p):
	print(sim_computer(a,b,c,p))


def part2(a,b,c,p):
	b=c=0

	# Populate valid a's for the first output	
	valids = []
	for a in range(2**10):  # First 10 bits matter, later on 3 bits per output
		if p[0] == sim_computer(a,b,c,p)[0]:
			valids.append(a)
	
	# For each instruction in program
	for i in range(1, len(p)):
		curr_valids = []
		# Filter valids for current instruction from valids of previous instruction 
		for valid in valids:
			# 3 bits of a is added per instruction
			for bits in range(8):
				# Append new bits to the left of a to obtain check_a
				check_a = (bits << 7 + (i*3)) | valid
				# Check it
				out = sim_computer(check_a,b,c,p)
				if len(out) > i and p[i] == out[i]:
					curr_valids.append(check_a)  # Save if satisfies
		# Filter valids only to ones that also satisfied this instruction
		valids = curr_valids
	print(min(valids))  # We want minimum a that satisfies


def main():
	a,b,c,p = parse_input()
	part1(a,b,c,p)
	part2(a,b,c,p)


if __name__ == '__main__':
	main()
