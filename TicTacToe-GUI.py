# TIC-TAC-TOE
import turtle as pt
from Minimax import *
from random import random, choice

#pt=turtle.Turtle()
pt.speed(speed=0)

def cross(pt):     #create cross
    pt.pu()
    pt.lt(45)
    pt.fd(56.5685)
    pt.pd()
    pt.bk(113.1370)
    pt.pu()
    pt.lt(45)
    pt.fd(80)
    pt.rt(135)
    pt.pd()
    pt.fd(113.1370)

matrix=list(range(9))      #marks positions

index={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}

pos=0
j=0
flag=0

def mat(pos,j):                      #update matrix
    global matrix
    global flag
    if matrix[pos] != 'O' and matrix[pos] != 'X':
        if j%2==0:
            matrix[pos] = 'O'
        else:
            matrix[pos] = 'X'
        #flag=1
    #return matrix

def empty_in_mat():
    global matrix
    l = [i for i in range(9) if type(matrix[i])==int]
    print (matrix, l)
    return l
    

strikeh={0:[-150,100],1:[-150,0],2:[-150,-100]}
strikev={0:[-100,150],1:[0,150],2:[100,150]}
striked={1:[-150,150],2:[150,150]}


def won_game():                             # check victory
    global matrix
    mx=matrix
    pt.pensize(8)
    for i in range(3):
        if (mx[0+i*3]==mx[1+i*3]==mx[2+i*3]=='O'):
            pt.pu()
            pt.goto(strikeh[i])
            pt.seth(0)
            pt.pd()
            pt.fd(300)
            print('P1 WON')
            return True
        elif (mx[0+i]==mx[3+i]==mx[6+i]=='O'):
            pt.pu()
            pt.goto(strikev[i])
            pt.seth(270)
            pt.pd()
            pt.fd(300)
            print('P1 WON')
            return  True
        elif (mx[0+i*3]==mx[1+i*3]==mx[2+i*3]=='X'):
            pt.pu()
            pt.goto(strikeh[i])
            pt.seth(0)
            pt.pd()
            pt.fd(300)
            print('P2 WON')
            return True
        elif (mx[0+i]==mx[3+i]==mx[6+i]=='X'):
            pt.pu()
            pt.goto(strikev[i])
            pt.seth(270)
            pt.pd()
            pt.fd(300)
            print('P2 WON')
            return True
        elif (mx[0]==mx[4]==mx[8]=='O'):
            pt.pu()
            pt.goto(striked[1])
            pt.seth(315)
            pt.pd()
            pt.fd(424.264)
            print('P1 WON')
            return True
        elif (mx[2]==mx[4]==mx[6]=='O'):
            pt.pu()
            pt.goto(striked[2])
            pt.seth(225)
            pt.pd()
            pt.fd(424.264)
            print('P1 WON')
            return True
        elif (mx[0]==mx[4]==mx[8]=='X'):
            pt.pu()
            pt.goto(striked[1])
            pt.seth(315)
            pt.pd()
            pt.fd(424.264)
            print('P2 WON')
            return True
        elif (mx[2]==mx[4]==mx[6]=='X'):
            pt.pu()
            pt.goto(striked[2])
            pt.seth(225)
            pt.pd()
            pt.fd(424.264)
            print('P2 WON')
            return True
    return False

for i in range(4):    #create board
    pt.pu()
    pt.fd(50)
    pt.lt(90)
    pt.fd(150)
    pt.rt(180)
    pt.pd()
    pt.fd(300)
    pt.pu()
    pt.goto(0,0)
    pt.seth(0)
    rot=(i+1)*90
    pt.lt(rot)
pt.pu()

circoord={0:[-100,60], 1:[0,60], 2:[100,60], 3:[-100,-40], 4:[0,-40], 5:[100,-40], 6:[-100,-140], 7:[0,-140], 8:[100,-140]}          # coordinates for circle
crocoord={0:[-100,100], 1:[0,100], 2:[100,100], 3:[-100,0], 4:[0,0], 5:[100,0], 6:[-100,-100], 7:[0,-100], 8:[100,-100]}         # coordinates for cross


def get(a,b):                     #get position of box
    pt.pensize(3)
    global pos,matrix,j
    if b>50:
        if a<-50:
            pos=0
        elif a>-50 and a<50:
            pos=1
        else:
            pos=2
    elif b<50 and b>-50:
        if a<-50:
            pos=3
        elif a>-50 and a<50:
            pos=4
        else:
            pos=5
    else:
        if a<-50:
            pos=6
        elif a>-50 and a<50:
            pos=7
        else:
            pos=8


    pt.pu()
    pt.goto(0,0)
    pt.seth(0)

    
    print ("Hooman: ", pos)
    mat(pos, j)
    mark(pos)    

    global alpha
    r = random()
    if r > alpha:
        pos = choice(empty_in_mat())
    else:
        pos = minimax(matrix, AI)['index']
    print ("AI: ", pos)
    mat(pos, j)
    mark(pos)


def mark(pos):
    global flag, j, matrix
    #if flag==1:
    if j%2==0:
        x=circoord[pos][0]
        y=circoord[pos][1]
        pt.pencolor("blue")
        pt.goto(x,y)
        pt.pd()
        pt.circle(40)
    else:
        x=crocoord[pos][0]
        y=crocoord[pos][1]
        pt.pencolor('#74f442')
        pt.goto(x,y)
        pt.pd()
        cross(pt)
    pt.pu()
    pt.goto(0,0)
    pt.seth(0)

    #print (matrix, j)
    j=j+1
    #flag=0

    if won_game():
        pt.exitonclick()

    if j==9:
        print ('MATCH DRAW')
        pt.exitonclick()


Human = 'O'
AI = 'X'
player = Human
alpha = 1

def main():
    global alpha
    ch = int(input("Choose difficulty level:\n\t1.Easy\t2.Intermediate\t3.Hard\t4.Impossible\n\t-->"))
    if ch == 1:
        alpha = 0.25
    elif ch == 2:
        alpha = 0.5
    elif ch == 3:
        alpha = 0.75
    else:
        alpha = 1
    pt.onscreenclick(get)
    pt.mainloop()
  
if __name__ == "__main__":
	main()
