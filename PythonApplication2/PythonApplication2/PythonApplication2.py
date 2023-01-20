import turtle

shape = input("Enter the shape you want to draw (rectangle or circle): ")

if shape == "rectangle":
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()
    turtle.exitonclick()

elif shape == "circle":
    radius = int(input("Enter the radius of the circle: "))
    turtle.circle(radius)
    turtle.exitonclick()

else:
    print("Invalid shape selected. Please enter 'rectangle' or 'circle'.")
