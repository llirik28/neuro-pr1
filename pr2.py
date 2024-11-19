import numpy as np

spisok = np.genfromtxt('Таблица.csv', delimiter=';')
cls = 3 
q = len(spisok)//cls
classA, classB, classC = list(), list(), list()

for i in range(len(spisok)):
    if i < q:
        classA.append(spisok[i])
    elif q <= i < (2*q):
        classB.append(spisok[i])
    elif (2*q) <= i < (3*q):
        classC.append(spisok[i])

signs = list()
for i in range(len(classA[0])):
    classes = list()
    while True:
        try:
            sign = int(input())
            if sign < 0:
                print('неверный ввод')
                exit()
            signs.append(sign)
            break
        except ValueError:
            print('неверный ввод')
            exit()
    
    for s in range(len(classA)):
        check = True
        object = classA[s].tolist()
        for sign_check in signs:
            if sign_check in object:
                object.remove(sign_check)
        if len(object) == len(classA[0]) - len(signs):
            classes.append('classA')
    
    for s in range(len(classB)):
        check = True
        object = classB[s].tolist()
        for sign_check in signs:
            if sign_check in object:
                object.remove(sign_check)
        if len(object) == len(classA[0]) - len(signs):
            classes.append('classB')
    
    for s in range(len(classC)):
        check = True
        object = classC[s].tolist()
        for sign_check in signs:
            if sign_check in object:
                object.remove(sign_check)
        if len(object) == len(classA[0]) - len(signs):
            classes.append('classC')


    if len(set(classes)) == 3:
        print('Class A, Class B or Class C')
    elif 'classA' in classes and 'classC' in classes:
        print('Not Class B')
    elif 'classA' in classes and 'classB' in classes:
        print('Not Class C')
    elif 'classB' in classes and 'classC' in classes:
        print('Not Class A')
    elif len(set(classes)) == 1:
        print(*set(classes))
        break 
    else:
        print('No one')
        break
