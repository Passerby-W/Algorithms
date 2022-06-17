# dijkstra算法
# 迪杰斯特拉算法主要特点是从起始点开始，采用贪心算法的策略，每次遍历到始点距离最近且未访问过的顶点的邻接节点，直到扩展到终点为止。
# 时间复杂度：O(V^2)，V为顶点数


# Graph格式:

g = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 3, 'D': 8},
    'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
    'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
    'E': {'C': 5, 'D': 11, 'F': 1},
    'F': {'D': 22, 'E': 1},
}
dep = 0
des = 5


def dijkstra(graph, departure, destination):
    visited = []
    node_data = {}
    inf = float('inf')
    for key in graph.keys():
        node_data[key] = {'cost': inf, 'path': []}
    node_data[departure]['cost'] = 0
    temp = departure
    for i in range(len(graph) - 1):
        if temp not in visited:
            visited.append(temp)
            heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['path'] = node_data[temp]['path'] + list(temp)
                    heap.append((node_data[j]['cost'], j))
            sorted(heap, key=lambda e: e[0])
            _, temp = heap[0]
    print(node_data[destination]['cost'])
    print(node_data[destination]['path'] + list(destination))


dijkstra(g, 'A', 'F')
# 10
# ['A', 'C', 'E', 'F']