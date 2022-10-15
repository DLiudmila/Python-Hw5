# Реализуйте RLE алгоритм: 
# реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

path = 'FileRLE_1.txt'
f1 = open(path, 'r') 
lst = f1.readline()
f1.close()


res = ''
i = 0
while i < len(lst):
    count = 1
    while (i+1) < len(lst) and lst[i] == lst[i+1]:
        count+= 1
        i+= 1
        tmpStr = str(count) + lst[i]
    i+=1
    res+=tmpStr
f2 = open('FileRLE_2.txt', 'w')
f2.writelines(res)
f2.close()


path_1 = 'FileRLE_3.txt'
t1 = open(path_1, 'r') 
lSt = t1.readline()
t1.close()

number = ''
res = ''
for i in range(len(lSt)):
    if not lSt[i].isalpha():
        number += lSt[i]
    else:
        res = res + lSt[i] * int(number)
        number = ''
t2 = open('FileRLE_4.txt', 'w')
t2.writelines(res)
t2.close()