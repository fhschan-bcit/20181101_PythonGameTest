import pygame


def main():
    # initialize pygame module
    pygame.init()

    # load and set logo
    logo = pygame.image.load('./test_logo.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Racing Game')

    # create a surface on screen that has size of 240 x 180
    screen = pygame.display.set_mode((800, 600))

    # create a game time clock
    clock = pygame.time.Clock()

    # define a variable to control the main loop
    running = True

    while running:
        # event handling, gets all event from the event queue (key, mouse click, etc per frame per sec)
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        # for updating the entire the whole surface (the window), use pygame.display.flip()
        # for updating a part of the surface (window), use pygame.display.update(parameter)
        pygame.display.update()
        # defining fps, parameter is the fps
        clock.tick(30)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()