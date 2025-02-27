import collections
from collections import deque


#example of a default dict in python (a type of dictionary)
graph = {'A':['B','C','D'], 'B':['H'],'C':[],'D':['E','F'], 'E':[], 'F':[],'H':[]}

def bfs(graph, root):
    visited = set() #We use set() to avoid repetitions
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()   #Removing from the left end and storing it in node variable        
        if node not in visited:
            visited.add(node)
            print(node, end=' ')

        for child in graph[node]:
            if child not in visited:
                queue.append(child)
bfs(graph, 'A')

#Go and implement dfs


