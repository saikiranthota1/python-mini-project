from tkinter import Label, Frame, CENTER
import Logics
import constants as c

class Game(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)
        self.commands = {
            c.KEY_UP: Logics.move_up,        # Up arrow key for moving up
            c.KEY_LEFT: Logics.move_left,    # Left arrow key for moving left
            c.KEY_DOWN: Logics.move_down,    # Down arrow key for moving down (bottom)
            c.KEY_RIGHT: Logics.move_right,  # Right arrow key for moving right (top)
        }
        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                           width=c.SIZE, height=c.SIZE)
        background.grid()

        self.grid_cells = []

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background,
                             bg=c.BACKGROUND_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN,
                             height=c.SIZE / c.GRID_LEN)
                cell.grid(row=i, column=j, padx=c.GRID_PADDING, pady=c.GRID_PADDING)

                label = Label(master=cell,
                              text="",
                              bg=c.BACKGROUND_CELL_EMPTY,
                              justify=CENTER,
                              font=c.FONT,
                              width=5,
                              height=2)
                label.grid()
                grid_row.append(label)
            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = Logics.start_game()
        Logics.add_new_2(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=c.BACKGROUND_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(
                        text=str(new_number),
                        bg=c.background_color_dict.get(new_number, c.BACKGROUND_CELL_EMPTY),
                        fg=c.cell_color_dict.get(new_number, c.BACKGROUND_COLOR_GAME)
                    )
            self.update_idletasks()

    def key_down(self, event):
        key = event.char
        if key in self.commands:
            self.matrix, changed = self.commands[key](self.matrix)
            if changed:
                Logics.add_new_2(self.matrix)
                self.update_grid_cells()
                
                # Check for game states
                current_state = Logics.get_current_state(self.matrix)
                if current_state == 'Won':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="WON", bg=c.BACKGROUND_CELL_EMPTY)
                    self.master.after(1000, self.disable_input)  # Disable input after 1 second
                elif current_state == 'Lost':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lost", bg=c.BACKGROUND_CELL_EMPTY)
                    self.master.after(1000, self.disable_input)  # Disable input after 1 second

    def disable_input(self):
        """Disables the key input after the game ends"""
        self.master.unbind("<Key>")

game_grid = Game()
