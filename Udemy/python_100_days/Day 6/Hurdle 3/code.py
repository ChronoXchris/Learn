def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
def walk():
    while front_is_clear():
        move()
    while wall_in_front():
        jump()
        

while not at_goal():
    walk()