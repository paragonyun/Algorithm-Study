'''
다양한 수로 이루어진 배열이 있을 때, 주어진 수들을  M번 더하여 가장 큰 수를 만들어라.
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과해서 더해질 수 없다.
'''

# 시작시간 : 10:40

N, M, K =map(int, input().split())
n_lst = list(map(int, input().split()))

cnt = 0
result = 0

sorted_lst = sorted(n_lst, reverse=True)

first = sorted_lst[0]
second = sorted_lst[1]

while M > 0 :
    for i in range(K) :
        if M == 0 :
            break
        result += first
        M -= 1

    result += second
    M -= 1

print(result)

