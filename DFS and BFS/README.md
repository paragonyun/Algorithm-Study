# 그래프 탐색 알고리즘
### **탐색**
- 많은 양의 데이터 중에서 **원하는 데이터를 찾는 과정**
- 대표적인 것이 DFS와 BFS

### **자료구조**
- **데이터를 표현, 관리, 처리하기 위한 구조**
- 여기서는 Stack과 Queue가 사용됨!!

#### **Stack**
- 박스 쌓기. 먼저 들어온 게 제일 나중에 나감. 
- 가장 나중에 들어온 게 가장 먼저 나가는 방식이라 **"선입 후출 or 후입 선출"** 이라고 함.
- 단순 `list` 의 `apppend()`와 `pop()`으로 구현 가능함

예시
```python
lst = []
lst.append(1) # [1]
lst.append(2) # [1,2]
lst.append(3) # [1,2,3]
lst.pop()     # [1,2]
```

#### **Queue**
- 대기줄. 가장 먼저 들어온 게 먼저 나간다.
- **"선입 선출"** 이라고 함.
- que로 문제를 해결하고자 할 때는 `from collections import deque`를 이용함
- deque 라이브러리는 __"빠르게"__ queue를 이용할 수 있게해줌

예시
```python
queue = deque()

queue.append(1) # deque([1])
queue.append(2) # deque([1,2])
queue.append(3) # deque([1,2,3])
queue.popleft() # deque([2,3])

list(queue) # [2,3]
```

#### **재귀함수**
- 자기 자신을 계속 호출하는 함수, 예시로 보는 게 제일 좋다
``` python
def jaegui_function (i) :
    print(f'지금은 {i}번째 재귀함수')
    if i == 3 :
        return '전체 재귀함수 끝!' ## 이 메세지는 표시 안 됨
    print(f'{i}번째 재귀함수에서 {i+1}번째 재귀함수가 호출됩니다.')
    jaegui_function(i+1)
    print(f'{i}번째 재귀함수 종료')

jaegui_function(1)

## output 
지금은 1번째 재귀함수
1번째 재귀함수에서 2번째 재귀함수가 호출됩니다.
지금은 2번째 재귀함수
2번째 재귀함수에서 3번째 재귀함수가 호출됩니다.
지금은 3번째 재귀함수
2번째 재귀함수 종료
1번째 재귀함수 종료
```
- 재귀함수는 꼭 종료 조건을 달아줘야함 (while 처럼)
- 컴퓨터 내부적으로 재귀는 Stack을 이용함
    - 출력을 봤을 때 1-2-3을 쌓고 2-1 순서로 종료함
- 같은 결과를 낳더라도 재귀함수는 더 간결하게 표현할 수 있다는 장점이 있음!

<br>

# **그래프의 기본 구조**
- **노드**(Node, 정점)와 **간선**(Edge)로 표현됨
- 간선으로 연결된 두 노드를 "인접하다"라고 함

#### **표현 방식**
1. 인접 행렬  
말 그대로 matrix로 그래프를 표현함 관계를 노드들을 Column과 Index로 두고 인접하지 않은 노드 끼리는 Inf 값으로 나타냄

<br>

2. 인접 리스트  
비슷하게 2차원 list를 이용함 다만 노드와 간선의 관계를 Tuple로써 저장함

**메모리 상으로는 인접 리스트가 유리하고**  
**속도 측면에선 인접 행렬이 유리하다.**