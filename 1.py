import numpy as np
import matplotlib.pyplot as plt

def fisher_metric(class1, class2, class3):
    mean1 = np.mean(class1, axis=0)
    mean2 = np.mean(class2, axis=0)
    mean3 = np.mean(class3, axis=0)
    
    var1 = np.var(class1, axis=0)
    var2 = np.var(class2, axis=0)
    var3 = np.var(class3, axis=0)
    
    fisher_metric3 = (mean1 - mean2 - mean3) ** 2 / (var1 + var2 + var3)
    fisher_metric2 = (mean2 - mean3) ** 2 / (var2+ var3)
    
    return fisher_metric3, fisher_metric2 #выводим метрику фишера для 3 классов и для двух

spisok = np.genfromtxt('Таблица.csv', delimiter=';')
cls = 3 # заменил нахуй ввод 3 классов, устал уже от него
q = len(spisok)//cls
classA, classB, classC = list(), list(), list()

for i in range(len(spisok)):
    if i < q:
        classA.append(spisok[i])
    elif q <= i < (2*q):
        classB.append(spisok[i])
    elif (2*q) <= i < (3*q):
        classC.append(spisok[i])
        
classx3, classx2 = fisher_metric(classA, classB, classC) # классх3 - значения для 3 классов, классх2 - для 2
top_2_indices = np.argsort(classx3)[-2:] #информативные признаки в 3 классах
coords = list()
top_2_indices = [int(x) for x in top_2_indices.tolist()]
for stroka in range(len(spisok)):
    object = spisok[stroka].tolist()
    coords.append([int(object[top_2_indices[0]]), int(object[top_2_indices[1]])])

coordsx = [x[0] for x in coords]
coordsy = [y[1] for y in coords]

fig, ax = plt.subplots(figsize=(5, 5))
for i in range(15):
    plt.scatter(coordsx[i], coordsy[i], color='green')
for i in range(15, 30):
    plt.scatter(coordsx[i], coordsy[i], color='red')
for i in range(30, 45):
    plt.scatter(coordsx[i], coordsy[i], color='blue')

xa = [(sum(coordsx[i] for i in range(q)) / q), (sum(coordsy[i] for i in range(q)) / q)]
xbc = [(sum(coordsx[i] for i in range(q, q * 3)) / (q * 2)), (sum(coordsy[i] for i in range(q, q * 3)) / (q * 2))]
xa_xbc = [xa[0] - xbc[0], xa[1] - xbc[1]]
xaxbc = [xa[0] + xbc[0], xa[1] + xbc[1]]
z = 0.5 * (xa_xbc[0] * xaxbc[0] + xa_xbc[1] * xaxbc[1])
y = [(z - xa_xbc[0] * x) / xa_xbc[1] for x in coordsx]

plt.plot(coordsx, y)
plt.grid()
plt.show()



top_2_indices = np.argsort(classx2)[-2:]
coords = list()
top_2_indices = [int(x) for x in top_2_indices.tolist()]
for stroka in range(len(spisok)):
    object = spisok[stroka].tolist()
    coords.append([int(object[top_2_indices[0]]), int(object[top_2_indices[1]])])
coordsx = [x[0] for x in coords[15:]]
coordsy = [y[1] for y in coords[15:]]

fig, ax = plt.subplots(figsize=(5, 5))
for i in range(15):
    plt.scatter(coordsx[i], coordsy[i], color='red')
for i in range(15, 30):
    plt.scatter(coordsx[i], coordsy[i], color='blue')
    
xb = [(sum(coordsx[i] for i in range(q)) / q), (sum(coordsy[i] for i in range(q)) / q)]
xc = [(sum(coordsx[i] for i in range(q, q * 2)) / q), (sum(coordsy[i] for i in range(q, q * 2)) / q)]
xb_xc = [xb[0] - xc[0], xb[1] - xc[1]]
xbxc = [xb[0] + xc[0], xb[1] + xc[1]]
z = 0.5 * (xb_xc[0] * xbxc[0] + xb_xc[1] * xbxc[1])
y = [(z - xb_xc[0] * x) / xb_xc[1] for x in coordsx]

plt.plot(coordsx, y)
plt.grid()
plt.show()