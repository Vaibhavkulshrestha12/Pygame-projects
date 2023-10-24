import tkinter as tk
from tkinter import messagebox
import random


class Minesweeper:

    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper")

        self.rows = 10
        self.columns = 10
        self.mines = 1

        self.field = []
        self.mine_positions = []

        self.generate_mines()

        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                if (i, j) in self.mine_positions:
                    button = self.create_button(self.root, i, j, "*")
                else:
                    count = self.adjacent_mines(i, j)
                    button = self.create_button(self.root, i, j, count)
                row.append(button)
            self.field.append(row)

    def generate_mines(self):
        count = 0
        while count < self.mines:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.columns - 1)
            if (x, y) not in self.mine_positions:
                self.mine_positions.append((x, y))
                count += 1

    def create_button(self, parent, x, y, value):
        if value == "*":
            btn = tk.Button(parent, text="", width=3, command=lambda x=x, y=y: self.on_click(x, y))
        else:
            btn = tk.Button(parent, text="", width=3, command=lambda x=x, y=y: self.on_click(x, y))
        btn.grid(row=x, column=y)
        return (btn, value)

    def adjacent_mines(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (x + i, y + j) in self.mine_positions:
                    count += 1
        return count

    def on_click(self, x, y):
        if self.field[x][y][1] == "*":
            for mine in self.mine_positions:
                self.field[mine[0]][mine[1]][0].config(text="*", fg="red")
            messagebox.showinfo("Minesweeper", "Game Over!")
            self.root.destroy()
            return
        else:
            self.field[x][y][0].config(text=self.field[x][y][1])
            self.check_win()

    def check_win(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.field[i][j][0]["text"] == "" and self.field[i][j][1] != "*":
                    return
        messagebox.showinfo("Minesweeper", "You Won!")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()
