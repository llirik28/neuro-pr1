import numpy as np
def count_element(mas, x):
    count = 0
    for row in mas:
        for element in row:
            if element == x:
                count += 1
    return count

spisok = np.array(np.genfromtxt('text.csv', delimiter=','))
lenclass = len(spisok)
r = 0.72

d = list()
for i in range(lenclass):
    d.append(spisok[i])
    
srznach = np.mean(d, axis=0)
for i in range(len(srznach)):
    for q in range(lenclass):
        d[q][i] = float(round(d[q][i] - srznach[i], 1))
spcov = list()
spcov1 = list()
for col in range(len(d[0])):
    cov = 0
    for row in d:
        cov += (row[col] ** 2)
    cov = float(round(cov / 14, 2))
    spcov.append(float(round(cov / (cov ** 0.5 * cov ** 0.5), 2)))
    spcov1.append(float(round(cov ** 0.5, 2)))
covrazn = 0
spcovrazn = list()
for i in range(len(d[0]) - 1):
    for j in range(i + 1, len(d[0])):
        for row in d:
            covrazn += (row[i] * row[j])
        covrazn = float(round(covrazn / 14 / spcov1[i] / spcov1[j], 2))
        spcovrazn.append(covrazn)

d1 = np.array(list(list(0.00 for i in range(len(d[0]))) for j in range(len(d[0]))))
for i in range(len(d1[0])):
    d1[i][i] = spcov[i]
for x in range(2):
    k = 0
    for i in range(len(d1[0])):
        for j in range(i + 1, len(d1[0])):
            if spcovrazn[k] == 1 and i != j:
                d1[i][j] = spcovrazn[k] - 0.01
            elif spcovrazn[k] == -1 and i != j:
                d1[i][j] = spcovrazn[k] + 0.01
            else: d1[i][j] = spcovrazn[k]
            k += 1
    d1 = np.transpose(d1)
print(d1)

maxnediagelem = -1
i_index, j_index = 0, 0
spelem = list()
for i in range(len(d1[0])):
    for j in range(len(d1[0])):
        if d1[i][j] >= maxnediagelem and i != j:
            maxnediagelem = d1[i][j]
            i_index = i
            j_index = j
d1[i_index][j_index] = -1
d1[j_index][i_index] = -1
spelem.append([i_index, j_index, maxnediagelem])
maxnediagelem = -1
for z in range(len(d1) - 2):
    for i in range(len(d1[0])):
        if i == spelem[z][0] or i == spelem[z][1]:
            for j in range(len(d1[0])):
                if d1[i][j] >= maxnediagelem and i != j and d1[i][j] != -1 and count_element(spelem, j) <= 0:
                    maxnediagelem = d1[i][j]
                    i_index = i
                    j_index = j
    d1[i_index][j_index] = -1
    d1[j_index][i_index] = -1
    spelem.append([i_index, j_index, maxnediagelem])
    maxnediagelem = -1

spgroup = list()
for i in range(10):
    spgroup.append(set())
numgroup = 0

for i in range(len(spelem)):
    if spelem[i][2] > r:
        spgroup[numgroup].add(spelem[i][0])
        spgroup[numgroup].add(spelem[i][1])
    else:
        numgroup += 1
        spgroup[numgroup].add(spelem[i][1])

for i in range(len(spgroup)):
    if len(spgroup[i]) != 0:
        print(f"Group {i + 1}: ", end="")
        print(", ".join(map(str, spgroup[i])))
