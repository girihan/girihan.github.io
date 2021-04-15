'''
문제
초등학교 5학년 누리는 최소공배수와 최대공약수를 배우고 있다. 
두 정수 a와 b 최소공배수는 두 수의 공통된 배수 중 가장 작은 수이고, 최대공약수는 두 수의 공통된 약수 중 가장 큰 수이다.
그런데 가끔 두수를 주며 최소공배수와 최대 공약수 맞는지 물어본다. 
스스로 학습을 위해 자동으로 구해주는 프로그램을 만들어주려고 한다. 
두 수 a와 b를 입력하면, 최소공배수와 최대공약수를 출력하면 된다.

입력
첫째 줄에 테스트 케이스의 개수 T(1<=T<=1,000)가 주어진다. 각 테스트 케이스는 두 정수 a와 b로 이루어져 있고, 공백으로 구분되어 있다. (1 <= a,b <= 1,000)

출력
각 테스트 케이스에 대해 최소공배수와 최대공약수를 차례대로 출력한다.

예제 입력 1 
3
5 10
7 23
42 56

예제 출력 1 
10 5
161 1
168 14
'''

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b//gcd(a,b)

N = int(input())
numbers = list()
for _ in range(N):
    a, b = map(int, input().split())
    numbers.append((a,b))

for a, b in numbers:
    print(lcm(a,b), gcd(a,b))
