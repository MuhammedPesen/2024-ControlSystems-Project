import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np


# Define vertices and edges (same as before)
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


# Function to load texture
def load_texture(image_name):
    textureSurface = pygame.image.load(image_name)
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    textureID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textureID)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return textureID

def draw_textured_cuboid(textureID):
    glBindTexture(GL_TEXTURE_2D, textureID)
    glBegin(GL_QUADS)

    # Front Face
    glTexCoord2f(0, 0); glVertex3fv(vertices[0])
    glTexCoord2f(1, 0); glVertex3fv(vertices[1])
    glTexCoord2f(1, 1); glVertex3fv(vertices[2])
    glTexCoord2f(0, 1); glVertex3fv(vertices[3])

    # Back Face
    glTexCoord2f(1, 0); glVertex3fv(vertices[5])
    glTexCoord2f(1, 1); glVertex3fv(vertices[6])
    glTexCoord2f(0, 1); glVertex3fv(vertices[7])
    glTexCoord2f(0, 0); glVertex3fv(vertices[4])

    # Top Face
    glTexCoord2f(0, 1); glVertex3fv(vertices[2])
    glTexCoord2f(0, 0); glVertex3fv(vertices[1])
    glTexCoord2f(1, 0); glVertex3fv(vertices[5])
    glTexCoord2f(1, 1); glVertex3fv(vertices[6])

    # Bottom Face
    glTexCoord2f(1, 1); glVertex3fv(vertices[3])
    glTexCoord2f(0, 1); glVertex3fv(vertices[0])
    glTexCoord2f(0, 0); glVertex3fv(vertices[4])
    glTexCoord2f(1, 0); glVertex3fv(vertices[7])

    # Right face
    glTexCoord2f(1, 0); glVertex3fv(vertices[1])
    glTexCoord2f(1, 1); glVertex3fv(vertices[2])
    glTexCoord2f(0, 1); glVertex3fv(vertices[6])
    glTexCoord2f(0, 0); glVertex3fv(vertices[5])

    # Left Face
    glTexCoord2f(0, 0); glVertex3fv(vertices[0])
    glTexCoord2f(1, 0); glVertex3fv(vertices[3])
    glTexCoord2f(1, 1); glVertex3fv(vertices[7])
    glTexCoord2f(0, 1); glVertex3fv(vertices[4])

    glEnd()









def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    glEnable(GL_TEXTURE_2D)
    textureID = load_texture('top.jpg')  # Replace with your texture image

    rotation_speed = 1  # Degrees per frame

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Apply rotation around the Y-axis 
        glRotatef(rotation_speed, 0, 1, 0)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_textured_cuboid(textureID)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()