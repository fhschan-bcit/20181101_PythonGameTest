import pygame


def main():
    # initialize pygame module
    pygame.init()

    # global variables
    display_width = 800
    display_height = 600

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    boundary_top = 0
    boundary_left = 0
    boundary_right = display_width - 100  # 100px is the width of the car image
    boundary_bottom = display_height - 98 # 98px is the height of the car image

    # load and set logo
    logo = pygame.image.load('./images/car.png')
    pygame.display.set_icon(logo)

    # game name
    pygame.display.set_caption('Racing Game')

    # create a surface on screen that has size of 800 x 600 (w x h)
    gameDisplay = pygame.display.set_mode((display_width, display_height))

    # create a game time clock
    clock = pygame.time.Clock()

    carImg = pygame.image.load('./images/car.png')

    def car(x, y):
        # blit draws on to the surface
        gameDisplay.blit(carImg, (x, y))

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    # define a variable to control the main loop
    running = True

    while running:
        # event handling, gets all event from the event queue (key, mouse click, etc per frame per sec)
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

            # checking keyboard inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10

                if event.key == pygame.K_UP:
                    y_change = -10
                elif event.key == pygame.K_DOWN:
                    y_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change

        if x < boundary_left:
            x = boundary_left

        if x > boundary_right:
            x = boundary_right

        if y > boundary_bottom:
            y = boundary_bottom

        if y < boundary_top:
            y = boundary_top

        gameDisplay.fill(white)
        car(x, y)
        # for updating the entire the whole surface (the window), use pygame.display.flip()
        # for updating a part of the surface (window), use pygame.display.update(parameter)
        pygame.display.update()
        # defining fps, parameter is the fps
        clock.tick(60)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
