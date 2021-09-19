from graphics import *

def DDA(x1, x2, y1, y2, console):
    x, y = x1, y1
    do_dai = 0
    if abs(x2 - x1) > abs(y2 - y1):
        do_dai = abs(x2 - x1)
    else:
        do_dai = abs(y2 - y1)
    dx = (x2 - x1) / float(do_dai)
    dy = (y2 - y1) / float(do_dai)
    for i in range(do_dai):
        x += dx
        y += dy
        new_point = Point(x, y)
        new_point.draw(console)

def Bresenham(x1, x2, y1, y2, console):
    dx = x2 - x1
    dy = y2 - y1
    step_x = 1 if dx >= 0 else -1
    step_y = 1 if dy >= 0 else -1
    dx, dy= abs(dx), abs(dy)
    grad = dy/float(dx)
    x, y = x1, y1
    if grad <= 1:
        p = 2 * dy - dx
        for i in range(dx):
            if p >= 0:
                y += step_y
                p += 2 * (dy - dx)
            else:
                p += 2 * dy
            x += step_x
            pt = Point(x, y)
            pt.draw(console)
    else:
        p = 2 * dx - dy
        for i in range(dy):
            if p >= 0:
                x += step_x
                p += 2 * (dx - dy)
            else:
                p += 2 * dx
            y += step_y
            pt = Point(x, y)
            pt.draw(console)

x1, y1 = list([int(i) for i in input("Nhap toa do (x1, y1): ").split()])
x2, y2 = list([int(i) for i in input("Nhap toa do (x2, y2): ").split()])
    
console = GraphWin(f"Ve duong thang bang thuat toan DDA voi input ({x1},{y1}) va ({x2},{y2})", 1000, 1000)
DDA(x1,x2, y1, y2,console)

console = GraphWin(f"Ve duong thang bang thuat toan Bresenham voi input ({x1},{y1}) va ({x2},{y2})", 1000, 1000)
Bresenham(x1, x2, y1, y2, console)

console.getMouse()