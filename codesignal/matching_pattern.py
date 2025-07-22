#!/usr/bin/python3
def solution(source, pattern):
	n = len(source)
	m = len(pattern)

	if m > n:return 0

	vowels = set('aeiou')
	def check_pattern(source, pattern, start):
		for j in range(m):
			if (pattern[j] == '0' and source[start+j] not in vowels) \
			or (pattern[j] == '1' and source[start+j] in vowels):
				return 0
		return 1

	return sum(check_pattern(source, pattern, i) for i in range(n-m+1))

if __name__ == "__main__":
	pattern = "01"
	source = "amazing"
	print(f"Solution: {solution(source, pattern)}")
