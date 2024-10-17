import Character
import random
SCREENX_MAX = 1920
SCREENX_MIN = 0
SCREENY_MAX = 1080
SCREENY_MIN = 0

# this is used to trigger the spawning of a new enemy, enemies spawn when screen loads
def spawnEnemy():
    enemy = Character
    x = random.randint(SCREENX_MIN,SCREENX_MAX)
    y = random.randint(SCREENY_MIN,SCREENY_MAX)
    enemy.position(x,y)