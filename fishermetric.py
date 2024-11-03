def fisher_metric(class1, class2):
    mean1 = np.mean(class1, axis=0)
    mean2 = np.mean(class2, axis=0)
    var1 = np.var(class1, axis=0)
    var2 = np.var(class2, axis=0)
    return (mean1 - mean2)**2 / (var1 + var2)

# Чтение данных
vhod_file = 'Таблица.csv'
vyhod_file = 'Таблица1.csv'

chclass = int(input('Введите количество объектов в классе: '))

with open(vhod_file, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()
with open(vyhod_file, 'w', encoding='utf-8') as outfile:
    outfile.writelines(lines[1:])

# Классы
class_A, class_B, class_C = list(), list(), list()


file = open(vyhod_file)
spisok = list(list(map(int, i.split(',')[2:])) for i in file)

for i in spisok:
    if len(class_A) < chclass:
        class_A.append(i)
    elif len(class_B) < chclass:
        class_B.append(i)
    elif len(class_C) < chclass:
        class_C.append(i)

class_A = np.array(class_A)
class_B = np.array(class_B)
class_C = np.array(class_C)

# Расчет метрики Фишера для всех пар классов
fisher_values_AB = fisher_metric(class_A, class_B)
fisher_values_BC = fisher_metric(class_B, class_C)
fisher_values_AC = fisher_metric(class_A, class_C)

# Среднее значение метрики Фишера для каждого признака по всем парам классов
fisher_mean = (fisher_values_AB + fisher_values_BC + fisher_values_AC) / 3

# Индексы двух самых информативных признаков
top_2_indices = np.argsort(fisher_mean)[-2:]

print("Фишеровская метрика между классами A и B:", fisher_values_AB)
print("Фишеровская метрика между классами B и C:", fisher_values_BC)
print("Фишеровская метрика между классами A и C:", fisher_values_AC)
print("Средние значения метрики Фишера для каждого признака:", fisher_mean)

