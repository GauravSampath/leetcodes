class Solution(object):
    def sortList(self, head):
        l = []
        curr = head
        while head:
            l.append(head.val)
            head = head.next
        
        l.sort()
        count = 0
        head = curr
        while head:
            head.val = l[count]
            head = head.next
            count += 1
        
        return curr