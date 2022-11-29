import os
import random
import imageio
from TicTacToeImage import TicTacToeImage

imageCount = 1


class TicTacToe:
    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.turn = -1
        self.turnNumber = 1
        self.image = TicTacToeImage()
        # x = -1
        # o = 1

    def getWinner(self):
        sums = self.getSums()

        maxSum = max(sums, key=abs)

        return int(maxSum / 3) if abs(maxSum) == 3 else 0

    def hasSpace(self):
        for row in self.board:
            for pos in row:
                if pos == 0:
                    return True

        return False

    def isOver(self):
        return self.getWinner() != 0 or not self.hasSpace()

    def getSequences(self):
        sequences = []

        # Row
        for i in range(len(self.board)):
            sequences.append(self.board[i])

        # Column
        for i in range(len(self.board[0])):
            col = []
            for row in self.board:
                col.append(row[i])
            sequences.append(col)

        # Diagonals
        sequences.append([self.board[i][i] for i in range(len(self.board))])
        sequences.append([self.board[i][len(self.board) - i - 1] for i in range(len(self.board))])

        return sequences

    def getSums(self):
        return [sum(sequence) for sequence in self.getSequences()]

    def takeTurn(self):
        global imageCount
        initialBoard = [c[:] for c in self.board]
        positions = []

        for r, row in enumerate(self.board):
            for c, position in enumerate(row):
                if position == 0:
                    self.board[r][c] = self.turn
                    positions.append([(r, c), self.evaulatePosition()])
                self.board = [c[:] for c in initialBoard]

        bestPosition = [[(-1, -1), -10000 * self.turn]]

        for position in positions:
            if position[1] * self.turn > bestPosition[0][1] * self.turn:
                bestPosition.clear()
                bestPosition.append(position)
            if position[1] == bestPosition[0][1]:
                bestPosition.append(position)

        position = random.choice(bestPosition)

        self.board[position[0][0]][position[0][1]] = self.turn
        self.image.paste(position[0][0], position[0][1], self.turn)
        self.image.save(name=str(imageCount) + ".png")

        self.turn = -1 * self.turn
        imageCount += 1
        self.turnNumber += 1

    def evaulatePosition(self):
        position = self.getWinner() * 1000

        for s in self.getSums():
            if s == 2 * self.turn:
                position += s * 5
            if s == -2 * self.turn:
                position += s * 100

        return position


def createGame(name="game"):
    name += ".gif"
    TicTacToeImage.clearImages()
    ttt = TicTacToe()
    while not ttt.isOver():
        ttt.takeTurn()
    with imageio.get_writer("games/" + name, mode='I', duration=15.0 / len(os.listdir('images'))) as writer:
        for _, _, files in os.walk("images"):
            for file in files:
                image = imageio.v3.imread("images/" + file)
                writer.append_data(image)


def createImages(imageNum=250):
    TicTacToeImage.clearImages()
    ttt = TicTacToe()
    counter = 0
    while True:
        counter += 1
        if not ttt.isOver():
            ttt.takeTurn()
        else:
            if counter < imageNum:
                ttt = TicTacToe()
            else:
                break
