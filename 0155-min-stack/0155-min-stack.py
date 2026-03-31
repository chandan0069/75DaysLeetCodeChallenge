class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return -1
        val=self.stack.pop()
        if val==self.min_stack[-1]:
            self.min_stack.pop()
        return val
    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return "Stack is empty"
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min_stack:
            return -1
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()