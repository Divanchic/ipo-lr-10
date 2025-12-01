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
    b=0
    for i in (len(rectangles)/2):
        b+=min(a)-max(i[0][0],i[1][0])
    return 0

for i in range(int(len(rectangles)/2)):
    print(2**i)
    