from graphics import *

class Button_:
    
    def __init__(self, window, name, c1, c2, c3, c4):
        y = c2.getY() - ((c2.getY() - c1.getY()) / 2.)
        x = c4.getX() - ((c4.getX() - c1.getX()) / 2.)
        self.polygon = Polygon(c1, c2, c3, c4)
        self.polygon.setFill("white")
        self.msg = Text(Point(x, y),name)
        self.polygon.draw(window)
        self.msg.draw(window)
        self.c1, self.c2, self.c3, self.c4 = c1, c2, c3, c4
        
    def clicked(self, point):
        px, py = point.getX(), point.getY()
        return px > self.c1.getX() and px < self.c3.getX() and py > self.c1.getY() and  py < self.c2.getY()

    def __del__(self):
        self.polygon.undraw()
        self.msg.undraw()

def is_numeric(str_):
    
    l = "0123456789."
    for i in str_:
        if i not in l:
            return False
    return True


class Circle_:
        
    def __init__(self, window, center, letter):
        self.letter = letter
        l_loc = Point(center.getX()+20,center.getY()+20)
        Text(l_loc, self.letter).draw(window)
        self.window = window
        self.center = center
        self.x = center.getX()
        self.y = center.getY()
        self.circle = Circle(center, 15)
        self.circle.draw(window)
        self.number = self.getinput()
        Text(center, self.number).draw(window)
        self.dependencies = []
        self.value = self.number

    def setval(self, pos):
        if pos.dependencies == []:
            return
        max_pos = pos.dependencies[0]
        max_val = max_pos.value
        for i in pos.dependencies:
            if i.value > max_val:
                max_val = i.value
                max_pos = i
        self.value += max_val
        #self.setval(max_pos)

    def getinput(self):
        input_box = Entry(self.center, 6)
        input_box.draw(self.window)
        self.window.getMouse()
        input_str = input_box.getText()
        while not is_numeric(input_str):
            input_box.setText("")
            self.window.getMouse()
            input_str = input_box.getText()
        input_box.undraw()
        try:
            return int(input_str)
        except:
            return 0

    def clicked(self, point):
        px, py = point.getX(), point.getY()
        cx, cy = self.center.getX(), self.center.getY()
        if px > cx - 15 and px < cx + 15 and py > cy - 15 and py < cy + 15:
            return True
        return False

    
