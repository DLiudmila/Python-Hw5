# Реализуйте RLE алгоритм: 
# реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

path = 'FileRLE_1.txt'
f1 = open(path, 'r') 
lst = f1.readline()
f1.close()


list1 = [i for i in range(0, len(lst)) if (lst[i] != lst[i-1] or i == len(lst)-1) or i == 0]
resList = ([str(list1[x] - list1[x-1])+lst[list1[x-1]] for x in range(1, len(list1))])
f2 = open('FileRLE_2.txt', 'w')
for item in resList:
    f2.write(item)
f2.close()


path_1 = 'FileRLE_3.txt'
t1 = open(path_1, 'r') 
lSt = t1.readline()
t1.close()

list2 = [(lSt[k], lSt[k+1]) for k in range(len(lSt)) if k%2 == 0]
t2 = open('FileRLE_4.txt', 'w')
x = list(map(lambda tup: t2.write(tup[1]*int(tup[0])), list2))
t2.close()