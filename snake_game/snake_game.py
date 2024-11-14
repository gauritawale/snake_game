# turtle
# random
# time


import turtle
import random
import time


delay = 0.1
score = 0
highestscore = 0
bodies = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Screen setup
a = turtle.Screen()
a.title("Snake Game")
a.bgcolor("gray")
a.setup(width=600, height=600)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("yellow")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.goto(0, 200)

# Scoreboard
sb = turtle.Turtle()
sb.speed(0)
sb.color("white")
sb.penup()
sb.hideturtle()
sb.goto(-250, -250)
sb.write("Score: 0  | Highest Score: 0", align="left", font=("Arial", 14, "bold"))

def move():
    # Calculate direction towards the food
    x_diff = food.xcor() - head.xcor()
    y_diff = food.ycor() - head.ycor()
    
    if abs(x_diff) > abs(y_diff):
        if x_diff > 0:
            head.setx(head.xcor() + 20)
        else:
            head.setx(head.xcor() - 20)
    else:
        if y_diff > 0:
            head.sety(head.ycor() + 20)
        else:
            head.sety(head.ycor() - 20)

# Main loop
while True:
    a.update()

    # Border collision detection and wrap-around
    if head.xcor() > 290:
        head.setx(-290)
        
    elif head.xcor() < -290:
        head.setx(290)

    if head.ycor() > 290:
        head.sety(-290)
        
    elif head.ycor() < -290:
        head.sety(290)

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase snake length
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color(colors[len(bodies) % len(colors)])  # Assign colors in a gradient pattern
        body.penup()
        bodies.append(body)

        # Update score and delay
        score += 10
        delay -= 0.001

        if score > highestscore:
            highestscore = score

        sb.clear()
        sb.color("lightblue")  # Make score text more attractive
        sb.write(f"Score: {score}  | Highest Score: {highestscore}", align="left", font=("Arial", 16, "bold"))

    # Move the snake body segments
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check for collision with the snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            for body in bodies:
                body.hideturtle()
            bodies.clear()

            score = 0
            delay = 0.1

            sb.clear()
            sb.write(f"Score: {score}  | Highest Score: {highestscore}", align="left", font=("Arial", 16, "bold"))

    time.sleep(delay)

a.mainloop()
