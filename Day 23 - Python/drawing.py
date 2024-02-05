import pygame
pygame.init()

fps = 120
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_size = 0
active_color = 'white'
painting = []

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Drawing')

def draw_menu(size, color, clear_button_clicked=False):
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', [0, 70], [WIDTH, 70], 3)

    # Change Brush Sizes (xl, l, m, s)
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', [35, 35], 20)
    l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'white', [95, 35], 15)
    m_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
    pygame.draw.circle(screen, 'white', [155, 35], 10)
    s_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
    pygame.draw.circle(screen, 'white', [215, 35], 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]

    if size == 20:
        pygame.draw.rect(screen, 'green', [10, 10, 50, 50], 3)
    elif size == 15:
        pygame.draw.rect(screen, 'green', [70, 10, 50, 50], 3)
    elif size == 10:
        pygame.draw.rect(screen, 'green', [130, 10, 50, 50], 3)
    elif size == 5:
        pygame.draw.rect(screen, 'green', [190, 10, 50, 50], 3)
    
    # Dispaly Current Clicked Colour with Border
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    # Implement Colors For The Drawing
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    white = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 110, 10, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 35, 25, 25])
    color_rect = [blue, red, green, yellow, teal, purple, white, black]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255), (0, 0, 0)]

    # Function to Clear The Screen
    clear_button = pygame.draw.rect(screen, 'black', [250, 10, 80, 50])
    pygame.draw.rect(screen, 'black', [250, 10, 70, 50], 3)
    font = pygame.font.Font(None, 28)
    clear_text = font.render("CLEAR", True, 'yellow')
    screen.blit(clear_text, (256, 25))

    return brush_list, color_rect, rgb_list, clear_button 

def draw_painting(paints):
    for i in range(len(paints)): # Draw the brush on the window using the mouse.
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])

run = True # Check if the user wants to close the window
clear_button_clicked = False # Check if the user clicked the clear button.

while run:
    timer.tick(fps) # Set the frame rate per second for drawing.
    screen.fill('white') # Display a Pygame window with a white background.
    mouse = pygame.mouse.get_pos() # Get the position of the mouse on the window.
    left_click = pygame.mouse.get_pressed()[0] # Get the state of the left mouse button

    if left_click and mouse[1] > 70:
        painting.append((active_color, mouse, active_size))
    draw_painting(painting) # Allow the user to draw on the window using the mouse.
    if mouse[1] > 70:
        pygame.draw.circle(screen, active_color, mouse, active_size) # Draw the brush on the window using the mouse.
    
    brushes, colors, rgbs, clear_button = draw_menu(active_size, active_color, clear_button_clicked)

    for event in pygame.event.get(): # Close the window if the user closes it
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN: # Change the color of the brush if the user clicks on it
            for i in range(len(brushes)): # Change the size of the brush if the user clicks on it
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)

            for i in range(len(colors)): # Change the color of the brush if the user clicks on it
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

            if clear_button.collidepoint(event.pos): # Clear Screen
                painting = []  
                clear_button_clicked = True


    pygame.display.flip()

    clear_button_clicked = False # Reset Clear Button

pygame.quit()