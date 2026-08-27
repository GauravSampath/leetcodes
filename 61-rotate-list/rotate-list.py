class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        val = []
        curr = head
        while curr:
            val.append(curr.val)
            curr = curr.next
        n = len(val)
        k = k%n
        if k == 0:
            return head
        rotated_val = val[-k:] + val[:-k]
        curr = head
        for num in rotated_val:
            head.val = num
            head = head.next
        return curr

       