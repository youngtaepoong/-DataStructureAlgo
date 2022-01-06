'''
1. �� ���� ���� a, b�� input���� �Է� ����.
2. �� �� a, b�� �ִ� ������� ����ϴ� �Լ��� �� ���� �������� �ۼ��Ѵ�.
    gcd_sub(a, b) ū ������ ���� ���� �ݺ������� �����鼭 gcd ���
    gcd_mod(a, b) ū ���� ���� ���� ���� �������� �̿��Ͽ� gcd ���
    gcd_rec(a, b)  gcd_sub �Լ��� ����Լ� ����
3. �� ���� �Լ��� ȣ���Ͽ� ���� ���� ��(�ִ�����)�� ���ʷ� ����Ѵ�. ���� ���ϰ��� x, y, z �� ������ ���ʷ� �޾Ҵٸ�, ������� x y z�� ����Ѵ�. (�Ʒ� ����� ���� ������ �� - ������Ŀ� �°� ������� ������ �ִ������� �´��� ����ó����)
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