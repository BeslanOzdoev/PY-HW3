#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
N = int(input())

b = ''

while N > 0:
    b = str(N % 2) + b
    N = N//2

print(b)