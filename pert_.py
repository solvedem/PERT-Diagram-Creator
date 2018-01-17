from pert_helper import *
from collections import defaultdict

crit_p = []

def critical(pos):
    # Finds critical path, adds it to global array crit_p
    if pos.dependencies == []:
        return
    max_pos = pos.dependencies[0]
    max_val = max_pos.value
    for i in pos.dependencies:
        if i.number > max_val:
            max_val = i.value
            max_pos = i
    global crit_p
    crit_p.append(max_pos)
    critical(max_pos)

def main():
    
    win = GraphWin("", W, H)
    win.setCoords(0, 0, W, H)
    nb = next_button(win)
    qb = quit_button(win)
    start_point = Point(20, H/2.)
    end_point = Point(W-20, H/2.)
    start_circ = Circle(start_point,20)
    end_circ = Circle(end_point,20)
    start_circ.draw(win)
    end_circ.draw(win)
    circles = []
    letters = "abcdefghijklmnopqrstuvqxyz"

    # Get circles from the user while they haven't quit or clicked next
    p = win.getMouse()
    i = 0
    while not qb.clicked(p) and not nb.clicked(p):
        circles.append(Circle_(win, p, letters[i]))
        p = win.getMouse()
        i += 1

    # Change color of next button if clicked
    if nb.clicked(p):
        nb.polygon.setFill("peachpuff")

    # DRAWING ARROWS -------------------------------------------------------------------
    
    p, p2 = reset_p()
    loop = True
    conns = defaultdict(list)
    
    while not qb.clicked(p) and not qb.clicked(p2) and loop:

        # Get 2 valid clicks from user, ensuring they are within a circle

        # Click 1, start of arrow
        p, p2 = reset_p()
        while not on_a_circle(circles, p)[0] and loop:
            if qb.clicked(p) or qb.clicked(p2):
                loop = False
            else:
                p = win.getMouse()
                
        conn1 = on_a_circle(circles, p)[1] 

        # Click 2, tail of arrow
        while not on_a_circle(circles, p2)[0] and loop:
            if qb.clicked(p2) or qb.clicked(p):
                loop = False
            else:
                p2 = win.getMouse()
                
        conn2 = on_a_circle(circles, p2)[1]

        # Add the first circle as a dependency of the second
        if conn2 != "":
            conn2.dependencies.append(conn1)
            conns[conn2.letter].append(conn1.letter)

        # Draw arrow if possible
        if not win.isClosed() and loop:
            line = Line(p, p2)
            line.setArrow("last")
            line.draw(win)
            
    # END DRAWING ARROWS -------------------------------------------------------------------

    # Draw line from starting circle to
    # all circles without dependencies
    # Also, find and set values of all circles
    for i in circles:
        i.setval(i)
        if i.dependencies == []:
            line = Line(start_point,i.center)
            line.setArrow("last")
            line.draw(win)

    # Find all circles that nothing depends on (end nodes)
    # Also, draw values of circles on window
    max_pos = circles[-1]
    depends_on = []
    for i in circles:
        tp = Point(i.x - 20, i.y - 20)
        Text(tp, str(i.value)).draw(win) # draw values
        for j in i.dependencies:
            if j not in depends_on:
                depends_on.append(j)
                
    # Draw a line from the ending circle
    # to circles that nothing depends on
    maxes = []
    for i in circles:
        if i not in depends_on:
            maxes.append(i)
            line = Line(i.center, end_point)
            line.setArrow("last")
            line.draw(win)

    # Find best critical path
    # out of all circles that no other circles depends on
    best_val = 0
    best_critical = maxes[0]
    for i in maxes:
        global crit_p
        crit_p = []
        crit_p.append(i)
        critical(i)
        if sum(j.value for j in crit_p) >= best_val:
            best_val = sum(j.value for j in crit_p)
            best_critical = crit_p
            
    # Color critical path
    if type(best_critical)==type([]):
        for i in best_critical:
            i.circle.setFill("cyan")

    # Wait to close
    while not quit_button(win).clicked(win.getMouse()):
        continue
    
    win.close()


main()
