#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

N = [3, 4, 1, 9, 6, 7, 9, 2, 2]
X=[]
print(len(N))
if len(N) % 2 !=0:
   for i in range(0, len(N)//2+1):
       X.append(N[i]*N[len(N)-i-1])
elif len(N) % 2 ==0:
    for i in range(0, len(N)//2):
       X.append(N[i]*N[len(N)-i-1])
print(X)