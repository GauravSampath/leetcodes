class Solution(object):
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None
        slow = head
        fast = head.next.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head