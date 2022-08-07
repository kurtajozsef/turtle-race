from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


def init_turtles() -> list[Turtle]:
    starting_y = -100
    distance = 30
    turtles = []
    for i in range(len(colors)):
        turtle = Turtle("turtle")
        turtle.penup()
        turtle.setposition(x=-230, y=starting_y + i * distance)
        turtle.color(colors[i])
        turtle.speed(1)
        turtles.append(turtle)
    return turtles


def get_winner(turtles: list[Turtle]) -> Turtle:
    for turtle in turtles:
        if turtle.position()[0] >= 240:
            return turtle
    return None


def race(turtles: list[Turtle]):
    race_over = False
    while not race_over:
        for turtle in turtles:
            distance = randint(1, 5)
            turtle.forward(distance)
            winner = get_winner(turtles)
            if winner is not None:
                race_over = True


screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?(color):")
if bet in colors:
    racers = init_turtles()
    race(racers)
    winner_turtle = get_winner(racers)
    if winner_turtle.color()[0].lower() == bet.lower():
        print(f"You win! {bet.title()} won the race!")
    else:
        print(f"You lost. {winner_turtle.color()[0].title()} won the race!")
else:
    print(f"Wrong color/value: {bet}")

screen.exitonclick()
