import numpy as np
import matplotlib.pyplot as plt

def fisher_metric(class1, class2, class3):
    mean1 = np.mean(class1, axis=0)
    mean2 = np.mean(class2, axis=0)
    mean3 = np.mean(class3, axis=0)
    
    var1 = np.var(class1, axis=0)
    var2 = np.var(class2, axis=0)
    var3 = np.var(class3, axis=0)
    
    fisher_metric_12 = (mean1 - mean2)**2 / (var1 + var2)
    fisher_metric_13 = (mean1 - mean3)**2 / (var1 + var3)
    fisher_metric_23 = (mean2 - mean3)**2 / (var2 + var3)
    
    return fisher_metric_12, fisher_metric_13, fisher_metric_23
spisok = np.genfromtxt('table2572.csv', delimiter=';')
print(spisok)
cls = int(input('Введите количество классов: '))
q = len(spisok)//cls
classA, classB, classC = list(), list(), list()

for i in range(len(spisok)):
    if i < q:
        classA.append(spisok[i])
    elif q <= i < (2*q):
        classB.append(spisok[i])
    elif (2*q) <= i < (3*q):
        classC.append(spisok[i])
        
class12, class13, class23 = fisher_metric(classA, classB, classC)
classx = list()
for i in range(7):
    classx.append(class12[i] + class13[i] + class23[i])
top_2_indices = np.argsort(classx)[-2:]
coords = list()
top_2_indices = [int(x) for x in top_2_indices.tolist()]
for stroka in range(len(spisok)):
    object = spisok[stroka].tolist()
    coords.append([int(object[top_2_indices[0]]), int(object[top_2_indices[1]])])

coordsx = [x[0] for x in coords]
coordsy = [y[1] for y in coords]

fig, ax = plt.subplots(figsize=(5, 5))
for i in range(15):
    plt.scatter(coordsy[i], coordsx[i], color='green')
for i in range(15, 30):
    plt.scatter(coordsy[i], coordsx[i], color='red')
for i in range(30, 45):
    plt.scatter(coordsy[i], coordsx[i], color='blue')
xa = [(sum(coordsx[i] for i in range(q)) / q), (sum(coordsy[i] for i in range(q)) / q)]
xb = [(sum(coordsx[i] for i in range(q, q * 2)) / q), (sum(coordsy[i] for i in range(q, q * 2)) / q)]
xa_xb = [xa[0] - xb[0], xa[1] - xb[1]]
xaxb = [xa[0] + xb[0], xa[1] + xb[1]]
X = list(range(70))
y = [((-(xa_xb[0] * x) + 0.5 * ((xa_xb[1] * xaxb[1]) + (xa_xb[0] * xaxb[0]))) / (xa_xb[1])) for x in X]

# Рисуем прямую
plt.plot(y, X)
plt.grid()
plt.show()