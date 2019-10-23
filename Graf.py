# graph = {'a': {'b': 10, 'c': 3},
#          'b': {'c': 1, 'd': 2},
#          'c': {'b': 4, 'd': 8, 'e': 2},
#          'd': {'e': 7},
#          'e': {'d': 9}}

graph = {'1': {'2': 1, '5': 10, '3': 5},
         '2': {'1': 1, '4': 1},
         '3': {'1': 5, '5': 8},
         '4': {'2': 1, '5': 1},
         '5': {'4': 1, '3': 8}}


def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Шлях недосяжний')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print('Найкоротша відстань заняла ' + str(shortest_distance[goal]))
        print('Шлях ' + str(path))


dijkstra(graph, '1', '5')
