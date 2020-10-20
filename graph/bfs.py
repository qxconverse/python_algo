class Graph:
    def __init__(self, v, e, directed=True):
        self.v = v
        self.e = e
        self.adj_list = {}
        for vv in self.v:
            if directed:
                self.adj_list[vv] = [p[1] for p in self.e if p[0] == vv]
            else:
                self.adj_list[vv] = [p[0] if p[1] == vv else p[1] for p in self.e if vv in p]

    def show_info(self):
        print(self.adj_list)

    def bfs(self, node):
        visited = [False] * (len(self.v) + 1)

        # 注意一定要放进去后立即设置已访问
        queue = [node]
        visited[node] = True

        while queue:
            cur = queue.pop(0)
            print(cur)
            for i in self.adj_list[cur]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def dfs(self, node):
        visited = [False] * (len(self.v) + 1)

        def do_dfs(n):
            print(n)
            for i in self.adj_list[n]:
                if not visited[i]:
                    visited[i] = True
                    do_dfs(i)

        do_dfs(node)

    def dfs_stack(self, node):
        visited = [False] * (len(self.v) + 1)

        stack = [node]
        print(node)
        visited[node] = True

        while stack:
            # 注意这里不出栈，不能写成pop
            top = stack[-1]
            cur_list = self.adj_list[top]
            j = 0
            for cur in cur_list:
                if not visited[cur]:
                    stack.append(cur)
                    print(cur)
                    visited[cur] = True
                    break
                j += 1
            # 把当前节点的所有邻居节点遍历结束后，把该点出栈
            if j == len(cur_list):
                stack.pop()


def main():
    v = [1, 2, 3, 4, 5]
    e = [(1, 2), (1, 3), (1, 4), (2, 5), (3, 4), (4, 5)]
    graph = Graph(v, e, directed=False)
    graph.show_info()
    # graph.bfs(1)
    graph.dfs_stack(1)


if __name__ == '__main__':
    main()
