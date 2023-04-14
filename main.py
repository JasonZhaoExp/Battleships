#    main.py - Main file for Battleships game
#    Copyright (C) 2023  Jason Zhao
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import subprocess
import time
import pyfiglet
import termcolor
from game import Game

# Welcome screen
subprocess.run(['clear' if os.name == 'posix' else 'cls'], shell=True)
print(termcolor.colored(pyfiglet.figlet_format("Battleships") + """
Version 1.0, Developed by Jason""", "green"))
time.sleep(5)

# Clear the screen
subprocess.run(['clear' if os.name == 'posix' else 'cls'], shell=True)

# Create a new game instance and start it
game = Game()
game.generate_ships_and_mines()
game.start()
