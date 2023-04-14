#    game.py - Implementation of the game logic
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

import random
import os
import subprocess
import termcolor
import board
from consolemenu import SelectionMenu


class Game:
    def __init__(self):
        self.board = board.Board()
        self.hits = 0
        self.ships = []
        self.mines = []
        self.turn_count = 0

    def generate_ships_and_mines(self):
        self.mineNumber = 0
        self.shipNumber = 3
        self.lives = 3
        difficulties = ["Easy", "Medium", "Hard", "Impossible", "One Life", "Custom"]
        difficulty_index = SelectionMenu.get_selection(difficulties)
        if difficulties[difficulty_index] == "Easy":
            self.mineNumber = 3
        elif difficulties[difficulty_index] == "Medium":
            self.mineNumber = 5
        elif difficulties[difficulty_index] == "Hard":
            self.mineNumber = 10
        elif difficulties[difficulty_index] == "Impossible":
            self.mineNumber = 20
        elif difficulties[difficulty_index] == "One Life":
            self.mineNumber = 20
            self.lives = 1
        elif difficulties[difficulty_index] == "Custom":
            while True:
                self.mineNumber = int(input("Enter the number of mines (up to 50): "))
                if self.mineNumber > 50:
                    print("Please enter a number less than 50.")
                else:
                    break
            while True:
                self.lives = int(input("Enter the number of lives (up to 50): "))
                if self.lives > 50:
                    print("Please enter a number less than 50.")
                else:
                    break
            while True:
                self.shipNumber = int(input("Enter the number of ships (up to 50):  "))
                if self.shipNumber > 50:
                    print("Please enter a number less than 50.")
                else:
                    break
        elif difficulty_index == 6:
            quit()
        for i in range(self.shipNumber):
            while True:
                ship = ((random.randint(0, self.board.size - 1), random.randint(0, self.board.size - 1)))
                if ship not in self.ships:
                    self.ships.append(ship)
                    break

        for i in range(self.mineNumber):
            while True:
                mine = ((random.randint(0, self.board.size - 1), random.randint(0, self.board.size - 1)))
                if mine not in self.mines and mine not in self.ships:
                    self.mines.append(mine)
                    break
        return difficulties[difficulty_index]
    
    def start(self):

        # Print the initial board
        self.board.print_board()

        # Loop until the player wins
        while self.hits < self.shipNumber and self.lives > 0:
            # Increment the turn count
            self.turn_count += 1

            # Ask the player for a guess
            guess = input("Enter a guess (format: row,column): ")
            guess = guess.split(",")
            guess_row, guess_col = map(int, guess)
            subprocess.run(['clear' if os.name == 'posix' else 'cls'], shell=True)
            
            # Check if the guess is a hit, mine or miss
            if (guess_row, guess_col) in self.ships:
                print(termcolor.colored("Hit!", "green"))
                self.hits += 1
                self.ships.remove((guess_row, guess_col))
                self.board.mark_hit(guess_row, guess_col)
            elif (guess_row, guess_col) in self.mines:
                print(termcolor.colored("Mine!", "red"))
                self.lives -= 1
                self.mines.remove((guess_row, guess_col))
                self.board.mark_mine(guess_row, guess_col)
            else:
                print(termcolor.colored("Miss!", "yellow"))
                self.board.mark_miss(guess_row, guess_col)

            # Print the updated board
            self.board.print_board()
            
            # Check if the player has won
        if self.hits == self.shipNumber:
            print(termcolor.colored("You sunk all the battleships! Congratulations!", "green"))
        elif self.lives == 0:
            print(termcolor.colored("You lost all your lives! Game over!"), "red")
        print(f"Turns: {self.turn_count}")
        print(f"Remaaining ships: {self.ships}")
        print(f"Remaining mines: {self.mines}")
        input("Press Enter to exit...")
