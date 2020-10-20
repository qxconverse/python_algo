class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def tree_node_to_string(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def string_to_tree_node(input_str):
    input_str = input_str.strip()
    input_str = input_str[1:-1]
    if not input_str:
        return None

    input_values = [s.strip() for s in input_str.split(',')]
    root = TreeNode(int(input_values[0]))
    node_queue = [root]
    front = 0
    index = 1
    while index < len(input_values):
        node = node_queue[front]
        front = front + 1

        item = input_values[index]
        index = index + 1
        if item != "null":
            left_number = int(item)
            node.left = TreeNode(left_number)
            node_queue.append(node.left)

        if index >= len(input_values):
            break

        item = input_values[index]
        index = index + 1
        if item != "null":
            right_number = int(item)
            node.right = TreeNode(right_number)
            node_queue.append(node.right)
    return root


def pre_order(root):
    stack = []
    cur = root

    while cur or len(stack) != 0:
        while cur:
            print(cur.val)
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        cur = cur.right


def in_order(root):
    stack = []
    cur = root

    while cur or len(stack) != 0:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        print(cur.val)
        cur = cur.right


def post_order(root):
    stack = []
    cur = root
    prev = None

    while cur or len(stack) != 0:
        while cur:
            stack.append(cur)
            cur = cur.left

        top = stack[-1]
        # 如果存在右节点，并且还没有访问，则设置当前节点为栈顶节点的右节点
        if top.right and prev != top.right:
            cur = top.right
        else:
            print(top.val)
            prev = top
            stack.pop()


def post_order2(root):
    stack = []
    prev = None
    stack.append(root)

    while len(stack) != 0:
        cur = stack[-1]
        # 如果左右节点都存在，那么只需要看prev是否是右节点即可，因为一定是先出左节点，后出右节点（入栈是反的原因）
        # 那么什么时候回看prev是否是左节点呢？当右节点为空的时候！
        if (not cur.left and not cur.right) or (prev and (prev == cur.left or prev == cur.right)):
            print(cur.val)
            prev = cur
            stack.pop()
        else:
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)


def level_order(root):
    queue = [root]
    while queue:
        # 取队首节点
        top = queue.pop(0)
        print(top.val)
        if top.left:
            queue.append(top.left)
        if top.right:
            queue.append(top.right)


def main():
    line = '[8,7,5,4,null,1,6]'
    p = string_to_tree_node(line)
    level_order(p)
    # ret = tree_node_to_string(p)
    # print(ret)


if __name__ == '__main__':
    main()
