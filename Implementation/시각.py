'''
정수 N이 입력디면 00시00분00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 
모든 경우의 수를 구하는 프로그램을 작성하시오.

입력예시
5

제한 시간
15분
'''
## 시작시간 : 21:10
## 종료시간 : 21:16

N = int(input())

cnt = 0

for h in range(N+1) :
    for m in range(0,60) :
        for s in range(0, 60) :
            now = str(h) + str(m) + str(s)
            if '3' in now :
                cnt += 1

print(cnt)