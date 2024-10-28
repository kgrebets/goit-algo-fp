import turtle
import math

def draw_tree(branch_length, level):
    if level == 0:
        return

    turtle.forward(branch_length)

    current_pos = turtle.pos()
    current_heading = turtle.heading()

    angle = 60

    #left part
    turtle.left(angle)
    draw_tree(branch_length * math.sqrt(2) / 2, level - 1)

    #go to start point
    turtle.setheading(current_heading)
    turtle.setpos(current_pos)

    #right part
    turtle.right(angle)
    draw_tree(branch_length * math.sqrt(2) / 2, level - 1)

    #go to start point
    turtle.setheading(current_heading)
    turtle.setpos(current_pos)

def main():
    user_input = input("Введіть рівень рекурсії (натисніть Enter для використання рівня 7): ")
    try:
        level = int(user_input) if user_input else 7
        if level < 0:
            raise ValueError("Рівень рекурсії повинен бути додатнім")
    except ValueError as e:
        print(e)
        return

    turtle.speed("fastest")
    turtle.left(90)
    turtle.penup()
    turtle.setpos(0, -300) 
    turtle.pendown()
    turtle.color("green")
    draw_tree(150, level)
    turtle.done()

if __name__ == "__main__":
    main()
