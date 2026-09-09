class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for ast in asteroids:
            alive = True
            while stack and stack[-1] > 0 and ast < 0:
                if stack[-1] < abs(ast):
                    stack.pop() 
                    continue
                elif stack[-1] == abs(ast):
                    stack.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break
            if alive:
                stack.append(ast)
        return stack
