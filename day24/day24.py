from pprint import pp


def parse_input():
	with open('day24_input.txt', encoding="utf8") as f:
		lines = [line.strip() for line in f.readlines()]
	vals = {}
	gates = []
	state = 'b'
	for line in lines:
		if line == '':
			state = 'g'
			continue
		if state == 'b':
			varname, varval = line.split(': ')
			vals[varname] = int(varval)
		elif state == 'g':
			gates.append(line)
	return vals, gates


def part1(vals, gates):
	outputs = {}
	i = len(gates) - 1
	while len(gates) > 0:		
		var1, gate, var2, _, var_out = gates[i].split(' ')

		if var1 not in vals or var2 not in vals:
			i = 0 if i >= len(gates)-1 else i+1
			continue

		if gate == 'AND':
			vals[var_out] = vals[var1] & vals[var2]
		elif gate == 'OR':
			vals[var_out] = vals[var1] | vals[var2]
		elif gate == 'XOR':
			vals[var_out] = vals[var1] ^ vals[var2]
		else:
			raise Exception('UNEXPECTED GATE')
		gates.pop(i)
		if i >= len(gates):
			i = 0
	z_bin = ''
	for k in sorted(vals, reverse=True):
		if k[0] == 'z':
			z_bin += str(vals[k])
	print('Part 1 =', z_bin)


def change_char(s, i, replacement):
	l = list(s)
	l[i] = replacement
	s = ''.join(l)
	return s


def checks1(vals, gates):
	for i in range(len(gates)):
		var1, gate, var2, _, var_out = gates[i].split(' ')
		# If XOR input is not x,y; it has to output z
		if gate == 'XOR' and var_out[0] != 'z' and not ((var1[0] == 'x' and var2[0] == 'y') or (var1[0] == 'y' and var2[0] == 'x')):
			print(f'gate[{i}]\tdoesn\'t output z:\t\t\t{gates[i]}')
		# z can only be output of XOR except last z
		if var_out[0] == 'z' and gate != 'XOR':
			if var_out[1:] != '45':
				print(f'gate[{i}]\tz is not an output of XOR:\t\t{gates[i]}')


def checks2(vals, gates):
	xors_inputing_xy = []
	xors_outputing_z = []
	xors_outputing_z_inputs = []
	for i in range(len(gates)):
		var1, gate, var2, _, var_out = gates[i].split(' ')

		if gate == 'XOR':
			if var_out[0] == 'z':
				xors_outputing_z.append(gates[i])
				xors_outputing_z_inputs.append(var1)
				xors_outputing_z_inputs.append(var2)

			if ((var1[0] == 'x' and var2[0] == 'y') or (var1[0] == 'y' and var2[0] == 'x')):
				xors_inputing_xy.append(gates[i])

	for xor in xors_inputing_xy:
		var1, gate, var2, _, var_out = xor.split(' ')

		if var_out not in xors_outputing_z_inputs:
			if var1[1:] != '00':
				print(f'xor inputting x,y not outputting to xor outputting z:\t{xor}')


# Only helps for manual inspection
def part2(vals, gates):
	checks1(vals, gates)
	checks2(vals, gates)
	outputs = {}
	i = len(gates) - 1
	while len(gates) > 0:		
		var1, gate, var2, _, var_out = gates[i].split(' ')

		if var1 not in vals or var2 not in vals:
			i = 0 if i >= len(gates)-1 else i+1
			continue

		if gate == 'AND':
			vals[var_out] = vals[var1] & vals[var2]
		elif gate == 'OR':
			vals[var_out] = vals[var1] | vals[var2]
		elif gate == 'XOR':
			vals[var_out] = vals[var1] ^ vals[var2]
		else:
			raise Exception('UNEXPECTED GATE')
		gates.pop(i)
		if i >= len(gates):
			i = 0
	
	z_str, x_str, y_str = '', '', ''
	for k in sorted(vals, reverse=True):
		if k[0] == 'z': z_str += str(vals[k])
		elif k[0] == 'x': x_str += str(vals[k])
		elif k[0] == 'y': y_str += str(vals[k])
	x, y, z = int(x_str, 2), int(y_str, 2), int(z_str, 2)
	expected = bin(x + y)[2:]
	# pp(vals)
	# print(f'x_str    = {x_str}')
	# print(f'y_str    = {y_str}')

	print(f'z_str    = {z_str}')
	print(f'expected = {expected}')
	diff_idxs = []
	for i in range(len(z_str)):
		if z_str[i] != expected[i]:
			diff_idxs.append(len(z_str) - i - 1)
	print(f'diff_idxs = {diff_idxs}')


def main():
	vals, gates = parse_input()
	part1(vals.copy(), gates.copy())
	part2(vals, gates)


if __name__ == '__main__':
	main()
