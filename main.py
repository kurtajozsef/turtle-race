from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


def init_turtles():
    starting_y = -100
    distance = 30
    turtle_tuples = []
    for i in range(len(colors)):
        turtle = Turtle("turtle")
        turtle.penup()
        turtle.setposition(x=-230, y=starting_y + i * distance)
        turtle.color(colors[i])
        turtle.speed(1)
        turtle_tuples.append((colors[i], turtle))
    return turtle_tuples


def get_winner(turtle_tuples):
    for turtle_tuple in turtle_tuples:
        if turtle_tuple[-1].position()[0] >= 240:
            return turtle_tuple
    return None


def race(turtle_tuples):
    winner = None
    while winner is None:
        for turtle in turtle_tuples:
            distance = randint(1, 5)
            turtle[-1].forward(distance)
            winner = get_winner(turtle_tuples)
            if winner is not None:
                return


screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?(color):")
if bet in colors:
    racers = init_turtles()
    race(racers)
    winner_turtle = get_winner(racers)
    if winner_turtle[0].lower() == bet.lower():
        print(f"You win! {bet.title()} won the race!")
    else:
        print(f"You lost. {winner_turtle[0].title()} won the race!")
else:
    print(f"Wrong color/value: {bet}")

screen.exitonclick()
