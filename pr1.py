import numpy as np

def fisher_metric(clas):
    mean = np.mean(clas, axis=0)
    var = np.var(clas, axis=0)
    return (mean)**2 / (var)

spisok = np.array(np.genfromtxt('Таблица.csv', delimiter=';'))
cls = 3
q = len(spisok)//cls
classA = list()

for i in range(q):
    classA.append(spisok[i])

fisher_values = fisher_metric(classA)
top_2_indices = np.argsort(fisher_values)[:2]
print("Фишеровская метрика между классами:", fisher_values)
print("Два самых информативных признака (индексы):", top_2_indices)
