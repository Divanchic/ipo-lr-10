a = ([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)])

rectangles = [[(-3, 1), (9, 10)],[(-7, 0), (13, 12)],[(0, 0), (5, 5)],[(2, 2), (7, 7)]]

def isCorrectRect(a):
    if((a[0][0]<a[1][0])&(a[0][1]<a[1][1])):
        return True
    else:
        return False
    
def isCollisionRect(a):
    if(((a[0][0][0]>a[1][0][0])&(a[0][1][0]<a[1][1][0]))or((a[0][1][0]>a[1][1][0])&(a[0][1][1]<a[1][1][1]))):
        return True
    else:
        return False
    try:
        isCorrectRect(a[0])==True
    except NameError:
        print('Прямоугольник не существует')

def intersectionAreaRect(a):
    # границы области пересечения
    left = max(a[0][0][0],a[1][0][0])
    bottom = max(a[0][0][1],a[1][0][1])
    right = min(a[0][1][0],a[1][1][0])
    top = min(a[0][1][1],a[1][1][1])

    width = right - left # ширина пересечения
    height = top - bottom # высота пересечения
    if (width <= 0 or height <= 0):# если ширина и высота области пересечения меньше или равны 0
        return 0 # то его площадь 0
    else:
        return (width * height)# если больше 0, то выводим площадь
    try:
        isCorrectRect(a[0])==True
    except NameError:
        print('Прямоугольник не существует')

def intersectionAreaMultiRect(a):
    # Обработка пустого списка
    if not rectangles:
        return 0
    
    # Проверка корректности всех прямоугольников
    for i, rect in enumerate(rectangles, 1):
        if not isCorrectRec(rect):
            raise RectCorrectError(i)  # i-й прямоугольник некорректен
    
    x_left_max = rectangles[0][0][0]    # Максимальная левая граница
    y_bottom_max = rectangles[0][0][1]  # Максимальная нижняя граница
    x_right_min = rectangles[0][1][0]   # Минимальная правая граница
    y_top_min = rectangles[0][1][1]     # Минимальная верхняя граница
    
    # Обновление границ для всех остальных прямоугольников
    for i in range(1, len(rectangles)):
        rect = rectangles[i]
        
        x_left_max = max(x_left_max, rect[0][0])
        y_bottom_max = max(y_bottom_max, rect[0][1])
        x_right_min = min(x_right_min, rect[1][0])
        y_top_min = min(y_top_min, rect[1][1])
    
    # Проверяю, существует ли общая область пересечения
    if x_left_max < x_right_min and y_bottom_max < y_top_min:
        width = x_right_min - x_left_max
        height = y_top_min - y_bottom_max
        return width * height
    else:
        return 0  # Нет общей области пересечения
