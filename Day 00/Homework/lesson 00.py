from turtle import*


#we want to paint a square


#step 1: draw a square
width(7)
color("blue")
speed(30)
forward(200)
left(90)
forward( 200)
left(90)
forward(200)
left(90)
forward(200)
#end of square

#drawing a door 


left(90)
forward(70)

color("brown")

left(90)
forward(70)

right(90)
forward(60)


right(90)
forward(70)
#end a door

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

left(30)
color("blue")
forward(90)
left(90)
color("white")
forward(30)
color("black")
left(90)
forward(50)
right(90)
forward(35)
right(90)
forward(50)
right(90)
forward(30)
right(180)
forward(35)
color("white")
forward(70)
color("black")
left(90)
forward(50)
right(90)
forward(35)
right(90)
forward(50)
right(90)
forward(35)




exitonclick()