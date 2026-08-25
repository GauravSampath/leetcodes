class Solution(object):
    def detectCycle(self, head):
       visited = set()
       temp = head
       while temp:
        if temp in visited:
            return temp
        visited.add(temp)
        temp = temp.next
       return temp
    
        