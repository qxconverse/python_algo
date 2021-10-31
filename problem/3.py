# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         # write code here
#         res = []
#         def f(node):
#             if rootode:
#                 res.append(node.val)
#                 f(node.next)
#         f(listNode)
#         return res


# s = Solution()
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n1.next = n2
# n2.next = n3
# print(s.printListFromTailToHead(n1))
        
class Solution:
    def print_linked_list(self, head):
        # 方法一：栈，两次遍历
        # # 边界判断
        # if head is None:
        #     return None
        # node_stack = []
        # cur = head
        # while cur:
        #     node_stack.append(cur)
        #     cur = cur.next
        # new_head = node_stack.pop()
        # cur = new_head
        # while node_stack:
        #     cur.next = node_stack.pop()
        #     cur = cur.next
        # # 一定要加，否则会死循环  
        # cur.next = None
        # return new_head

        # 方法二：递归
        # if head.next is None:
        #     return head
        # new_head = self.printLinkedList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head

        # 方法三：迭代
        cur = head
        tmp = None
        new_head = None
        while cur:
            tmp = cur.next # 保留现场
            cur.next = new_head # 反转
            new_head = cur # 重置头
            cur = tmp # 向前进
        return new_head

        
    def print_node(self, head):
        while head: 
            print(head.val)
            head = head.next

s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
new_head = s.print_linked_list(n1)
s.print_node(new_head)
