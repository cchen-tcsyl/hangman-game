import random
from turtle import Turtle, Screen
import time as ti

# different methods that accomplish tasks

t = Turtle()
s = Screen()

t.speed(0)
t.width(20)



def start_game():
  
  wordbank = ['sandwich', 'house', 'pizza', 'grape'] 
  word = random.choice(wordbank)
  guess = '_ ' * len(word)
  print(guess)
  # rope, head, eyes, nose, mouth, right arm, left arm, neck, body, left leg, right leg
  lives = 11

  while lives > 0 and guess.find('_') != -1: 
    digit = (input('Enter a letter: '))[0:1]
    changed = False
    for x in range(len(word)):
      if word[x:x+1] == digit:
        changed = True
        guess =  guess[0:2*x] + digit + guess[2*x + 1:]
    print (guess)
    if changed == False:
      lives -= 1

      print('The letter is not in the word, you lost a life')
      # t.write( 'You have ' + str(lives) + ' lives', font = ('Sans', 40, 'italic'))
      draw_limbs(lives)
    else:
      print ('The letter is correct')
  t.penup()
  t.goto(-50,0)
  t.pendown()
  if lives == 0:
    t.write(' You Lost, Game Over ', font=("Garamond", 40, "italic"))
  else:
    t.write(' You Won, Hurray ', font=("Garamond", 40, "italic"))

def draw_limbs(num):
  if num == 10:
    draw_head()
  elif num == 9:
    draw_eyes()
  elif num == 8:
    draw_nose()
  # elif num == 7:
  #   draw_mouth()
  # elif num == 6:
  #   draw_neck()
  # elif num == 5:
  #   draw_arm(1)
  # elif num == 4
  #   draw_arm(0)
  # elif num == 3
  #   draw_body()
  # elif num == 2
  #   draw_leg(1)
  # elif num == 1
  #   draw_leg(0)
  # else:
  #   t.write(' Oh No I died ', font=("Garamond", 40, "italic")
  #   ti.sleep(2)
  pass

def draw_head():
  t.width(1)
  t.setheading(180)
  t.begin_fill()
  t.circle(40, steps = 250)
  t.end_fill()

def draw_eyes():
  t.hideturtle()
  t.setheading(270)
  t.width(1)
  t.fillcolor('white')
  t.forward(20)
  t.right(90)
  t.forward(15)
  t.begin_fill()
  t.circle(5, steps = 200)
  t.end_fill()

  t.right(180)
  t.forward(30)
  t.right(180)

  t.begin_fill()
  t.circle(5, steps = 200)
  t.end_fill()

  t.forward(15)
  t.left(90)
  t.forward(20)

def draw_nose():
  
  t.begin_fill()
  t.left(30)
  t.forward(10)
  t.right(120)
  t.forward(10)
  t.right(120)
  t.forward(10)
  t.right(150)
  t.forward(40)
  t.end_fill()

def draw_post():
  t.penup()
  t.goto(-300, 300)
  t.pendown()
  t.fd(200)
  t.back(100)
  t.left(90)
  t.fd(600)
  t.rt(90)
  t.fd(500)
  t.rt(90)
  t.fd(100)

draw_post()
start_game()