from graphics import *

def to_loang(arr, x, y, color):
    
    tren, duoi = y, y+1
    
    while [x,tren] not in arr and [x, duoi] not in arr:
        left, right = x, x+1
        while [left-1, tren] not in arr:
            console.plot(left, tren, color)
            if [right, tren] not in arr:
                console.plot(right, tren, color)
                right +=1
            left -= 1
        tren -=1
        left, right = x, x+1
        while [left-1, duoi] not in arr:
            console.plot(left, duoi, color)
            if [right, duoi] not in arr:
                console.plot(right, duoi, color)
                right +=1
            left -= 1
        duoi += 1
    console.getMouse()
    
def scanline(arr, max_x, min_y, max_y):
    for y in range(min_y, 500):
        x = max_x + 1
        while [x, y] not in arr:
            console.plot(x, y, "Green")
            x+=1
        while [max_x-1, y+1] not in arr:
            max_x -=1 
    for y in range(500, max_y+1):
        while[max_x , y] in arr:
            max_x += 1
        x = max_x + 1
        while [x, y] not in arr:
            console.plot(x, y, "Green")
            x+=1
        
    console.getMouse()  

def ve_(arr):
    min_y = 9999
    max_y = 500
    for toa_do in arr:
        min_y = min(min_y, toa_do[1])
        max_y = max(max_y, toa_do[1])
    max_x = 500
    while[max_x, min_y] in arr:
        min_y += 1
    while[max_x-1, min_y] not in arr:
        max_x -= 1
    while[500, max_y] in arr: max_y -= 1
    scanline(arr, max_x , min_y+1, max_y)
        
def ve(arr):
    x, y = 500, 500
    to_loang(arr, x, y, "red")
    console.getMouse()

def draw_ellipse(a, b, key):
    x_ = (a*a)/(pow(a*a + b*b, 0.5))
    x, y = 0,0
    x1, y1 = 0, b
    p = a*a*(1 - 2 * b) + b*b 
    arr_xy = [] #luu toa do bien
    arr_da_to = [] #luu toa do da to
    while x1 <= x_:
        Point(x1+500, y1+500).draw(console)
        Point(500-x1, 500+y1).draw(console)
        Point(x1+500, 500-y1).draw(console)
        Point(500-x1, 500-y1).draw(console)
        arr_xy.append([x1+500, y1+500])
        arr_xy.append([-x1+500, y1+500])
        arr_xy.append([x1+500, -y1+500])
        arr_xy.append([-x1+500, -y1+500])
        if p >= 0: 
            p += 4*a*a*(1 - y1)
            y1 -= 1
        x1 += 1
        p = p + 2*b*b*(2*x1 + 3) 
    #ve phan 2 dao nguoc a, b va x, y
    y_ = (b*b)/(pow(b*b + a*a, 0.5))
    p_ = b*b*(1 - 2 * a) + a*a
    x1, y1 = a, 0
    while y1 <= y_:
        Point(x1+500, y1+500).draw(console)
        Point(500-x1, 500+y1).draw(console)
        Point(x1+500, 500-y1).draw(console)
        Point(500-x1, 500-y1).draw(console)
        arr_xy.append([x1+500, y1+500])
        arr_xy.append([-x1+500, y1+500])
        arr_xy.append([x1+500, -y1+500])
        arr_xy.append([-x1+500, -y1+500])
        if p_ >= 0: 
            p_ += 4*b*b*(1 - (x1))
            x1 -= 1
        y1 += 1
        p_ = p_ + 2*a*a*(2*y1 + 3)
    if key == 0:   
        ve(arr_xy)
    else:
        ve_(arr_xy)
        
    console.getMouse()        

a, b = input("Hay nhap 50 <= a,b <= 200: ").split()
a, b = int(a), int(b)
console = GraphWin(f"Duong ellipse sau khi nhap a = {a}, b = {b} co ban kinh 1, to mau loang",1000 , 1000)
draw_ellipse(a, b, 0)
console = GraphWin(f"Duong ellipse sau khi nhap a = {a}, b = {b} co ban kinh 1, to mau scanline",1000 , 1000)
draw_ellipse(a, b, 1)