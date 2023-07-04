# import and set up dependencies
import pgzrun
import random

# define screen parameters
WIDTH = 600
HEIGHT = 400

# initialize the score
score = 0

# define the brick
brick = Actor("brick")
brick.x = 100
brick.y = 150

# create the walls
wall_top = Actor("wall-top")
wall_bottom = Actor("wall-bottom")
gap = 150
wall_top.x = 300
wall_top.y = 0
wall_bottom.x = 300
wall_bottom.y = wall_top.height + gap

# implement left mouse button functionality
def on_mouse_down():
  brick.y = brick.y - 40

# draw the UI and the actors
def draw():
  screen.fill("black")
  brick.draw()
  wall_top.draw()
  wall_bottom.draw()
  screen.draw.text("Score: " + str(score), (500, 30), color="orange")

# update global state -  keep the game running
def update():
  global score
  brick.y = brick.y + 1
  wall_top.x = wall_top.x - 1
  wall_bottom.x = wall_bottom.x - 1
  # implement the logic when the brick falls, crashes, or evades a wall
  if brick.colliderect(wall_top) or brick.colliderect(wall_bottom):
      reset()
  if brick.y > 600:
      reset()
  if wall_top.x < 0:
      score = score + 1
      reset_walls()

# game over functionality - resets the game for now
def reset():
  global score
  score = 0
  print("Game over! Resetting...")
  brick.y = 250
  wall_top.x = 300
  wall_bottom.x = 300

# spawns new walls when a wall is dodged
def reset_walls():
  wall_top.x = 600
  wall_bottom.x = 600
  wall_top.y = random.randint(-50, 50)
  wall_bottom.y = wall_top.y + wall_top.height + gap

# run the game
pgzrun.go()
