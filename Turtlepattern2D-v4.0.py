import turtle

speed = 0 # should be 0 - 10 
forward_path = 400 # Size of the diagram
right_turn = 179 #pattern gen 160, 163, 166, 178,179, 180
arc_length = 60 #should be between 60 - 61
limit = 36 # Pattern Control


circle_radius = forward_path/2
backward_path = forward_path/2


tom = turtle.Turtle()
tom.shape("circle")
tom.speed(speed)
tom.color('#051929','#D6D6D6')
tom.pensize(1)
tom.penup()
tom.goto(-forward_path/2,50)
tom.pendown()



i = 1

tom.begin_fill()
while True:  
    tom.forward(forward_path)
    tom.right(right_turn)
    tom.circle(circle_radius,arc_length)
    tom.backward(backward_path)
     
    i+=1 
    if i == limit:
        i = 1
        break
tom.end_fill()

tom.ht() 
turtle.done()
