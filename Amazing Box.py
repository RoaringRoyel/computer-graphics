from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

animation = True
points = []
speed = 0.2
############ CREATING POINTS ###########
def create_point(x,y):
    if animation:
        global points
        color = (random.random(), random.random(), random.random())
        dx = random.choice([-1, 1])
        dy = random.choice([-1, 1])
        points.append([x,y,color,dx,dy])

########## PLOTING THE POINTS #############
def draw_points():
    glPointSize(10)
    glBegin(GL_POINTS)
    for i in points:
        glColor3f(*i[2]) #getting the color value
        glVertex2f(i[0],i[1]) # getting the co ordinate
    glEnd()

############ END OF CREATING POINTS #############


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
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_points()
    glutSwapBuffers()
    glutPostRedisplay()
############## HANDELING Blinking ##########
import time
def blinking_time():
    if animation:
        glBegin(GL_TRIANGLES)  # Start defining a triangle
        glColor3f(0.0, 0.0, 0.0)  # Red color for the first vertex
        glVertex2f(0, 0)  # First vertex (x, y)
        glVertex2f(0,500)  # First vertex (x, y)
        glVertex2f(500, 500)  # First vertex (x, y)
        glEnd()
        time.sleep(1)
        
        glutPostRedisplay()


######### END OF BLINKING ###############
################ HANDELING NEW POINTS #############
def mouse_click(key, state, x, y):
    global animation
    if key == GLUT_RIGHT_BUTTON and state == GLUT_DOWN and animation:
            create_point(x, 500 - y)
            glutPostRedisplay()
    if key == GLUT_LEFT_BUTTON and state == GLUT_DOWN and animation:
            blinking_time()
            # blink = True
            # glutTimerFunc(blink_interval, start_blinking, 0)

############## END OF NEW POINTS ####################
############# HANDELING ANIMATION #############
def animate():
    global points,speed,animation
    if animation:
        for i in range(len(points)):
            x,y,color,dx,dy = points[i]
            x += dx * speed
            y += dy * speed
            if y >= 500:
                y = 500
                dy = -1
            elif y <=0:
                y = 0 
                dy = 1
            if x >=500:
                x = 500
                dx = -1
            elif x <=0:
                x = 0
                dx = +1
            points[i] = (x,y,color,dx,dy)
    glutPostRedisplay()
############## END ANIMATION #####################
########### HANDELING SPEED ############
def specialKeyListener(key,x,y):
    global speed, animation
    if animation:
        if key==GLUT_KEY_UP:
            speed += 0.2
        if key==GLUT_KEY_DOWN:
            speed -= 0.2
            speed = max(0.2,speed)
    glutPostRedisplay()

############# END OF SPEED #############

############ Pasueing Controll ########
def keyboard_listener(key,x,y):
    global animation
    if key == b' ':
        if animation:
            animation = False
        else:
            animation = True
    glutPostRedisplay() 
######### END OF PAUSE #############



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
#glClearColor(1.0,1.0,1.0, 1)
wind = glutCreateWindow(b"Amazing Box") 
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutMouseFunc(mouse_click)

glutKeyboardFunc(keyboard_listener) 
glutSpecialFunc(specialKeyListener)

glutMainLoop()
