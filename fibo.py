'''
1. 두 양의 정수 a, b를 input으로 입력 받음.
2. 두 수 a, b의 최대 공약수를 계산하는 함수를 세 가지 버전으로 작성한다.
    gcd_sub(a, b) 큰 수에서 작은 수를 반복적으로 빼가면서 gcd 계산
    gcd_mod(a, b) 큰 수를 작은 수로 나눈 나머지를 이용하여 gcd 계산
    gcd_rec(a, b)  gcd_sub 함수의 재귀함수 버전
3. 세 가지 함수를 호출하여 리턴 받은 값(최대공약수)을 차례로 출력한다. 만약 리턴값을 x, y, z 세 변수에 차례로 받았다면, 순서대로 x y z를 출력한다. (아래 입출력 예시 참조할 것 - 출력형식에 맞게 출력하지 않으면 최대공약수가 맞더라도 오답처리됨)
'''

def gcd_sub(a, b):
    while a*b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a+b


def gcd_mod(a, b):
    while a*b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b

def gcd_rec(a, b):
    if a*b != 0:
        if  a > b:
            a = a - b
        else:
            b = b - a
        return gcd_rec(a, b)
    return a + b

a, b = input().split()
a = int(a)
b = int(b)

x = gcd_sub(a, b)
y = gcd_mod(a, b)
z = gcd_rec(a, b)

print(x, y, z)