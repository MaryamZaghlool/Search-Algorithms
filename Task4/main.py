import ast

# graph = open('Graph.txt', 'r')
with open('Graph.txt') as Gr:
    graph = Gr.read()
points = ast.literal_eval(graph)
visited = []
queue = []


def bfs(visited, points, node):  # function for BFS
    visited.append(node)
    queue.append(node)
    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in points[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("Following is the Breadth-First Search")
bfs(visited, points, '5')  # function calling
Gr.close()
# graph.close()
