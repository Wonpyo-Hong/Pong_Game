from turtle import Turtle  # Import the Turtle class from the turtle module for creating graphics

class Ball(Turtle):  # Define the Ball class, inheriting from the Turtle class
    def __init__(self):
        super().__init__()  # Initialize the superclass (Turtle), allowing Ball to use Turtle's methods and attributes
        self.shape("circle")  # Set the shape of the ball to a circle
        self.color("white")  # Set the color of the ball to white
        self.speed("slow")  # Set the animation speed of the ball to slow
        self.penup()  # Lift the pen up to prevent the ball from drawing lines
        self.setpos(0, 0)  # Initialize the ball's position at the center of the screen
        self.x_move = 10  # Set the ball's horizontal movement increment
        self.y_move = 10  # Set the ball's vertical movement increment
        self.ball_speed = 0.1  # Set the initial speed of the ball

    def move(self):
        x_cor = self.xcor() + self.x_move  # Calculate the new x-coordinate based on the current x-coordinate and x_move
        y_cor = self.ycor() + self.y_move  # Calculate the new y-coordinate based on the current y-coordinate and y_move
        self.goto(x_cor, y_cor)  # Move the ball to the new coordinates

    def bounce_y(self):
        self.y_move *= -1  # Reverse the vertical direction of the ball to simulate a bounce
        self.ball_speed *= 0.2  # Incorrect operation, it should reduce speed, but it's intended to increase the speed when bouncing

    def bounce_x(self):
        self.x_move *= -1  # Reverse the horizontal direction of the ball to simulate a bounce
        self.ball_speed *= 0.2  # Incorrect operation as above, same mistake in intention to modify speed on bounce

    def reset_position(self):
        self.goto(0, 0)  # Reset the ball's position to the center of the screen
        self.ball_speed = 0.1  # Reset the speed of the ball to the initial speed
        self.bounce_x()  # Reverse the ball's horizontal direction to start moving towards the opponent
