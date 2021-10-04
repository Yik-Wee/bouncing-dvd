from random import randint
from helpers import make_colour


class DVD:
    delta_x: int = 5  # change in x coord
    delta_y: int = 1  # change in y coord
    delta_colour: int = 1  # change in ANSI 256-colour value

    LOGO = (  # list of lines representing the DVD logo
        '⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⡀',
        '⠀⢠⣿⣿⡿⠀⠀⠈⢹⣿⣿⡿⣿⣿⣇⠀⣠⣿⣿⠟⣽⣿⣿⠇⠀⠀⢹⣿⣿⣿',
        '⠀⢸⣿⣿⡇⠀⢀⣠⣾⣿⡿⠃⢹⣿⣿⣶⣿⡿⠋⢰⣿⣿⡿⠀⠀⣠⣼⣿⣿⠏',
        '⠀⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀⢿⣿⣿⠏⠀⠀⢸⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀',
        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣸⣟⣁⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
        '⣠⣴⣶⣾⣿⣿⣻⡟⣻⣿⢻⣿⡟⣛⢻⣿⡟⣛⣿⡿⣛⣛⢻⣿⣿⣶⣦⣄⡀⠀',
        '⠉⠛⠻⠿⠿⠿⠷⣼⣿⣿⣼⣿⣧⣭⣼⣿⣧⣭⣿⣿⣬⡭⠾⠿⠿⠿⠛⠉⠀ '
    )

    def __init__(self, min_colour: int, max_colour: int, boundaries: tuple) -> None:
        # initialise min & max ANSI 256 colour values, initialise random ANSI 256 colour value
        self.min_colour = min_colour
        self.max_colour = max_colour
        self.colour = randint(self.min_colour, self.max_colour)

        # initialise DVD logo dimensions
        self.width = len(self.LOGO[0])
        self.height = len(self.LOGO)

        # initialise (x, y) and max (x, y) coordinates
        self.max_x = boundaries[0] - self.width
        self.max_y = boundaries[1] - self.height
        self.coordinates = [randint(0, self.max_x), randint(0, self.max_y)]

    def update_and_render(self, terminal_width, terminal_height) -> None:
        self.update_boundaries(terminal_width, terminal_height)
        self.update_coordinates()
        self.render()
        self.morph_colour()

    def render(self) -> None:
        print('\n' * self.coordinates[1])  # go to y coord
        for y in range(self.height):  # print dvd lines
            print(' ' * self.coordinates[0] + make_colour(self.LOGO[y], self.colour))
        print('\n' * (self.max_y - self.coordinates[1]))  # print remaining empty lines

    def update_boundaries(self, terminal_width: int, terminal_height: int) -> None:
        self.max_x = terminal_width - self.width
        self.max_y = terminal_height - self.height

    def update_coordinates(self) -> None:
        self.coordinates[0] += self.delta_x
        self.coordinates[1] += self.delta_y

        min_x, min_y = 0, 3

        # move in opposite horizontal direction if hit the side walls
        if self.coordinates[0] > self.max_x:
            self.coordinates[0] = self.max_x
            self.delta_x = -self.delta_x
        elif self.coordinates[0] < min_x:
            self.coordinates[0] = min_x
            self.delta_x = -self.delta_x

        # move in opposite vertical direction if hit the ceiling/floor
        if self.coordinates[1] > self.max_y:
            self.coordinates[1] = self.max_y
            self.delta_y = -self.delta_y
        elif self.coordinates[1] < min_y:
            self.coordinates[1] = min_y
            self.delta_y = -self.delta_y

    def morph_colour(self) -> None:
        self.colour += self.delta_colour

        if self.colour > self.max_colour:  # max set colour value reached -> start decrementing colour
            self.colour = self.max_colour
            self.delta_colour = -self.delta_colour
        elif self.colour < self.min_colour:  # min set colour value reached -> start incrementing colour
            self.colour = self.min_colour
            self.delta_colour = -self.delta_colour
