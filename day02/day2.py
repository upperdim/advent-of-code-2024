# One report per line
# Each number : level (separated by spaces)

# Safe report = either always increases or always decreases
# Difference of at least 1, at most 3 at a time

def is_report_valid(nums):
	# Determine direction
	is_ascending = None
	if nums[1] > nums[0]:
		is_ascending = True
	elif nums[1] < nums[0]:
		is_ascending = False
	else:
		return False
	
	# Check report
	is_safe_report = True
	for i in range(1,len(nums)):
		if is_ascending and nums[i] < nums[i - 1]:
			return False
		if not is_ascending and nums[i] > nums[i - 1]:
			return False

		diff = abs(nums[i] - nums[i - 1])
		if  diff < 1 or diff > 3:
			return False
	return True


def parse_input():
	with open('day2_input.txt', encoding="utf8") as f:
		lines = [line.strip() for line in f.readlines()]
	return lines


def part1(reports):
	safe_reports_count = 0
	for report in reports:
		nums = [int(num_s) for num_s in report.split(' ')]
		if is_report_valid(nums):
			safe_reports_count += 1
	print(safe_reports_count)


def part2(reports):
	safe_reports_count = 0
	for report in reports:
		nums = [int(num_s) for num_s in report.split(' ')]
		if is_report_valid(nums):
			safe_reports_count += 1
			continue
		# Handle invalid report, try removing each element and check validity
		for i in range(len(nums)):
			nums_removed = nums.copy()
			nums_removed.pop(i)
			if is_report_valid(nums_removed):
				safe_reports_count += 1
				break
	print(safe_reports_count)


def main():
	reports = parse_input()
	part1(reports)
	part2(reports)


if __name__ == '__main__':
	main()
