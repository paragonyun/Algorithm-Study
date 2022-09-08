## 예시 그래프
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]


def dfs(graph, v, visited) :
    ## 현재의 노드를 방문 처리한다.
    visited[v] = True
    print(v, end=' ')
    
    ## 현재 노드와 "연결된" 다른 노드를 재귀적으로 방문
    for i in graph[v] : 
        if not visited[i] :
            dfs(graph, i, visited)
visited = [False]*9 # index 0부터 나타내주기 때문에 index 형태로 그대로 매핑하기 위해 노드수+1로 False를 채움

dfs(graph, 1, visited)