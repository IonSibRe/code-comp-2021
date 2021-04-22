from graphics import *
from time import sleep

def main():
    window = GraphWin("Semafor", width=500, height=500)

    # vars
    cirRad = 50

    # Rectangle
    rect1 = Rectangle(Point(150, 50), Point(350, 450))
    rect1.setFill(color_rgb(0, 0, 0))
    rect1.setOutline(color="black")
    rect1.draw(window)

    # Red Circle
    cirRed = Circle(Point(250, 130), cirRad);
    cirRed.setFill(color_rgb(30, 30, 30));
    cirRed.setOutline(color_rgb(30, 30, 30));
    cirRed.draw(window)


    # Orange Circle
    cirOrange = Circle(Point(250, 250), cirRad);
    cirOrange.setFill(color_rgb(30, 30, 30));
    cirOrange.setOutline(color_rgb(30, 30, 30));
    cirOrange.draw(window)


    # Green Circle
    cirGreen = Circle(Point(250, 370), cirRad);
    cirGreen.setFill(color_rgb(30, 30, 30));
    cirGreen.setOutline(color_rgb(30, 30, 30));
    cirGreen.draw(window)

    # ========== Lights ========== 

    while(True):
        # 5 sec green
        cirGreen.setFill(color="green")
        time.sleep(5);
        cirGreen.setFill(color_rgb(30, 30, 30))

        # 3 sec orange
        cirOrange.setFill(color="orange")
        time.sleep(3)
        cirOrange.setFill(color_rgb(30, 30, 30))


        # 5 sec red
        cirRed.setFill(color="red");
        time.sleep(5)
        cirRed.setFill(color_rgb(30, 30, 30))

        # 1 sec red and orange
        cirRed.setFill(color="red");
        cirOrange.setFill(color="orange")
        time.sleep(1)
        cirRed.setFill(color_rgb(30, 30, 30))
        cirOrange.setFill(color_rgb(30, 30, 30))

    window.getMouse()
    window.close()

main()