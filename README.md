# TicTacToeDiscordPresence
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

TicTacToe Generator for Discord Rich Presence

File Breakdown:
- [Main File](main.py)
  - Controls RichPresence
  - Must be ran on Computer Logged Into Discord
- [TicTacToe Game](TicTacToe.py)
  - Plays TicTacToe. 
  - Uses a simple Position Evaluating algorithm with low depth and only evaluates 2 / 3 in a row in order to increase randomization and prevent all games from being the same.
- [TicTacToeImage Create](TicTacToeImage.py)
  - Generates the images of TicTacToe to be displayed as the Rich Presence Image based on a few template images.

The Images are captured from TicTacToe.py, and then uploaded to the Discord Application. The main.py then creates the Rich Presence, and iterates through the images to create the illusion that it is "playing" TicTacToe. I attempted to use request.py to programically upload and delete images from Discord to create new games, but frequent issues with Discord's API resulted in me giving up on that, and simply using the 300 open image slots to upload ~50 games of TicTacToe to rotate between.
