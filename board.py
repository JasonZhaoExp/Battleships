#    board.py - Implementation of the board and markers for battleships
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

import termcolor

class Board:
    def __init__(self):
        self.size = 10
        self.board = [[termcolor.colored("W", "blue") for _ in range(self.size)] for _ in range(self.size)]

    def mark_hit(self, row, col):
        self.board[row][col] = termcolor.colored("X", "green")

    def mark_miss(self, row, col):
        self.board[row][col] = termcolor.colored("O", "yellow")

    def mark_mine(self, row, col):
        self.board[row][col] = termcolor.colored("X", "red")

    def print_board(self):
        # Print column labels
        print("  ", end="")
        for col in range(self.size):
            print(col, end="")
        print()

        # Print rows
        for row in range(self.size):
            # Print row label
            print(row, end=" ")

            # Print cells
            for col in range(self.size):
                print(self.board[row][col], end="")
            print()
