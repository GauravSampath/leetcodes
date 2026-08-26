class Solution(object):
    def isPalindrome(self, head):
        values = []
        current = head
        while current is not None:
            values.append(current.val)
            current = current.next
        left = 0
        right = len(values)-1
        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        return True
        