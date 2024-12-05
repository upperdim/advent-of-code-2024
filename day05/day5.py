# Advent of Code 2024 - Day 5


def parse_input():
	with open('day5_input.txt', encoding="utf8") as f:
		lines = [line.strip() for line in f.readlines()]

	rules_str = []
	page_updates_str = []
	updates_state = False
	for line in lines:
		if line == '':
			updates_state = True
			continue
		if updates_state:
			page_updates_str.append(line)
		else:
			rules_str.append(line)

	rules = []
	for rule_str in rules_str:
		rules.append([int(num) for num in rule_str.split('|')])

	page_updates = []
	for page_update_str in page_updates_str:
		page_updates.append([int(num) for num in page_update_str.split(',')])

	return rules, page_updates


# X|Y -> x before Y
# add middle page numbers of correct page_updates
def part1(rules, page_updates):
	print(f'rules:\n{rules}\n\npage_updates:\n{page_updates}\n')
	rules_map = {}
	for rule in rules:
		rules_map[rule[0]] = []
	for rule in rules:
		rules_map[rule[0]].append(rule[1])
	print(f'rules_map:\n{rules_map}\n')

	midpage_sum_of_valids = 0
	for page_update in page_updates:
		comes_before_dependency = False
		for i, page_nr in enumerate(page_update):
			# Check previous pages
			for j in range(0, i):
				# dependencies_arr_of_page_nr = rules_map[page_nr]
				if page_nr in rules_map and page_update[j] in rules_map[page_nr]:
					# print(f'comes before dependency')
					comes_before_dependency = True
					break
			if comes_before_dependency:
				break
		if not comes_before_dependency:
			# No page before it's dependency, find mid page
			midpage_idx = (len(page_update) - 1) // 2
			print(f'found midpage {page_update[midpage_idx]} of page_update {page_update}')
			midpage_sum_of_valids += page_update[midpage_idx]
	print(midpage_sum_of_valids)


def part2(rules, page_updates):
	print(f'rules:\n{rules}\n\npage_updates:\n{page_updates}\n')
	rules_map = {}
	for rule in rules:
		rules_map[rule[0]] = []
	for rule in rules:
		rules_map[rule[0]].append(rule[1])
	print(f'rules_map:\n{rules_map}\n')

	midpage_sum_of_valids = 0
	for page_update in page_updates:
		comes_before_dependency = False
		for i, page_nr in enumerate(page_update):
			# Check previous pages
			j = 0
			while j < i:
				if page_nr in rules_map and page_update[j] in rules_map[page_nr]:
					# Order page
					page_update[i], page_update[j] = page_update[j], page_update[i]
					comes_before_dependency = True
				j += 1
		# For incorrect pages only
		if comes_before_dependency:
			midpage_idx = (len(page_update) - 1) // 2
			print(f'found midpage {page_update[midpage_idx]} of page_update {page_update}')
			midpage_sum_of_valids += page_update[midpage_idx]
	print(midpage_sum_of_valids)


def main():
	rules, page_updates = parse_input()
	part1(rules, page_updates)
	part2(rules, page_updates)


if __name__ == '__main__':
	main()
