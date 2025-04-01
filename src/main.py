from game import Game
from renderer import GameRenderer

if __name__ == "__main__":
    renderer = GameRenderer()
    game = Game(renderer)
    game.run()
