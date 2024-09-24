import turtle  #
a=int(input('输入个数:'))
banjing=100
jiaodu=10
sudu=0
turtle.speed(sudu)
for x in range(a):
    turtle.circle(banjing)
    turtle.left(jiaodu)
turtle.done()