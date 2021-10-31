# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []
    
    def push(self, node):
        # write code here
        while self.stack_pop:
            self.stack_push.append(self.stack_pop.pop())
        self.stack_push.append(node)
        
    def pop(self):
        # return xx
        while self.stack_push:
            self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop.pop()