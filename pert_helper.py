from graphics import *
from button_ import *
W = 500
H = 500

def quit_button(window):
    w1, w2 = (W/5.5), (W/20.)
    h1, h2 = (H/1.03), (H/1.2)
    c1 = Point(W - w1, H - h1)
    c2 = Point(W - w1, H - h2)
    c3 = Point(W - w2, H - h2)
    c4 = Point(W - w2, H - h1)
    return Button_(window, "", c1, c2, c3, c4)

def next_button(window):
    w1, w2 = (W/5.5/2 - 20), (W/20./2)
    h1, h2 = (H/1.03/2 - 20), (H/1.2/2)
    c1 = Point(W - w1, H - h1)
    c2 = Point(W - w1, H - h2)
    c3 = Point(W - w2, H - h2)
    c4 = Point(W - w2, H - h1)
    return Button_(window, "", c1, c2, c3, c4)

def on_a_circle(circles, point):
    for circle in circles:
        if circle.clicked(point):
            return [True,circle]
    return [False,""]

def reset_p():
    return Point(-10,0), Point(-10,0)

