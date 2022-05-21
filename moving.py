import pygame
import random
import sys
# define the pygame main window surface object.
MAIN_WINDOW_SURFACE = None
# define the pygame.time.Clock object to control the frames refresh frequency.
FRAME_PER_SECOND_CLOCK = None
# define the frame per second numbers, that means one second draw 23 frame at most.
FPS = 23
# define the text surface object.
TEXT_SURFACE_OBJECT = None
# define the direction constants.
LEFT = 'LEFT'
RIGHT = 'RIGHT'
DIRECTION = LEFT
# the text move steps.
MOVE_STEP = 5
# define the text surface rectangle's center (x, y) coordinates.
TEXT_CENTER_X = 0
TEXT_CENTER_Y = 0
# this function initialize the pygame application.


def initialize_pygame():

    pygame.init()

    # create the game main window.
    main_window_size = (1000, 300)

    global MAIN_WINDOW_SURFACE
    MAIN_WINDOW_SURFACE = pygame.display.set_mode(
        main_window_size, pygame.RESIZABLE)

    # set the window title.
    window_title = 'Pygame Draw Moving Text With Specified Text Font Example.'
    pygame.display.set_caption(window_title)

    # create a pygame.time.Clock object.
    global FRAME_PER_SECOND_CLOCK
    FRAME_PER_SECOND_CLOCK = pygame.time.Clock()


# get a text font from the system supported font list.
def get_random_text_font():

    # get all system supported fonts.
    system_fonts_list = pygame.font.get_fonts()

    system_fonts_list = ['signpainter', 'shree714', 'songti']
    # get a random text font from the above fonts list.
    ret_text_font = random.choice(system_fonts_list)

    return ret_text_font
# initialize the moving text surface object.


def initialize_moving_text():

    # get a random text font.
    text_font = get_random_text_font()
    print('text_font = ', text_font)

    # create a pygame.font.Font object use the pygame.font.SysFont() method.
    font_object = pygame.font.SysFont(text_font, 32, bold=True, italic=True)

    # define the text color and text background color.
    text_color = pygame.Color('green')
    text_background_color = pygame.Color('blue')
    global TEXT_SURFACE_OBJECT
    # call the pygame.font.Font's object's render() method to create the text surface object.
    TEXT_SURFACE_OBJECT = font_object.render(
        'Hello pygame world!', True, text_color, text_background_color)

    # get the pygame main screen window's width and height.
    window_width = MAIN_WINDOW_SURFACE.get_width()
    window_height = MAIN_WINDOW_SURFACE.get_height()

    # calculate the text surface object's rectangle object's center coordinates.
    global TEXT_CENTER_X
    global TEXT_CENTER_Y

    # when the pygame starts, the text surface object is located at the main window screen center.
    if TEXT_CENTER_X == 0:

        TEXT_CENTER_X = window_width/2
        TEXT_CENTER_Y = window_height/2

    # get the text surface object's pygame.Rect object.
    text_rect_object = TEXT_SURFACE_OBJECT.get_rect()
    # position the text rectangle object' center to coordinate(TEXT_CENTER_X, TEXT_CENTER_Y).
    text_rect_object.center = (TEXT_CENTER_X, TEXT_CENTER_Y)

    # clear the main window screen by drawing white color.
    MAIN_WINDOW_SURFACE.fill(pygame.Color('white'))
    # draw the text surface object to the pygame main window.
    MAIN_WINDOW_SURFACE.blit(TEXT_SURFACE_OBJECT, text_rect_object)
# this function will move the text on the screen by changing the text surface object center point coordinates.


def draw_moving_text():

    global DIRECTION, TEXT_CENTER_X
    # if move to left.
    if DIRECTION == LEFT:
        # text center point's x coordinate will decrease.
        TEXT_CENTER_X -= MOVE_STEP
    # if move to right.
    elif DIRECTION == RIGHT:
        # text center point's x coordinate will increase.
        TEXT_CENTER_X += MOVE_STEP

    # get the main window's width.
    window_width = MAIN_WINDOW_SURFACE.get_width()

    # if reach the left border.
    # change move direction to right. DIRECTION = RIGHT # if touch the right border. elif TEXT_CENTER_X >= window_width:
    if TEXT_CENTER_X <= 0:
        # change move direction to left.
        DIRECTION = LEFT

    # if the text move to the main window screen center.
    if TEXT_CENTER_X == window_width/2:
        # change the text font.
        initialize_moving_text()
    else:
        # get the text surface object's rectangle object.
        text_rect_object = TEXT_SURFACE_OBJECT.get_rect()
        # position the text surface object to coordinates (TEXT_CENTER_X, TEXT_CENTER_Y).
        text_rect_object.center = (TEXT_CENTER_X, TEXT_CENTER_Y)
        # clear the window by fill the white background color.
        MAIN_WINDOW_SURFACE.fill(pygame.Color('white'))
        # draw the text surface object to the main window screen with the pygame.Rect position.
        MAIN_WINDOW_SURFACE.blit(TEXT_SURFACE_OBJECT, text_rect_object)


def main_loop():

    while True:

        draw_moving_text()

        # Loop to get events and listen for event status.
        for event in pygame.event.get():

            # if user click the window close button.
            if event.type == pygame.QUIT:

                # quit pygame.
                pygame.quit()

                # quit the application.
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    print('The Esc key is pressed.')

                    # quit pygame.
                    pygame.quit()

                    # quit the application.
                    sys.exit()

            elif event.type == pygame.VIDEORESIZE:

                # draw the pixel units again when user resize the pygame window.
                draw_moving_text()

        pygame.display.update()

        # set the frame count that will be printed in one seconds.
        FRAME_PER_SECOND_CLOCK.tick(FPS)


if __name__ == '__main__':

    initialize_pygame()

    initialize_moving_text()

    main_loop()
