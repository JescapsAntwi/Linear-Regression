#implementing depth first search algorithm

visited = set()

graph = {'5': ['3', '7'], '3': ['2', '4'], '7': '8', '4': '8', '2': [], '8':[] }

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)

        for neighbour in graph[node]: #go to the neighboring node of the graph and 
            dfs(visited, graph, neighbour)#call the DFS function to use the neighbor parameter

print("Below is the depth first search:")
dfs(visited, graph, '5')
