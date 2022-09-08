# DFS(Depth First Search)
### 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘  
### 즉, 최대한 멀리 있는 노드를 우선적으로 탐색하는 알고리즘!
<br>

**Stack or 재귀함수 이용**
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리 함
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 노드를 스택에 넣고 _방문처리_* 함  

    2-1. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄

3. 2번과정을 할 수 없을 때까지 반복

    *방문처리 : 스택에 삽입하여 다시 방문노드로 처리 안 되게 하는 것

<br>

**DFS 구현**
![image](https://user-images.githubusercontent.com/83996346/189016699-d4fc3c55-4a08-4f3c-b8c9-2dbf64e1439d.png)

```python
## 예시 그래프
graph = [
    [], # 0번 노드
    [2,3,8], # 1번 노드와 인접
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7], # 8번 노드와 인접
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

출력
1 2 7 6 8 3 4 5
```