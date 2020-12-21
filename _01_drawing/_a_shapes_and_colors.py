import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # This code makes a new Turtle. Pick a new name for the turtle
    ellie = turtle.Turtle()
    
    # Make your turtle's shape 'turtle', .shape('turtle')
    ellie.shape("turtle")
    # Set your turtle's speed using .speed(2)
    ellie.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    ellie.color("green")
    ellie.pencolor("blue")
    # Move your turtle forward using .forward(100)
    #ellie.forward(100)
    # TEST    Did your turtle move forward?
    
    # Move your turtle left or right using .left(90) or .right(90)
    #ellie.right(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for i in range (4):
        ellie.forward(100)
        ellie.right(90)
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    ellie.penup()
    ellie.goto(-200,150)
    ellie.pendown()
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    ellie.begin_fill()
    ellie.circle(50,360,50)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    ellie.end_fill()
    # Draw 3 more shapes with different fill colors!
    ellie.penup()
    ellie.goto(-30,100)
    ellie.pendown()
    for i in range(3):
        ellie.right(120)
        ellie.forward(150)
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
