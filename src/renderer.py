import sys
import pygame


class GameRenderer:
    """Handles the rendering of the game on the screen."""

    def __init__(self, width=1400, height=900, restart_callback=None):
        """
        Initializes the game renderer with screen dimensions and an optional restart callback.

        Args:
            width: The width of the game window.
            height: The height of the game window.
            restart_callback: A function to call when the game is restarted.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Korttipeli")
        self.font = pygame.font.Font(None, 36)
        self.colors = {
            "punainen": (200, 0, 0),
            "vihreä": (0, 200, 0),
            "sininen": (0, 0, 200),
            "keltainen": (200, 200, 0)
        }
        self.restart_callback = restart_callback

    def draw(self, game):
        """
        Draws the current state of the game on the screen.

        Args:
            game: The game object containing the current state.
        """
        self.screen.fill((255, 255, 255))
        self._draw_text(f"Vuoro: {game.turn}", 50, 20)
        ai_text = f"Tietokone: {len(game.ai.hand)} korttia{game.ai.last_action}"
        self._draw_text(ai_text, 50, 60)

        self._draw_text("Poistopakan ylin kortti:", 50, 100)
        card_text = f"{game.current_card[0]} {game.current_card[1]}"
        card_color = self.colors.get(game.current_card[0], (0, 0, 0))
        self._draw_text(card_text, 50, 130, card_color)
        player_text = f"Pelaaja: {len(game.player.hand)} korttia{game.player.last_action}"
        self._draw_text(player_text, 50, 190)

        self._draw_text("Pelaajan kortit:", 50, 250)
        for i, card in enumerate(game.player.hand):
            card_label = f"[{chr(97 + i)}] {card[0]} {card[1]}"
            x_pos = 50 + (i % 4) * 330
            y_pos = 280 + (i // 4) * 50
            color = self.colors.get(card[0], (0, 0, 0))
            self._draw_text(card_label, x_pos, y_pos, color)

        pygame.display.flip()

    def _draw_text(self, text, x, y, color=(0, 0, 0)):
        """
        Draws text on the screen.

        Args:
            text: The text to draw.
            x: The x-coordinate for the text.
            y: The y-coordinate for the text.
            color: The color of the text (default is black).
        """
        self.screen.blit(self.font.render(text, True, color), (x, y))

    def draw_color_choice(self):
        """Draws the color choice prompt on the screen."""
        self.screen.fill((255, 255, 255))
        self._draw_text(
            "Valitse väri: [R] punainen, [G] vihreä, [B] sininen, [Y] keltainen", 50, 300)
        pygame.display.flip()

    def draw_end_screen(self, message):
        self.screen.fill((255, 255, 255))
        self._draw_text(message, 400, 300, (0, 0, 0))
        self._draw_text("Pelaa uudestaan? (Kyllä = Y, Ei = N)",
                        300, 360, (0, 0, 0))
        pygame.display.flip()
        self._handle_end_screen_input()

    def _handle_end_screen_input(self):
        while True:
            for event in pygame.event.get():
                self._handle_event(event)

    def _handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            self._handle_keydown(event.key)

    def _handle_keydown(self, key):
        if key == pygame.K_y and self.restart_callback:
            self.restart_callback()
        elif key == pygame.K_n:
            pygame.quit()
            sys.exit()
