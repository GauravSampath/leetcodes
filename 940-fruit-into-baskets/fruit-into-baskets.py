class Solution(object):
    def totalFruit(self, fruits):
        from collections import Counter
        fruit_map = Counter()
        n = len(fruits)
        l = 0
        ans = 0
        for r in range(n):
            fruit_map[fruits[r]] += 1
            while len(fruit_map) > 2:
                    left_fruit = fruits[l]
                    fruit_map[left_fruit] -= 1
                    if fruit_map[left_fruit] == 0:
                        del fruit_map[left_fruit]
                    l += 1
            ans = max(ans,r-l+1)
        return ans
        