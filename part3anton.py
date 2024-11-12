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
    
    return fisher_metric3, fisher_metric2 

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
        
fisher_3cls, fisher_2cls = fisher_metric(classA, classB, classC) 
top_2_indices = np.argsort(fisher_3cls)[-2:] 
coordsx, coordsy = list(), list()
top_2_indices = [int(x) for x in top_2_indices.tolist()]
for stroka in range(len(spisok)):
    object = spisok[stroka].tolist()
    coordsx.append(int(object[top_2_indices[0]]))
    coordsy.append(int(object[top_2_indices[1]]))

fig, ax = plt.subplots(figsize=(5, 5))


xa = [(sum(coordsx[i] for i in range(q)) / q), (sum(coordsy[i] for i in range(q)) / q)] 
xbc = [(sum(coordsx[i] for i in range(q, q * 3)) / (q * 2)), (sum(coordsy[i] for i in range(q, q * 3)) / (q * 2))]
xa_xbc = [xa[0] - xbc[0], xa[1] - xbc[1]]
xaxbc = [xa[0] + xbc[0], xa[1] + xbc[1]]
z = 0.5 * (xa_xbc[0] * xaxbc[0] + xa_xbc[1] * xaxbc[1])
y = [(z - xa_xbc[0] * x) / xa_xbc[1] for x in coordsx]
count1, count2 = True, True
for i in range(q * 3):
    f = xa_xbc[0] * coordsx[i] + xa_xbc[1] * coordsy[i] - z
    if f > 0:
        plt.scatter(coordsx[i], coordsy[i], color='green', label='class A' if count1 else '')
        count1 = False
    else:
        plt.scatter(coordsx[i], coordsy[i], color='red', label='classes B & C' if count2 else '')
        count2 = False

plt.xlabel('Первая дискриминантная функция')
plt.plot(coordsx, y)
plt.legend()
plt.grid()
plt.show()


top_2_indices = np.argsort(fisher_2cls)[-2:]
coordsx, coordsy = list(), list()
top_2_indices = [int(x) for x in top_2_indices.tolist()]
print(top_2_indices)
for stroka in range(q, len(spisok)):
    object = spisok[stroka].tolist()
    coordsx.append(int(object[top_2_indices[0]]))
    coordsy.append(int(object[top_2_indices[1]]))

fig, ax = plt.subplots(figsize=(5, 5))
    
xb = [(sum(coordsx[i] for i in range(q)) / q), (sum(coordsy[i] for i in range(q)) / q)]
xc = [(sum(coordsx[i] for i in range(q, q * 2)) / q), (sum(coordsy[i] for i in range(q, q * 2)) / q)]
xb_xc = [xb[0] - xc[0], xb[1] - xc[1]]
xbxc = [xb[0] + xc[0], xb[1] + xc[1]]
z = 0.5 * (xb_xc[0] * xbxc[0] + xb_xc[1] * xbxc[1])
y = [(z - xb_xc[0] * x) / xb_xc[1] for x in coordsx]
count1, count2 = True, True
for i in range(q * 2):
    f = xb_xc[0] * coordsx[i] + xb_xc[1] * coordsy[i] - z
    if f > 0:
        plt.scatter(coordsx[i], coordsy[i], color='green', label='class B' if count1 else '')
        count1 = False
    else:
        plt.scatter(coordsx[i], coordsy[i], color='red', label='class C' if count2 else '')
        count2 = False

plt.xlabel('вторая дискриминантная функция')
plt.plot(coordsx, y)
plt.grid()
plt.legend()
plt.show()
