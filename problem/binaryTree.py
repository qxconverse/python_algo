class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def get_val(self):
        return self.val

def print_node_list(l):
    print([i.get_val() for i in l])

class traverse:
    def first(self, root):
        if root:
            print(root.val)
            self.first(root.left)
            self.first(root.right)

    def first_none_r(self, root):
        s = [root]
        while len(s) > 0:
            root = s.pop()
            print(root.val)
            if root.right:
                s.append(root.right)
            if root.left:
                s.append(root.left)
        # s = []
        # while root != None or len(s) > 0:
        #     while root:
        #         s.append(root)
        #         print(root.val)
        #         root = root.left
        #     root = s.pop()
        #     root = root.right
        # print_node_list(s)


    def middle(self, root):
        if root:
            self.middle(root.left)
            print(root.val)
            self.middle(root.right)

    def middle_none_r(self, root):
        # 每次入一个时，再入它的左
        # 每次出一个时，就入它的右
        s = []
        while root != None or len(s) > 0:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            print(root.val)
            root = root.right


    def after(self, root):
        if root:
            self.after(root.left)
            self.after(root.right)
            print(root.val)

    def after_none_r(self, root):
        s = []
        while root != None or len(s) > 0:
            while root:
                s.append(root)
                root = root.left if root.left else root.right
            root = s.pop()
            print(root.val)
            if s and s[-1].left == root:
                root = s[-1].right
            else:
                root = None


    def bfs(self, root):
        q = []
        q.append(root)
        while len(q) > 0:
            print_node_list(q)
            print(q[0].val)
            node = q[0]
            q = q[1:]
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        



# 针对非递归的方法，在写代码或画图示时，注意几个点
# 1.始终已当前代码指针为核心
# 2.知当前代码指针对应在树上的哪个位置，有可能在一个空节点上
# 3.区别栈操作和打印的关系




p = TreeNode("A")
p2 = TreeNode("B")
p3 = TreeNode("C")
p4 = TreeNode("D")
p5 = TreeNode("E")
p6 = TreeNode("F")
p.left = p2
p.right = p3
p2.left = p4
p2.right = p5
p3.left = p6
t = traverse()

# print("------first------")
# t.first(p)

print("------first-none-r------")
t.first_none_r(p)

# print("------middle------")
# t.middle(p)

print("------middle-none-r------")
t.middle_none_r(p)

# print("------after------")
# t.after(p)

print("------after-none-r------")
t.after_none_r(p)


# print("------bfs------")
# t.bfs(p)
