import time  # Import the time module to control the game's frame rate
from turtle import Screen  # Import Screen class from turtle module for creating the game window
from paddle import Paddle  # Import Paddle class to create paddle objects for the game
from ball import Ball  # Import Ball class to create a ball object for the game
from scoreboard import ScoreBoard  # Import ScoreBoard class to display scores

# Set up the game window
screen = Screen()  # Create a screen object for the game window
screen.setup(width=800, height=600)  # Set the window size to 800x600 pixels
screen.bgcolor("black")  # Set the background color of the window to black
screen.title("Pong Game")  # Set the title of the window to "Pong Game"
screen.tracer(0)  # Turn off automatic screen updates, allows for manual update

# Create paddle objects
r_paddle = Paddle((350, 0))  # Create right paddle at position (350, 0)
l_paddle = Paddle((-350, 0))  # Create left paddle at position (-350, 0)

# Create a scoreboard object
scoreboard = ScoreBoard()  # Create a scoreboard to display scores

# Create a ball object
ball = Ball()  # Create a ball for the game

# Set up keyboard bindings to move paddles
screen.listen()  # Listen for keyboard input
screen.onkey(r_paddle.move_up, "Up")  # Bind the "Up" arrow key to move the right paddle up
screen.onkey(r_paddle.move_down, "Down")  # Bind the "Down" arrow key to move the right paddle down
screen.onkey(l_paddle.move_up, "w")  # Bind the "w" key to move the left paddle up
screen.onkey(l_paddle.move_down, "s")  # Bind the "s" key to move the left paddle down

# Main game loop
game_is_on = True  # Flag to control the game loop
while game_is_on:
    time.sleep(ball.ball_speed)  # Pause the loop to control the speed of the ball
    screen.update()  # Update the screen to reflect changes
    ball.move()  # Move the ball continuously

    # Detect collision with the top or bottom walls
    if ball.ycor() > 275 or ball.ycor() < -275:  # If the ball hits the top or bottom edge
        ball.bounce_y()  # Bounce the ball off the wall vertically

    # Detect collision with the paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 325) or (ball.distance(l_paddle) < 50 and ball.xcor() < -325):
        ball.bounce_x()  # Bounce the ball off the paddle horizontally

    # Check for the ball going out of bounds and update scores
    if ball.xcor() > 380:  # If the ball goes past the right paddle
        scoreboard.l_got_point()  # Left player scores a point
        ball.reset_position()  # Reset the ball to the center
    if ball.xcor() < -380:  # If the ball goes past the left paddle
        scoreboard.r_got_point()  # Right player scores a point
        ball.reset_position()  # Reset the ball to the center

screen.exitonclick()  # Close the game window when clicked
