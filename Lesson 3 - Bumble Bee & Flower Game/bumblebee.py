import pgzrun
import random

WIDTH = 600
HEIGHT = 500

bee = Actor("bee")
bee.pos = 100, 100

flower = Actor("flower")
flower.pos = 200, 200

score = 0

def draw():
    screen.blit("background", (0, 0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: "+str(score), color = "blue", topleft = (10, 20))

def placeflower():
    flower.x = random.randint(70, (WIDTH-70))
    flower.y = random.randint(70, (HEIGHT-70))

def update():
    global score
    if keyboard.left:
        bee.x = bee.x-2
    if keyboard.right:
        bee.x = bee.x+2
    if keyboard.up:
        bee.y = bee.y-2
    if keyboard.down:
        bee.y = bee.y+2
    flowercollected = bee.colliderect(flower)
    if flowercollected:
        score = score+10
        placeflower()

# Check if the score has reached or exceeded 500
    if score >= 500:
        print("Score reached 500. Game over!")
        break  # Exit the loop and end the game
    
pgzrun.go()
