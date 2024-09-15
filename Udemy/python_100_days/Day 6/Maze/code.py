def turn_right():
    turn_left()
    turn_left()
    turn_left()
 


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and right_is_clear():
        turn_right()
    elif right_is_clear():
        turn_right()
