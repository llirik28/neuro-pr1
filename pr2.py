import numpy as np

classA = np.array([[11, 3, 12, 26, 11, 22, 33],
                  [13, 4, 16, 24, 4, 26, 12],
                  [19, 5, 18, 20, 16, 38, 48],
                  [16, 7, 12, 20, 21, 32, 63],
                  [12, 8, 14, 20, 6, 24, 18],
                  [11, 8, 12, 20, 12, 22, 36],
                  [17, 9, 14, 28, 26, 34, 78],
                  [18, 10, 16, 28, 17, 36, 51],
                  [13, 12, 16, 22, 9, 26, 27],
                  [11, 12, 12, 24, 22, 22, 66],
                  [15, 14, 10, 26, 14, 30, 42],
                  [16, 14, 12, 24, 27, 32, 81],
                  [19, 15, 18, 22, 5, 38, 15],
                  [17, 15, 14, 20, 22, 34, 66],
                  [12, 17, 14, 26, 18, 24, 54]])



classB =   np.array([[13, 22, 16, 22, 6, 26, 18],
                   [11, 23, 12, 26, 2, 22, 6],
                   [5, 24, 10, 22, 9, 30, 27],
                   [6, 24, 12, 28, 14, 32, 42],
                   [9, 25, 18, 22, 5, 38, 15],
                   [7, 27, 14, 20, 11, 34, 33],
                   [3, 28, 16, 24, 3, 26, 9],
                   [9, 28, 18, 26, 15, 38, 45],
                   [6, 29, 12, 28, 7, 32, 21],
                   [12, 30, 14, 20, 18, 24, 54],
                   [11, 31, 12, 24, 12, 22, 36],
                   [17, 32, 14, 20, 20, 34, 60],
                   [18, 33, 16, 26, 7, 36, 21],
                   [11, 34, 12, 26, 14, 22, 42],
                   [14, 35, 18, 22, 19, 28, 57]])


classC = np.array([[17, 23, 14, 24, 28, 34, 84],
                  [13, 25, 16, 28, 32, 26, 96],
                  [19, 25, 18, 22, 37, 38, 111],
                  [16, 25, 12, 28, 46, 32, 138],
                  [12, 28, 14, 28, 31, 24, 93],
                  [11, 28, 12, 26, 42, 22, 126],
                  [17, 29, 14, 22, 37, 34, 111],
                  [18, 30, 16, 24, 51, 36, 153],
                  [11, 31, 12, 24, 43, 22, 129],
                  [14, 32, 18, 22, 48, 28, 144],
                  [15, 32, 10, 28, 57, 30, 171],
                  [13, 33, 16, 20, 37, 26, 111],
                  [19, 34, 18, 24, 51, 38, 153],
                  [17, 36, 14, 26, 47, 34, 141],
                  [12, 36, 14, 20, 54, 24, 162]])

signs = list()
for i in range(len(classA[0])):
    classes = list()
    while True:
        try:
            sign = int(input())
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
        if len(object) != len(classA[0]):
            classes.append('classA')
    
    for s in range(len(classB)):
        check = True
        object = classB[s].tolist()
        for sign_check in signs:
            if sign_check in object:
                object.remove(sign_check)
        if len(object) != len(classA[0]):
            classes.append('classB')
    

   
    for s in range(len(classC)):
        check = True
        object = classC[s].tolist()
        for sign_check in signs:
            if sign_check not in object:
                object.remove(sign_check)
        if len(object) != len(classA[0]):
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



