from PIL import Image
import os

class TicTacToeImage:
    def __init__(self):
        self.o = "templates/o.png"
        self.x = "templates/x.png"
        self.board = "templates/TicTacToe.png"

        self.o = Image.open(self.o)
        self.x = Image.open(self.x)
        self.board = Image.open(self.board)

        self.o = self.o.convert("RGBA")
        self.x = self.x.convert("RGBA")
        self.board = self.board.convert("RGBA")

    def save(self, name="board.png"):
        self.board.save("images/" + name, format="png")

    def paste(self, r, c, turn):
        icon = self.x if turn == -1 else self.o
        self.board.paste(icon, (72 + r * 144, 79 + c * 144), icon)

    @staticmethod
    def clearImages():
        list(map(os.unlink, (os.path.join("images", f) for f in os.listdir("images"))))
