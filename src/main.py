from game import Game
from renderer import GameRenderer


def main():
    """Initializes and runs the game."""
    renderer = GameRenderer()
    game = Game(renderer, restart_callback=main)
    game.run()


if __name__ == "__main__":
    main()
