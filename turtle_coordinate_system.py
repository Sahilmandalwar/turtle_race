from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500,height=400)


is_race_on = False
turtle_on_bet = []


user_bet = screen.textinput(title = "make your bet",prompt="which turtle you wanna bet? Enter a color/NIL: ").lower()
if(user_bet != "nill"):
    is_race_on = True
print(f"you bet on : {user_bet}")

refery = Turtle()
refery.hideturtle()
refery.penup()
refery.goto(x = 220,y = -180)
refery.pendown()
refery.goto(x = 220, y = 180)
refery.penup()
refery.goto(x = -220, y = -180)
refery.pendown()
refery.goto(x = -220,y = 180)

colors = ['violet','indigo','blue','green','yellow','orange','red']
y_position = [-100,-60,-20,20,60,100,140]

for turtle_idx in range(0,7):
    ribbon = Turtle(shape='turtle')
    ribbon.color(colors[turtle_idx])
    ribbon.penup()
    ribbon.goto(x=-230,y=y_position[turtle_idx])
    turtle_on_bet.append(ribbon)


while is_race_on:
    for each_turtle in turtle_on_bet:
        move_distance = random.randint(0,10)
        each_turtle.forward(move_distance)
        if each_turtle.xcor() >= 220:
            winner = each_turtle
            is_race_on = False
            break
            

if winner.fillcolor() == user_bet:
    print(f"winner is {winner.fillcolor()} , and Happy you won!")
else:
    print(f"winner is {winner.fillcolor()}, Alas, you lose!")



screen.exitonclick()

#remeber color, fillcolor, pencolor are method not attributes