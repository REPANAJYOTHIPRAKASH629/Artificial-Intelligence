graph = { 'A':['B','C','D'],
          'B':['E'],
          'C':['D','E'],
          'D':[],
          'E':[]}
visited = set()
def dfs(visted,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)
dfs(visited,graph,'A')
