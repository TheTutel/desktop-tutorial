import time
import turtle
from idlelib.run import exit_now

#вопрос - время года
print("You have entered the cloth-room")
print("-Which clothes should we wear today?")
print("Which season is outside?")
weather=input()
if weather=="Winter":
    print("you should wear something warm")
    #you should wear something warm
    for i in range(6):
        turtle.forward(50)
        turtle.right(45)
        turtle.forward(20)
        turtle.back(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.back(20)
        turtle.right(45)
        turtle.back(50)
        turtle.right(60)
    exit()
if weather=="Summer":
    print("you should wear something not as warm as winter clothes")
    #you should wear something not as warm as winter clothes
else:
    exit()