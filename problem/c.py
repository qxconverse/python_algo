class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def get_val(self):
        return self.val

class traverse:
    def first(self, root):
        s = []
        while root or s:
            while root:
                s.append(root)
                print(root.val)
                root = root.left
            root = s.pop()
            root = root.right
    
    def middle(self, root):
        s = []
        while root or s:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            print(root.val)
            root = root.right

    def after(self, root):
        s = []
        while root or s:
            while root:
                s.append(root)
                root = root.left if root.left else root.right
            root = s.pop()
            print(root.val)
            # 如果当前pop出来的节点是栈顶的左节点，则指针指向pop出的节点的右节点
            if s and s[-1].left == root:
                root = s[-1].right
            else:
                root = None

    def bfs(self, root):
        q = []
        q.append(root)
        while q:
            root = q[0]
            print(root.val)
            q = q[1:]
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)

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

print("------first-none-r------")
t.first(p)

print("------middle-none-r------")
t.middle(p)

print("------after-none-r------")
t.after(p)

print("------bfs------")
t.bfs(p)
