'''
현민이는 ㄱ임 캐릭터가 맵 안에서 움직이는 시스템을 개발중이다.
N x M 크기의 직사각형으로 각각의 칸은 육지 혹은 바다이다.
캐릭터는 상하좌우로 움직이도 바다로는 이동할 수 없다.

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
2. 그 칸이 아직 가보지 않았다면 왼쪽으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 
    이미 가본 칸이면 회전만 하고 다시 왼쪽을 확인한다.
3. 네 방향이 모두 가봤거나 바다인 경우엔 바라보는 방향을 유지하고 한 칸 뒤로 가고 1단계로 간다. 
    뒤가 바다인 경우엔 움직임을 멈춘다.

0이 바다, 1이 육지이다.
북 : 0 동 : 1 남 : 2 서: 3

캐릭터가 방문한 칸의 수를 구하는 프로그램을 만드시오.

제한 시간 : 40분

입력 예시
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''

## 시작시간 : 20:05
## 종료시간 : 실패


N, M = map(int, input().split())
x, y, heads = map(int, input().split())

loc = []
for i in range(N) :
    locs = list(input().split())
    loc.append(locs)


now = loc[x][y]


## 방문 했던 곳을 저장하는 list
xsys = [(x,y)]


## 왼쪽을 도는 행위를 이러면 다 짜야하니까 함수를 아예 만드는 게 좋을 거 같음
def turn() :
    global heads

    heads -= 1 # 점점 작아져야 왼쪽으로 돎
    if heads == -1 :
        heads = 3 # 0다음엔 서쪽인 3이 와야함   

cnt = 1
go_back = 0

while True :
    if go_back == 4 : ## 네 방향 다 돌았으면
        '''
        여기서 time over
        '''
    
    turn() ## 왼쪽을 봄

    if heads == 0 : # 왼쪽을 바라본 게 북쪽이면
        x_ = x - 1
        will_be = (x_, y)
        if (will_be in xsys) or (loc[x_][y] == 1) : ## 가봤거나 바다면
            go_back += 1
            continue ## 처음으로 돌아감 = 한번 더 돌게됨

        else : ## 안 가봤고, 육지면
            here = will_be
            go_back = 0
            cnt += 1
            continue

    

    elif heads == 1 : # 왼쪽을 바라본 게 동쪽이면
        y_ = y + 1
        will_be = (x, y_)
        if (will_be in xsys) or (loc[x][y_] == 1) :
            go_back += 1
            continue

        else : ## 안 가봤고, 육지면
            here = will_be
            go_back = 0
            cnt += 1
            continue


    elif heads == 2 :
        x_ = x + 1
        will_be = (x_, y)
        if (will_be in xsys) or (loc[x_][y] == 1) : ## 가봤거나 바다면
            go_back += 1
            continue

        else : ## 안 가봤고, 육지면
            here = will_be
            go_back = 0
            cnt += 1
            continue


    elif heads == 3 :
        y_ = y-1
        will_be = (x, y_)
        if (will_be in xsys) or (loc[x][y_] == 1) :
            go_back += 1
            continue
    
        else : ## 안 가봤고, 육지면
            here = will_be
            go_back = 0
            cnt += 1
            continue
    


### 교재의 풀이
N, M =map(int, input().split())

## 맵을 일단 생성함 (0 으로)
d = [[0] * M for _ in range(N)] 
'''
[[0, 0, 0, 0], 
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]

지도형 자료를 만드는 가장 쉬운 방법...!
'''
x, y, direction = map(int, input().split())
# 현재 위치를 1로 표시
d[x][y] = 1
'''
[[0, 0, 0, 0], 
 [0, 1, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]
'''

## 현재 위치까지 표시하고 나서 이제 맵 전체 정보를 입력 받음
array = []
for i in range(N) :
    array.append(list(map(int, input().split())))
'''
[[1, 1, 1, 1],
 [1, 0, 0, 1],
 [1, 1, 0, 1],
 [1, 1, 1, 1]]
'''
## 동서남북 정의 (여기 아이디어가 핵심인듯)
## 이건 북동남서
dx = [-1,0,1,0] # 이런 식으로 방향을 미리 정해버림 그러고 하나씩 뽑아오는 방식
dy = [0,1,0,-1] # 북쪽을 바라보고 북쪽으로 이동 (-1.0) 

## 회전을 위한 함수 (이 아이디어는 똑같았음)
def turn_left() :
    global direction
    
    direction -= 1
    if direction == -1 :
        direction = 3

## 여기가 이제 시뮬레이션
cnt = 1
turn_time = 0
while True :
    # 일단 왼쪽으로 돎 -> direction이 -1이 됨 (첫번째 iter엔 서쪽을 봄)
    turn_left()
    # 서쪽 = direction의 3번째 index(turn_left에 의해 -1=3)
    # 그거에 맞게 새로운 좌표 지정
    nx = x + dx[direction]
    ny = y + dy[direction]

    ## 회전해서 갈 곳이 육지고, 가보지 않은 곳이라면
    if d[nx][ny] == 0 and array[nx][ny] == 0 :
        d[nx][ny] = 1 # 이제 갔다고 표시
        x = nx #이동
        y = ny

        cnt += 1
        turn_time = 0 # 도는 횟수 초기화
        continue # 다음 반복분으로 돌림
    
    else : # 둘 중 하나라도 안 되면
        turn_time += 1
        ## 그러고 while문 처음으로 돌아감
    
    if turn_time == 4 : ## 4방향 모두 갈 수 없는 경우
        '''
        사실 여기가 핵심... 
        나는 뒤로 가는 거를 생각 못했는데 방향을 지정하면 이렇게
        앞으로 가는 거 뒤로 가는 거 모두 쉽게 구현할 수 있음..
        '''
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        ## 뒤로 갈 수 있으면 이동
        if array[nx][ny] == 0 :
            x = nx
            y = ny
        
        else : ## 뒤가 바다로 막혀있는 경우
            break ## 반복문 탈출

        ## 어떤 경우든 turn_tiem = 0 이 되어야 함
        ## 이거 안 하면 무한 루프 걸립니다~
        turn_time = 0
print(cnt)
