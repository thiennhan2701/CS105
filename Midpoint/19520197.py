from graphics import * 

def draw_circle(x, y, r):
    x1, y1 = x, y - r
    while x1 - x <= y - y1:
        f = (x1 - x)**2 + (y - y1)**2 - r**2
        y1 += 1 if f >= 0 else 0
        # ve 8 diem doi xung
        Point(x1, y1).draw(console)
        Point(x1 , 2*y - y1).draw(console)
        Point(2*x - x1, y1).draw(console)
        Point(2*x - x1, 2*y - y1).draw(console)
        Point(x + y- y1, x + y- x1).draw(console)
        Point(x + y- y1, y - x + x1).draw(console)
        Point(x - y + y1, x + y- x1).draw(console)
        Point(x - y + y1, y - x + x1).draw(console)
        x1 += 1
    console.getMouse()

x, y, r = list([int(i) for i in input("Nhap toa do (x, y) va ban kinh cua duong tron, moi tham so cach nhau 1 khoang trang: ").split()])
console = GraphWin(f"Duong tron sau khi nhap toa do ({x},{y}) co ban kinh {r}", 1000, 1000)
Point(x, y).draw(console)
draw_circle(x, y, r)