import numpy as np

spisok = np.array(np.genfromtxt('text.csv', delimiter=','))
classescount = 4
lenclass = 15


d = spisok.copy()
ourclass = list()
for z in range(classescount):
    for i in range(lenclass * z, lenclass * (z + 1)):
        ourclass.append(spisok[i])
    srznach = np.mean(ourclass, axis=0)
    for i in range(len(srznach)):
        for q in range(lenclass * z, lenclass * (z + 1)):
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
            j = i + 1
            while j < len(d1[0]):
                d1[i][j] = spcovrazn[k]
                k += 1
                j += 1
        d1 = np.transpose(d1)

    print(d1)