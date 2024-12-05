from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


########### COLOR CONTROLLER #############

background_color = [0.0, 0.0, 0.0] #setting the background color
line_color = [1.0, 1.0, 1.0] # setting all the line color

def color_controller():
    
    global line_color #handeling the line_colors
    print("From color controleer")
    print(line_color)
    line_color = [1.0 - i for i in background_color]
    print(line_color)
    print(background_color,"Background color")

##### END OF COLOR CONTROLLER ###########



############# Drawing All Lines ###########
########## Drawing house #############
def draw_house():
    glLineWidth(5)
    glBegin(GL_TRIANGLES)  
    glVertex2f(400,300)
    glVertex2f(100,300)
    glVertex2f(250,400)
    glEnd()
    glPointSize(5)
    glLineWidth(5)
    glBegin(GL_LINES)

    glVertex2f(380,300)
    glVertex2f(380,100)
    glVertex2f(120,300)
    glVertex2f(120,100)
    glVertex2f(120,100)
    glVertex2f(380,100)
    glEnd()


    glPointSize(5)
    glLineWidth(5)
    glBegin(GL_LINES)

    glVertex2f(160,100)
    glVertex2f(160,210)
    glVertex2f(220,100)
    glVertex2f(220,210)
    glVertex2f(160,210)
    glVertex2f(220,210)

    glVertex2f(350,200)
    glVertex2f(350,250)
    glVertex2f(300,200)
    glVertex2f(300,250)
    glVertex2f(350,250)
    glVertex2f(300,250)
    glVertex2f(350,200)
    glVertex2f(300,200)
    glVertex2f(300,225)
    glVertex2f(350,225)
    glVertex2f(325,250)
    glVertex2f(325,200)
    glEnd()

    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(210,150)
    glEnd()


############# END OF HOUSE ###############

########### Drawing Rain #########
rain_x = 0
rain_y = 500
raindrops = [(random.randint(0, 1000), random.randint(0, 500)) for _ in range(100)]
tilt = 0 
def draw_rain():
    glLineWidth(2)
    glBegin(GL_LINES)

    global tilt
    for x,y in raindrops:
        glVertex2f(x, y)  # Starting point of the line
        glVertex2f(x+ tilt, y-100)  # Ending point of the line
    

    glEnd()
####### END OF RAIN #############
def draw_lines():
    draw_house() #drawing house
    draw_rain() #drawing rain

############ END OF ALL LINES ##########################

def iterate():
    glViewport(0, 0, 1000, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glClearColor(*background_color, 1.0) #setting the background 
    glColor3f(*line_color) #setting the color of lines
    #call the draw methods here
    print("From show screen")
    print(line_color)
    print(background_color)
    print("Ends")
    draw_lines()
    glutSwapBuffers()
    glutPostRedisplay()

############## handeling Key + Color #########
def keyboard_listener(key,x,y):
    global background_color,animation
    if animation:
        if key == b'w':  # Increase brightness (toward white)
            background_color = [min(x + 0.1, 1.0) for x in background_color]
        elif key == b's':  # Decrease brightness (toward black)
            background_color = [max(x - 0.1, 0.0) for x in background_color]
    if key == b' ':
        if animation:
            animation = False
        else:
            animation = True
    
    color_controller()  # update the background with controller
    glutPostRedisplay()  # reload the file


def specialKeyListener(key,x,y):
    global raindrops,tilt,animation
    if animation:
        if key==GLUT_KEY_RIGHT:
            tilt += 3
            raindrops = [(((x + 3)% 1000), y) for x, y in raindrops]
        if key==GLUT_KEY_LEFT:
            tilt -= 3
            raindrops = [(((x - 3)% 1000), y) for x, y in raindrops]
    glutPostRedisplay()
########### HANDELING ANIMATION ##############
speed = 0.2
animation = True
def animate():
    global rain_x , rain_y , speed,animation
    if animation:
        for i in range(len(raindrops)):
            x,y = raindrops[i]
            y = (y - speed) % 500
            raindrops[i] = (x,y)

    glutPostRedisplay()  # Redraw the screen for smooth animation

############ END OF ANIMATION ##############

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Building a House in Rainfall") #window name
color_controller() #background color changing
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutKeyboardFunc(keyboard_listener) #listeniing from the keayboard
glutSpecialFunc(specialKeyListener)

glutMainLoop()
