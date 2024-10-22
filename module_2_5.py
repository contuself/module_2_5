def get_matrix(n, m, value): #функция
    matrix = [] #список
    if n <= 0 and m <= 0: #если аргументы меньше или равны нулю, то
        return matrix #возвращаем пустую матрицу
    for i in range(n): #количество строк
        pustoy = [] #пустой список внутри цикла
        matrix.append(pustoy) #добавление списка в список
        for j in range(m): #количество столбцов
                pustoy.append(value) #пополнение списка значением
    return matrix #вернуть матрицу
result1 = get_matrix(2, 2, 10) #вывести функции в переменную, задав ей значения
result2 = get_matrix(3, 5, 42) #вывести функции в переменную, задав ей значения
result3 = get_matrix(4, 2, 13) #вывести функции в переменную, задав ей значения
print(result1) #вывести переменную
print(result2) #вывести переменную
print(result3) #вывести переменную

