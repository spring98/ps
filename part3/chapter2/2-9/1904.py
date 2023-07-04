# n = int(input().strip())
#
# dp = [0] * 1000001
# dp[1] = 1
# dp[2] = 2
#
# for i in range(3, n+1):
#     dp[i] = (dp[i-1] + dp[i-2]) % 15746
#
# print(dp[n])

n1 = 1
n2 = 2

n = int(input())
n3 = 1
for _ in range(n-2):
    n3 = (n1 + n2) % 15746
    n1 = n2
    n2 = n3

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    print(n3)


'''
    피보나치인거 까지 알았고 dp로 배열 만들어서 해도 되고, matlab 처럼 풀어도 된다.
    초항 둘째항 일때 테스트 케이스를 분기해줘야 하고 값이 엄청 커지면 정수에 못담아 에러가 되기때문에
    중간중간에 % 로 나머지로 사용한다. 끝나고 나누는 것이 아니라 for문 내에서 한다는 뜻
'''



