from pypresence import Presence
import time

from TicTacToe import TicTacToe

ID = "APPLICATION_CLIENT_ID"
RPC = Presence(ID)
RPC.connect()

ttt = TicTacToe()

name = ""
iter = 0
while True:
    iter = (iter + 1) % 274
    RPC.update(large_image=str(iter),
               details="Language: Python",
               state="Updated Every 15 Seconds", # Due to Discord Limitations
               buttons=[{"label": "Github", "url": "https://github.com/22seegerb"}])
    time.sleep(15)