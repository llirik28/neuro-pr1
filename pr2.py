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
            sign = int(input('Введите признак: '))
            if sign < 0:
                print('неверный ввод')
                exit()
            signs.append(sign)
            break
        except ValueError:
            print('неверный ввод')
            exit()
    
    for s in range(len(classA)):
        object = classA[s].tolist()
        for sign_check in signs:
            if sign_check in object:
                object.remove(sign_check)
        if len(object) == len(classA[0]) - len(signs):
            classes.append('Class A')
    
    for s in range(len(classB)):
        object = classB[s].tolist()
        for sign_check in signs:
            if sign_check in object:
                object.remove(sign_check)
        if len(object) == len(classA[0]) - len(signs):
            classes.append('Class B')
    
    for s in range(len(classC)):
        object = classC[s].tolist()
        for sign_check in signs:
            if sign_check in object:
                object.remove(sign_check)
        if len(object) == len(classA[0]) - len(signs):
            classes.append('Class C')

    if len(set(classes)) == 3:
        if classes.count('Class A') > classes.count('Class B') and classes.count('Class A') > classes.count('Class C'):
            print('Class A')
        elif classes.count('Class B') > classes.count('Class A') and classes.count('Class B') > classes.count('Class C'):
            print('Class B')
        elif classes.count('Class C') > classes.count('Class A') and classes.count('Class C') > classes.count('Class B'):
            print('Class C')
        elif classes.count('Class A') == classes.count('Class C'):
            print('Not Class B')
        elif classes.count('Class B') == classes.count('Class C'):
            print('Not Class A')
        elif classes.count('Class A') == classes.count('Class B'):
            print('Not Class C')
        else: print('Class A or Class B or Class C')
    elif ('Class A' in classes and 'Class C' in classes):
        print('Not Class B')
    elif ('Class A' in classes and 'Class B' in classes):
        print('Not Class C')
    elif ('Class B' in classes and 'Class C' in classes):
        print('Not Class A')
    elif len(set(classes)) == 1:
        print(*set(classes))
        break 
    else:
        print('No one')
        break
