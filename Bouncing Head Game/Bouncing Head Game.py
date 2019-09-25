import pygame as pg
import random
pg.init() # Initialisation function

display_width = 800
display_height = 600


# Hello Yale peeps, these images were included in the zipped folder
ball_image = pg.image.load('laith.png') 
paddle_image = pg.image.load('carrot.png')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pg.display.set_mode((display_width, display_height)) # Sets the display
pg.display.set_caption('Bouncing Head Game')
clock = pg.time.Clock() # Frames per second, how we are going to measure frames per second

def ball(x,y):
    gameDisplay.blit(ball_image,(x,y))
def paddle(x,y):
    gameDisplay.blit(paddle_image, (x,y))

def game_loop():

    x_ball = display_width*0.5
    y_ball = display_height*0.4

    x_paddle = (display_width*0.45)
    y_paddle = (display_height*0.85)

    x_pchange = 0
    starts = [-4,-3,3,4]
    random.shuffle(starts)
    x_bchange = starts[0]
    y_bchange = -4

    game_exist = False

    while not game_exist:

        # Main loop for events
        for event in pg.event.get(): # This function creates a list of events that could happen in frames per second
            if event.type == pg.QUIT:
                game_exist = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_pchange = -4
                elif event.key == pg.K_RIGHT:
                    x_pchange = 4



        gameDisplay.fill(white)

        # Changing position
        x_paddle += x_pchange
        x_ball += x_bchange
        y_ball += y_bchange

        paddle(x_paddle,y_paddle)
        ball(x_ball,y_ball)

        # Boundaries
        if (x_paddle + 180) > display_width or x_paddle < 0:
            x_pchange = 0
        if (x_ball + 50) > display_width or x_ball < 0:
            x_bchange = -(x_bchange)
        if  y_ball < 0:
            y_bchange = -(y_bchange)
        elif (y_ball + 95) > display_height:
            y_bchange = 0
            x_bchange = 0
        if (x_ball+50) >= x_paddle and x_ball <= (x_paddle+180):
            if (y_ball+75) >= y_paddle and y_ball <= (y_paddle+40):
                y_bchange = -(y_bchange)
        pg.display.update() # If you put a parameter, it will only update that one thing. Processing will be easier if you do one thing at a time.
                            # No parameters, it will update everything. You can also use .flip() which updates everything
        clock.tick(60) # The parameter is the frames per second.

game_loop()
pg.quit()
quit()
