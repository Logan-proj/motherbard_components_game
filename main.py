import turtle
import pandas
import random

screen = turtle.Screen()
screen.title("Motherboard Components Game")
image = "motherboard_diagram.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("labels.csv")
all_answers = data.answer.to_list()
all_names = data.names.to_list()
check_list = data.names.to_list()
x = 0

while x != 15:
    print(all_names)
    q_name = str(random.choice(all_names))
    user_answer = int(screen.numinput(title="Input Number", prompt=f"Where is the {q_name}",
                                      default=None, minval=1, maxval=15))
    x += 1
    print(q_name)
    if user_answer == check_list.index(q_name) + 1:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_data = data[data.answer == user_answer]
        t.goto(int(answer_data.x), int(answer_data.y))
        t.pendown()
        t.color("#00FF00")
        t.shape("square")
        if len(q_name) >= 25:
            t.shapesize(stretch_wid=2, stretch_len=20)
        elif 10 < len(q_name) < 25:
            t.shapesize(stretch_wid=2, stretch_len=8)
        else:
            t.shapesize(stretch_wid=2, stretch_len=5)
        t.stamp()
        t.color("#003300")
        t.write(q_name, move=False, align='center', font='Arial')
    elif user_answer != check_list.index(q_name) + 1:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_data = data[data.answer == user_answer]
        t.goto(int(answer_data.x), int(answer_data.y))
        t.pendown()
        t.color("#FF0000")
        t.shape("square")
        if len(q_name) >= 25:
            t.shapesize(stretch_wid=2, stretch_len=20)
        elif 10 < len(q_name) < 25:
            t.shapesize(stretch_wid=2, stretch_len=10)
        else:
            t.shapesize(stretch_wid=2, stretch_len=5)
        t.stamp()
        t.color("#330000")
        t.write(q_name, move=False, align='center', font='Arial')
    else:
        pass
    all_names.remove(q_name)

screen.exitonclick()
