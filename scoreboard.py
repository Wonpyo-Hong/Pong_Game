from turtle import Turtle  # Import Turtle to use for drawing text on the screen

class ScoreBoard(Turtle):  # Define ScoreBoard class, inheriting from Turtle
    def __init__(self):
        super().__init__()  # Initialize the superclass (Turtle) to use its drawing and positioning methods
        self.color("white")  # Set the color of the text (score) to white
        self.penup()  # Lift the pen up to move the turtle without drawing a line
        self.hideturtle()  # Hide the turtle because we only want to display text, not the turtle icon
        self.l_score = 0  # Initialize the left player's score to 0
        self.r_score = 0  # Initialize the right player's score to 0
        self.update_scoreboard()  # Call the update_scoreboard method to display the initial scores

    def update_scoreboard(self):
        self.clear()  # Clear any previous score from the screen to update it
        self.goto(-100, 200)  # Move to the left side position to display the left player's score
        self.write(self.l_score, align="center", font=("courier", 100, "normal"))  # Display the left player's score
        self.goto(100, 200)  # Move to the right side position to display the right player's score
        self.write(self.r_score, align="center", font=("courier", 100, "normal"))  # Display the right player's score

    def l_got_point(self):
        self.l_score += 1  # Increment the left player's score by 1
        self.update_scoreboard()  # Update the scoreboard to reflect the new score

    def r_got_point(self):
        self.r_score += 1  # Increment the right player's score by 1
        self.update_scoreboard()  # Update the scoreboard to reflect the new score
