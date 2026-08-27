class Solution(object):
    def addTwoNumbers(self, l1, l2):
        res = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            carry, val = divmod(carry + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            n.next = n = ListNode(val)
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        return res.next