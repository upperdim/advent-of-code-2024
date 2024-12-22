from pprint import pp


def parse_input():
	with open('day22_input.txt', encoding="utf8") as f:
		lines = [line.strip() for line in f.readlines()]
	return lines


def prune(secret):
	return secret % 16777216


def mix(val, secret):
	return val ^ secret


def next_secret(old_secret):
	tmp = old_secret * 64
	tmp2 = mix(tmp, old_secret)
	new_secret = prune(tmp2)

	tmp = new_secret // 32
	tmp2 = mix(tmp, new_secret)
	new_secret = prune(tmp2)

	tmp = new_secret * 2048
	tmp2 = mix(tmp, new_secret)
	new_secret = prune(tmp2)

	return new_secret


def part1(lines):
	total = 0
	for line in lines:
		secret = int(line)
		for i in range(2000):
			secret = next_secret(secret)
		total += secret
	print(f'Part 1 = {total}')


def part2(lines):
	seq_to_bananas = {}
	# Process each buyer
	for line in lines:
		# Get prices
		secret = int(line)
		buyer_prices = []
		for i in range(2000):
			secret = next_secret(secret)
			buyer_prices.append(secret % 10)
		# Save visited price change sequences
		seen_price_change_seqs = set()
		# Get price change sequences
		for i in range(4, len(buyer_prices)):
			price_change_seq = (
				buyer_prices[i    ] - buyer_prices[i - 1],
				buyer_prices[i - 1] - buyer_prices[i - 2],
				buyer_prices[i - 2] - buyer_prices[i - 3],
				buyer_prices[i - 3] - buyer_prices[i - 4]
			)
			# Same price change sequence can't be considered again
			# It would have been sold at the first encounter 
			if price_change_seq in seen_price_change_seqs:
				continue
			# Save seen price change sequence
			seen_price_change_seqs.add(price_change_seq)
			# Price change sequence eligible for selling, update banana gain amount for the seq
			if price_change_seq not in seq_to_bananas:
				seq_to_bananas[price_change_seq] = buyer_prices[i]
			else:
				seq_to_bananas[price_change_seq] += buyer_prices[i]
	max_bananas = -1
	for bananas in seq_to_bananas.values():
		if bananas > max_bananas:
			max_bananas = bananas
	print(f'Part 2 = {max_bananas}')


def main():
	lines = parse_input()
	part1(lines)
	part2(lines)


if __name__ == '__main__':
	main()
