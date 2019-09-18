#   a115_buggy_image[studentinitials].py
import turtle as trtl

#creates the body of a spider
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

#creates the legs of a spider
legs = 6
legspace = 70
z = 380 / legs
spider.pensize(5)
n = 0
while (n < legs):
  spider.goto(0,0)
  spider.setheading(z*n)
  spider.forward(legspace)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()