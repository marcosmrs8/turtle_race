from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Make your color choice')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-100, -60, -20, 20, 60, 100]
all_turtle = []

for t in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[t])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position[t])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:

            is_race_on = False
            winning = turtle.pencolor()
            if winning == user_bet:
                print(f'Yay, you win the bet! {winning} is on fire! congratz!')
                turtle.write("[You Win]", font=("Courier", "36", "bold"), align="right")
            else:
                print(f'you lost this time ;c {winning} turtle is the winner')
                turtle.write("[You lose]", font=("Courier", "36", "bold"), align="right")

        ran_distance = random.randint(0,10)
        turtle.forward(ran_distance)

screen.exitonclick()