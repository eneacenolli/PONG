# Implementation of classic arcade game Pong

import simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
score1 = 0
score2 = 0
paddle1_vel = 0
paddle2_vel = 0
paddle1_start_point = [0,160]
paddle1_end_point = [0,240]
paddle2_start_point = [600,160]
paddle2_end_point = [600,240]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel[0] = random.randrange(120,240)
        ball_vel[1] = -(random.randrange(60,180))
    elif direction == LEFT:
        ball_vel[0] = -(random.randrange(120,240))
        ball_vel[1] = -(random.randrange(60,180))

#function when a player scores puts the ball in the centre and 
#ball goes to the opposide direction ands keeps score
def paddle1_reflect():
    global score1
    global score2
    global ball_pos
    global BALL_RADIUS   
    global ball_vel , PAD_HEIGHT , PAD_WIDTH
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH) and ball_pos[1] > ( paddle1_start_point[1]- BALL_RADIUS) and ball_pos[1] < (paddle1_start_point[1]+ PAD_HEIGHT +BALL_RADIUS):
        ball_vel[0] = - ball_vel[0] *1.1
    
    
def paddle2_reflect():
    global score1
    global score2
    global ball_pos
    global BALL_RADIUS,paddle1_start_point
    global ball_vel , PAD_HEIGHT , PAD_WIDTH                                                                  
    if ball_pos[0] >= WIDTH -(BALL_RADIUS + PAD_WIDTH) and ball_pos[1] > ( paddle2_start_point[1] - BALL_RADIUS) and ball_pos[1] < (paddle2_start_point[1]+ PAD_HEIGHT + BALL_RADIUS):
        ball_vel [0] = - ball_vel [0] *1.1
 
def button_handler():
    global score1 , score2
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    score1 = 0	
    score2 = 0
    spawn_ball(LEFT)
        
def score():
    global score1
    global score2
    return str(score1)+'       '+str(score2)        

def paddle1_stop():
    global paddle1_vel, paddle2_vel
    global paddle1_start_point,paddle1_end_point
    if paddle1_start_point <= [0,0]:
        paddle1_start_point  = [0,0]
        paddle1_end_point = [0,PAD_HEIGHT]                
    elif paddle1_end_point >= [0,HEIGHT]:
        paddle1_start_point = [0,(HEIGHT - PAD_HEIGHT)]
        paddle1_end_point = [0,HEIGHT]  

def paddle2_stop():
    global paddle1_vel, paddle2_vel
    global paddle2_start_point,paddle2_end_point
    if paddle2_start_point <= [600,0]:
        paddle2_start_point = [600,0]
        paddle2_end_point = [600,PAD_HEIGHT]
    elif paddle2_end_point >= [600,400]:
        paddle2_start_point = [600,(HEIGHT - PAD_HEIGHT)]
        paddle2_end_point = [600,400]  
    
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]
    score1 = 0
    score2 = 0
    paddle1_vel = 0
    paddle2_vel = 0
    paddle1_start_point = [0,160]
    paddle1_end_point = [0,240]
    paddle2_start_point = [600,160]
    paddle2_end_point = [600,240]
    spawn_ball(LEFT)
    
            
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_end_point, paddle2_start_point, paddle1_start_point,paddle2_end_point
    paddle1_reflect()   
    paddle2_reflect()
    paddle1_stop()
    paddle2_stop()
    
    
    #reflect 
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel [1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT -BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball    
    ball_pos [0] += ball_vel[0] / 60
    ball_pos [1] += ball_vel[1] / 60
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_start_point[1] += paddle1_vel
    paddle1_end_point[1] += paddle1_vel
    paddle2_start_point[1] += paddle2_vel
    paddle2_end_point[1] += paddle2_vel
    
    # draw paddles
    canvas.draw_line(paddle1_start_point,paddle1_end_point,15,'White')
    canvas.draw_line(paddle2_start_point,paddle2_end_point,15,'White')
    
    # determine whether paddle and ball collide    
    if ball_pos [0] <= BALL_RADIUS:
        score2 += 1
        spawn_ball(RIGHT)
    elif ball_pos [0] >= WIDTH - BALL_RADIUS:
        score1 += 1
        spawn_ball(LEFT)
        
    # draw scores
    canvas.draw_text(score(),(250,40),40,'White')
    
def keydown(key):
    acc = 5
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP ['down']:
        paddle2_vel += acc             
    elif key == simplegui.KEY_MAP ['s']:
        paddle1_vel += acc
    if key == simplegui.KEY_MAP ['up']:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP ['w']:
        paddle1_vel -= acc
    
def keyup(key):
    acc = 5
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP ['down']:
        paddle2_vel = 0             
    elif key == simplegui.KEY_MAP ['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP ['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP ['w']:
        paddle1_vel = 0             
            
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)
# start frame
new_game()
frame.start()
