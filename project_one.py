#Imports
from microbit import *
import random
import music

#Variables
score = 0
snake_x = 2
snake_y = 2
food_x = random.randint(0, 4)
food_y = random.randint(0, 4)
right_button = True
left_button = False
up_button = False
down_button = False
frame_count = 0
speed = 6

while True:
    display.clear()
    display.set_pixel(snake_x, snake_y, 9)
    display.set_pixel(food_x, food_y, 4)
    sleep(500)
    frame_count += 1
    music.set_tempo(bpm=200)
    
    #Change Direction
    if accelerometer.was_gesture('right'):
        right_button = True
        left_button = False
        up_button = False
        down_button = False
    if accelerometer.was_gesture('left'):
        right_button = False
        left_button = True
        up_button = False
        down_button = False
    if accelerometer.was_gesture('up'):
        right_button = False
        left_button = False
        up_button = True
        down_button = False
    if accelerometer.was_gesture('down'):
        right_button = False
        left_button = False
        up_button = False
        down_button = True
    #Automatic Moving
    if right_button == True:
        if frame_count == speed:
            snake_x += 1
            frame_count = 0
    if left_button == True:
        if frame_count == speed:
            snake_x -= 1
            frame_count = 0
    if up_button == True:
        if frame_count == speed:
            snake_y -= 1
            frame_count = 0
    if down_button == True:
        if frame_count == speed:
            snake_y += 1
            frame_count = 0

    if score == 5:
        #Level 2: 2 second wait-time
        music.play(music.POWER_UP)
        speed = 4
        snake_body = True
        score += 1
        continue
    if score == 11:
        #Level 3: 1 second wait-time
        music.play(music.POWER_UP)
        speed = 2
        score += 1
        continue
    if score == 17:
        #Level 4: 0.5 second wait-time
        music.play(music.POWER_UP)
        speed = 1
        score += 1
        continue
    if score == 23:
        #Level 5: Pass
        music.play(music.ENTERTAINER)
        speed = 1
        display.show("You Passed!")
        break
    #Touches Wall
    if snake_x < 0 or snake_x > 4 or snake_y < 0 or snake_y > 4:
        music.play(music.FUNERAL)
        display.show(score)
        break

    #Touches Object
    if snake_x == food_x and snake_y == food_y:
        display.clear()
        food_x = random.randint(0, 4)
        food_y = random.randint(0, 4)
        music.play(['c', 'e', 'g'])
        score += 1
        continue