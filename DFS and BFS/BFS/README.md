# BFS(Breadth First Search)
### 너비 우선 탐색, 그래프에서 가장 가까운 노드부터 우선적으로 탐색하는 알고리즘
### DFS와는 다르게, 최대한 가까운 노드부터 탐색하는 알고리즘!

<br>

**Queue 사용**

    1. 탐색 시작 노드를 que에 넣고 방문처리
    2. que에서 노드를 꺼내 그 노드의 인접 노드 중에서 **아직 방문하지 않은 노드를 모두 que에 삽입**
    3. 2번을 할 수 없을 때까지 반복
**deque를 이용하는 것이 정석!**  
재귀함수를 쓰면 오히려 느려지므로 deque로 쓰자. 시간은 DFS보다 빠른편!!

<br>

**BFS 구현**
![image](https://user-images.githubusercontent.com/83996346/189016699-d4fc3c55-4a08-4f3c-b8c9-2dbf64e1439d.png)


```python
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

from collections import deque 

def bfs(graph, start, visited) :
    ## deque로 Queue 생성
    queue = deque([start])

    ## 현재 노드 방문 처리
    visited[start] = True 

    ## queue가 빌 때까지 반복한다는 말
    while queue : 
        # 큐에서 가장 왼쪽의 원소를 뽑음
        v = queue.popleft()
        print(v, end = ' ')

        ## 해당 노드와 연결됐지만 아직 방문 안 했던 애들을 모두 큐에 삽입
        for i in graph[v] : #인접 노드를 돌면서
            if not visited[i] : # 방문을 안 했으면 (True값이 아니라 False 값이면)
                queue.append(i) # 현재 대기 큐에 넣고
                visited[i] = True # 방문 했다고 바꿔줌

visited = [False] * 9 #모든 노드를 비방문 처리

bfs(graph, 1, visited)

출력
1 2 3 8 7 4 5 6
```