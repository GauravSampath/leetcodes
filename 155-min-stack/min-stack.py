class MinStack(object):

    def __init__(self):
        self.stack= []

    def push(self, val):
       if not self.stack:
            self.stack.append((val,val))
       else:
            curr_min = min(val,self.stack[-1][1])
            self.stack.append((val,curr_min))
        

    def pop(self):
        self.stack.pop()

    def top(self):
       return self.stack[-1][0]
        

    def getMin(self):
        return self.stack[-1][1]        