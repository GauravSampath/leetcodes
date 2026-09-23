class Solution(object):
    def totalNumbers(self, digits):
        numbers = set()
        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                numbers.add((a, b, c))
        return len(numbers)