import serial
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Set up the serial connection
ser = serial.Serial('COM4', 115200)  # Replace 'COM4' with your actual COM port

# Define vertices and edges for the cuboid
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
)

def draw_cuboid():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        try:
            line = ser.readline().decode('utf-8').strip().split(',')
            if len(line) == 3:  # Expecting three values for yaw, pitch, and roll
                yaw, pitch, roll = map(float, line)
                # Convert degrees to radians for OpenGL
                yaw, roll, pitch = np.radians(yaw), np.radians(pitch), np.radians(roll)

                # Reset transformations and apply the new ones
                glLoadIdentity()
                gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
                glTranslatef(0.0, 0.0, -5)
                glRotatef(np.degrees(roll), 0, 0, 1)
                glRotatef(np.degrees(pitch), 1, 0, 0)
                glRotatef(-np.degrees(yaw), 0, 1, 0)  # Inverting yaw for correct direction
            else:
                print(line)
                continue
        except Exception as e:
            print(e)

                # Clear the screen and draw the cuboid
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_cuboid()
        pygame.display.flip()
        pygame.time.wait(10)

try:
    main()
finally:
    ser.close()  # Ensure the serial port is closed
