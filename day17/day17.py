# Advent of Code - Day 17


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
	output = ''
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
			output += str(get_combo_operand_val(p[ip+1]) % 8)
			output += ','
		elif opcode == 6:
			b = a // 2**get_combo_operand_val(p[ip+1])
		elif opcode == 7:
			c = a // 2**get_combo_operand_val(p[ip+1])
		ip += 2
	if len(output) > 0:
		output = output[:-1]
	return output


def part1(a,b,c,p):
	print(sim_computer(a,b,c,p))


def part2(a,b,c,p):
	b=c=0
	
	a = 0
	output_int_list = []
	
	while p != output_int_list:
		a += 1
		# a = 117440 # debug
		if a % 1_000_000 == 0:
			print(f'Checking for a = {a}...')
		output = sim_computer(a,b,c,p)
		
		output_int_list = []
		for num_str in output.split(','):
			if num_str != '':
				output_int_list.append(int(num_str))
		# exit(0) # debug	
	print(f'p == output_int_list when a = {a}')


def main():
	a,b,c,p = parse_input()
	part1(a,b,c,p)
	part2(a,b,c,p)


if __name__ == '__main__':
	main()
