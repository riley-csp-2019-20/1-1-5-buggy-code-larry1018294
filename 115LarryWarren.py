#   a115_buggy_image[studentinitials].py
import turtle as trtl

#creates the body of a spider
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

#creates the legs of a spider
legs = 8
leglength = 100
legspacing = 10000 / legs
spider.pensize(5)
count = 0
while (count < legs):
  spider.goto(0,20)
  spider.setheading(legspacing*count)
  spider.forward(leglength)
  count = count + 1

#creates the head
spider.penup()
spider.goto(50,50)
spider.pendown()
spider.begin_fill()
spider.circle(20)
spider.end_fill()

#creates spider eyes
spider.penup()
spider.goto(45,45)
spider.pencolor("cyan")
spider.pendown()
spider.circle(4)

spider.penup()
spider.goto(30,60)
spider.pencolor("red")
spider.pendown()
spider.circle(4)



spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()