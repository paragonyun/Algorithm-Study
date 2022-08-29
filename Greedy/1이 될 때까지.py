'''
1. N에서 1을 뺀다.
2. N을 K로 나눈다.

N이 1이 될 때까지 위의 과정을 반복하는데, 1번 혹은 2번의 과정을 수행해야 하는
최소 횟수를 구하라

입력 예시
25 5
'''

## 시간 시간 : 9:13
## 종료 시간 : 9:16

N, K = map(int, input().split())

cnt = 0

while N>1 :
    if N % K != 0 :
        N -= 1
        cnt += 1
    else :
        N /= K
        cnt += 1

print(cnt)