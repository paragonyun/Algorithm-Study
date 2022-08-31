'''
N x N 크기의 공간이 있다.
가장 왼쪽 위가 (1,1), 가장 오른쪽 아래의 좌표가 (N, N)이다.
계획서에는 L R U D 중 하나의 문자가 반복적으로 적혀있다.

정사각형 공간 밖을 움직여야 하는 경우는 무시된다. 
시작 좌표가 항상 (1,1) 일 때 가장 마지막에 도착하는 곳의 좌표를 구하시오.

입력 에시
5
R R R U D D

제한시간 
15분
'''
## 시작시간 : 20:46
## 종료시간 : 21:00

N = int(input())
lst = list(map(str, input().split()))

loc = [1,1]

for i in lst :
    if i == 'R' :
        loc[1] += 1 
        if loc[1] > N or loc[1] < 1 :
            loc[1] -=1 
            continue

    if i == 'L' :
        loc[1] -= 1 
        if loc[1] > N or loc[1] < 1 :
            loc[1] +=1 
            continue

    if i == 'D' :
        loc[0] += 1 
        if loc[0] > N or loc[0] < 1 :
            loc[0] -=1 
            continue

    if i == 'U' :
        loc[0] -= 1 
        if loc[0] > N or loc[0] < 1 :
            loc[0] +=1 
            continue

print(loc)