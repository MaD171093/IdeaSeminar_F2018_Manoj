import turtle

speed = 0
forward_path = 400
right_turn = 170 
arc_length = 60

circle_radius = forward_path/2
backward_path = forward_path/2


tom = turtle.Turtle()
tom.shape("circle")
tom.speed(speed)
tom.color('#051929','#8BCCFF')
tom.penup()
tom.goto(-200,100)
tom.pendown()
tom.pensize(1)


tic = turtle.Turtle()
tic.shape("triangle")
tic.speed(speed)
tic.color('#0B3602','#ADFF8B')
tic.pensize(2)
tic.penup()
tic.goto(-110,60)
tic.pendown()


tur = turtle.Turtle()
tur.shape("square")
tur.speed(speed)
tur.color('#EA0800','#FAC123')
tur.pensize(0.5)
tur.penup()
tur.goto(-65,40)
tur.pendown()

i = 0
j = 0

tom.begin_fill()
tic.begin_fill()
tur.begin_fill()
while True:  
    tom.forward(forward_path)
    tom.right(right_turn)
    tom.circle(circle_radius,arc_length)
    tom.backward(backward_path)

    tic.forward(forward_path/2)
    tic.right(right_turn)
    tic.circle(circle_radius/2,arc_length)
    tic.backward(backward_path/2)

    tur.forward(forward_path/4)
    tur.right(right_turn)
    tur.circle(circle_radius/4,arc_length)
    tur.backward(backward_path/4)  
    
    i+=1 
    if i == 36:
        i = 0
        break
tom.end_fill()
tic.end_fill()
tur.end_fill()

tom.ht()  
tic.ht()
tur.ht()

turtle.done()
