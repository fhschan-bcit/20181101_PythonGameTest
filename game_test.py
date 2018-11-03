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

    car_width = 100
    car_height = 97

    boundary_top = 0
    boundary_left = 0
    boundary_right = display_width - car_width  # 100px is the width of the car image
    boundary_bottom = display_height - car_height  # 98px is the height of the car image

    # load and set logo
    logo = pygame.image.load('./images/car.png')
    pygame.display.set_icon(logo)

    # game name
    pygame.display.set_caption('Racing Game')

    # create a surface on screen that has size of 800 x 600 (w x h)
    gameDisplay = pygame.display.set_mode((display_width, display_height))

    # create a game time clock
    clock = pygame.time.Clock()

    # created car image
    carImg = pygame.image.load('./images/car.png')

    def ai_car(ai_x, ai_y):
        gameDisplay.blit(carImg, (ai_x, ai_y))

    def car(player_x, player_y):
        # blit draws on to the surface
        gameDisplay.blit(carImg, (player_x, player_y))

    def game_loop():
        x = (display_width * 0.45)
        y = (display_height * 0.8)

        x_change = 0
        y_change = 0

        ai_x = display_width * 0.3
        ai_y = display_height * 0.1

        ai_x_change = 0
        ai_y_change = 5

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
                        x_change -= 10
                        # x = coord_sub(x)
                    elif event.key == pygame.K_RIGHT:
                        x_change += 10
                        # x = coord_add(x)

                    if event.key == pygame.K_UP:
                        y_change -= 10
                        # y = coord_sub(y)
                    elif event.key == pygame.K_DOWN:
                        y_change += 10
                        # y = coord_add(y)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0

            x += x_change
            y += y_change

            ai_y += ai_y_change

            x = boundary_check_x(x, boundary_left, boundary_right)
            y = boundary_check_y(y, boundary_top, boundary_bottom)

            # ai_x = boundary_check_x(ai_x, boundary_left, boundary_right)
            ai_y = ai_boundary_check_y(ai_y, boundary_top, boundary_bottom)

            gameDisplay.fill(white)
            running = ai_player_collision_check(x, y, ai_x, ai_y)
            car(x, y)
            ai_car(ai_x, ai_y)
            # for updating the entire the whole surface (the window), use pygame.display.flip()
            # for updating a part of the surface (window), use pygame.display.update(parameter)
            pygame.display.update()
            # defining fps, parameter is the fps
            clock.tick(60)

    def ai_player_collision_check(player_x, player_y, ai_x, ai_y):
        """Check AI car and player car collision"""
        p_left = player_x
        p_right = player_x + car_width
        p_top = player_y
        p_bottom = player_y + car_height

        ai_left = ai_x
        ai_right = ai_x + car_width
        ai_top = ai_y
        ai_bottom = ai_y + car_height

        if ((ai_left <= p_left <= ai_right) or (ai_left <= p_right <= ai_right)) and (
                ((ai_top <= p_top <= ai_bottom) or (ai_top <= p_bottom <= ai_bottom))):
            return False
        else:
            return True

    def ai_boundary_check_y(param_to_check, boundary_top_ai, boundary_bottom_ai):
        """Set the AI car's boundary if it reaches the boundary"""
        if param_to_check > boundary_bottom_ai:
            param_to_check = boundary_top_ai
        return param_to_check

    def boundary_check_x(param_to_check, boundary_left_player, boundary_right_player):
        if param_to_check < boundary_left_player:
            param_to_check = boundary_left_player
        if param_to_check > boundary_right_player:
            param_to_check = boundary_right_player
        return param_to_check

    def boundary_check_y(param_to_check, boundary_top_player, boundary_bottom_player):
        if param_to_check > boundary_bottom_player:
            param_to_check = boundary_bottom_player
        if param_to_check < boundary_top_player:
            param_to_check = boundary_top_player
        return param_to_check

    game_loop()
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
