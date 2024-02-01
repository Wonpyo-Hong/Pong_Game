from turtle import Turtle, Screen  # Import Turtle for drawing and controlling paddles, Screen not used here and can be removed

class Paddle(Turtle):  # Define the Paddle class, inheriting from Turtle to use its drawing and movement methods
    def __init__(self, position):
        super().__init__()  # Call the __init__ method of the Turtle superclass to initialize a new Turtle object
        self.shape("square")  # Set the shape of the paddle to square
        self.hideturtle()  # Temporarily hide the turtle to set up its properties before showing it
        self.color("white")  # Set the paddle color to white
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the square shape to make the paddle (5 times taller, same width)
        self.penup()  # Lift the pen up so the paddle does not draw a line when moving
        self.setpos(position)  # Set the paddle's starting position as specified by the 'position' argument
        self.showturtle()  # Make the paddle visible on the screen after its properties are set

    def move_up(self):
        current_ycor = self.ycor()  # Get the current y-coordinate of the paddle
        self.goto(self.xcor(), current_ycor + 20)  # Move the paddle up by 20 pixels without changing the x-coordinate

    def move_down(self):
        current_ycor = self.ycor()  # Get the current y-coordinate of the paddle
        self.goto(self.xcor(), current_ycor - 20)  # Move the paddle down by 20 pixels without changing the x-coordinate
