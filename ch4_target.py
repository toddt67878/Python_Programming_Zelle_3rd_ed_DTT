from graphics import *

     def main():
        squareside = 200  # single point of control that allows resizing of target
        r = (squareside / 2)
        center = Point((squareside / 2), (squareside / 2))
        # use this list to add or delete colors for simpler or more complex targets
        color = ["white", "black", "blue", "red", "yellow", "green"]

        win = GraphWin("Ready, Aim, Fire!", squareside, squareside)

        # len() is used so that a target of any number of circles can be drawn
        for i in range(len(color)):

            # len(0 is used to get the proportion of part to whole
            aim = Circle(center, r - (r * (i / len(color))))
            aim.setFill(color[i])
            aim.draw(win)

      main()
