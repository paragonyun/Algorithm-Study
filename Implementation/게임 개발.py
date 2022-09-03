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



