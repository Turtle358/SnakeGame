import turtle # To run the game
import time # To keep time
import random # To place the dots
import pickle # For the high score binary file
import ctypes # To get screen resolution

# Checking if High.Score is empty/ exists
try:
    Highscore = open("High.score","rb")
    high_score = int(pickle.load(Highscore))
    Highscore.close()
except:
    Highscorew = open("High.score","wb")
    pickle.dump("0",Highscorew)
    Highscorew.close()
# Setting Starting Delay
delay = 0.1

# Score
score = 0

# Set up the screen
Fullscreen = input("Would you like to go into fullscreen? (y or n) ")
if Fullscreen.lower() == "n":
    xres = 1280
    yres = 720
    titleheight = 320
    wn = turtle.Screen()
    wn.title("Snake Game By Luke")
    wn.bgcolor("black")
    wn.setup(xres,yres)
    wn.tracer(0) # Turns off the screen updates

else:
    wn = turtle.Screen()
    # Grabbing Screen Resolution
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    screenTk = wn.getcanvas().winfo_toplevel()
    screenTk.attributes("-fullscreen", True)
    wn.title("Snake Game By Luke")
    wn.bgcolor("black")
    wn.tracer(0)  # Turns off the screen updates
    xres = screensize[0]
    yres = screensize[1]
    titleheight = 440
xheight = (xres//2) - 20
yheight = (yres//2 - 20)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, titleheight)
pen.write("Score: 0  High Score: 0", align="center", font=("Eurofighter", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>xheight or head.xcor()<-xheight or head.ycor()>yheight or head.ycor()<-yheight:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Eurofighter", 24, "normal"))
        # Update high score
        HighScore = open("High.Score", "wb")
        pickle.dump(high_score,HighScore)
        HighScore.close()

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-xheight, xheight)
        y = random.randint(-yheight, yheight)
        food.goto(x,y)

        # Add a tail
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#580000")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Eurofighter", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Eurofighter", 24, "normal"))

            # Update high score
            HighScore = open("High.score","wb")
            pickle.dump(high_score,HighScore)
            HighScore.close()

    time.sleep(delay)
