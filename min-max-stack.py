"""
    Write a MinMaxStack class for a Min Max Stack. The class should support:
        - Pushing and popping values on and off the stack
        - Peeking at the value at the top of the stack
        - Getting both the minimum and maximum value in the stack at any 
            given point in time
    All class methods, when considered independently, should run in constant 
        time with constant space
"""
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_max_stack = []

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def pop(self):
        if len(self.stack) > 0:
            del self.min_max_stack[-1]
            return self.stack.pop()
        return None

    def push(self, number):
        if len(self.stack) > 0:
            min_num = number if number < self.getMin() else self.getMin()
            max_num = number if number > self.getMax() else self.getMax()
        else:
            min_num = number
            max_num = number

        stack_elem = {"min": min_num, "max": max_num}
        self.min_max_stack.append(stack_elem)
        self.stack.append(number)

    def getMin(self):
        if len(self.stack) > 0:
            return self.min_max_stack[-1]["min"]
        return None

    def getMax(self):
        if len(self.stack) > 0:
            return self.min_max_stack[-1]["max"]
        return None