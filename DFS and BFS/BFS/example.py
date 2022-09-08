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