from turtle import Turtle, Screen
import random 

r_speed=random.randint(0,10)
racer_color=["red","blue","green","yellow","orange","purple"]
racer_start=[100,80,60,40,20,0]
racers=[]
distance=200

def random_speed():
  r_speed=random.randint(0,10)
  return r_speed
    

def race_setup(racer_color,racer_start):
  for i in range(len(racer_start)):
    racer=Turtle()
    racer.color(racer_color[i])
    racer.speed(random_speed())
    racer.penup()
    racer.sety(racer_start[i])
    racers.append(racer)

def race_start(racers):
  is_race_on=True
  while is_race_on:
    for i in range(len(racers)):
      racers[i].pendown()
      racers[i].forward(random_speed())
      if racers[i].xcor()>distance:
        is_race_on=False
        screen.print(f"Racer {i} won the race")
    

race_setup(racer_color,racer_start)
race_start(racers)
screen=Screen()
screen.setup(width=800,height=600)
screen.exitonclick()
    