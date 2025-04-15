from game import Game
from renderer import GameRenderer


def main():
    renderer = GameRenderer(restart_callback=main)
    game = Game(renderer)
    game.run()


if __name__ == "__main__":
    main()
