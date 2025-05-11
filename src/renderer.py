import pygame


class GameRenderer:
    """Handles the rendering of the game on the screen."""

    def __init__(self, width=1200, height=900):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Korttipeli")
        self.font = pygame.font.Font(None, 36)
        self.colors = {
            "punainen": (200, 0, 0),
            "vihreä": (0, 200, 0),
            "sininen": (0, 0, 200),
            "keltainen": (200, 200, 0),
            "villi": (100, 100, 100)
        }

    def draw(self, game, selected_index=0):
        """
        Draws the current state of the game onto the screen.

        Includes drawing turn information, AI info, the discard pile,
        player info, and the player's hand.

        Args:
            game: The current Game object containing game state.
            selected_index (int): The index of the card currently selected
                                  in the player's hand (default is 0).
        """
        self.screen.fill((255, 255, 255))
        self._draw_turn_info(game)
        self._draw_ai_info(game)
        self._draw_discard_pile(game)
        self._draw_player_info(game)
        self._draw_player_hand(game, selected_index)
        self.draw_scroll_arrows(game, cards_per_row=10, rows_in_view=3)
        pygame.display.flip()

    def _draw_turn_info(self, game):
        turn_text = "Vuoro: "
        player_text = game.turn
        turn_color = (0, 0, 255) if game.turn == "Pelaaja" else (255, 0, 0)
        self._draw_text(turn_text, 50, 20, color=(0, 0, 0))
        self._draw_text(player_text, 135, 20, color=turn_color)

    def _draw_ai_info(self, game):
        ai_hand = len(game.ai.hand)
        suffix = " kortti" if ai_hand == 1 else " korttia"
        ai_text = f"Tietokone: {ai_hand}{suffix}{game.ai.last_action}"
        self._draw_text(ai_text, 50, 60)

    def _draw_discard_pile(self, game):
        self._draw_text("Poistopakan ylin kortti:", 50, 100)
        card_rect = pygame.Rect(50, 130, 100, 150)
        render_params = {"rect": card_rect, "is_selected": False}
        self.draw_card(game.current_card, render_params)

    def _draw_player_info(self, game):
        player_hand = len(game.player.hand)
        suffix = " kortti" if player_hand == 1 else " korttia"
        player_text = f"Pelaaja: {player_hand}{suffix}{game.player.last_action}"
        self._draw_text(player_text, 50, 300)
        self._draw_text("Pelaajan kortit:", 50, 340)

    def _draw_player_hand(self, game, selected_index):
        cards_per_row = 10
        rows_in_view = 3
        max_cards_in_view = cards_per_row * rows_in_view

        hand = game.player.hand
        hand_length = len(hand)
        view_start_row = getattr(game, "view_start_row", 0)
        start_index = view_start_row * cards_per_row if hand_length > max_cards_in_view else 0

        cards_to_draw = hand[start_index:start_index + max_cards_in_view]

        for i, card in enumerate(cards_to_draw):
            card_rect = pygame.Rect(
                50 + (i % cards_per_row) * 110,
                370 + (i // cards_per_row) * 160,
                100,
                150
            )
            render_params = {
                "rect": card_rect,
                "is_selected": start_index + i == selected_index
            }
            self.draw_card(card, render_params)

    def draw_card(self, card, render_params):
        """
        Draws a single card on the screen using render parameters.

        Args:
            card (tuple): The card to draw (color, value).
            render_params (dict): A dictionary containing rendering parameters,
                                  expected to have 'rect' (pygame.Rect) for position
                                  and size, and 'is_selected' (bool) to indicate
                                  if the card is currently selected.
        """
        rect = render_params["rect"]
        is_selected = render_params["is_selected"]

        color_name, _ = card
        fill_color = self.colors.get(color_name, (100, 100, 100))
        text_color = (
            255, 255, 255) if color_name != "keltainen" else (0, 0, 0)
        border_color = (255, 0, 0) if is_selected else (0, 0, 0)

        self._draw_card_body(rect, fill_color, border_color, is_selected)

        lines = self._get_card_text_lines(card)

        self._render_card_text_lines(rect, lines, text_color)

    def _draw_card_body(self, rect, fill_color, border_color, is_selected):
        """Draws the physical shape and border of the card, including shadow if selected."""
        if is_selected:
            shadow_offset = 6
            shadow_rect = pygame.Rect(
                rect.x + shadow_offset, rect.y + shadow_offset, rect.width, rect.height)
            pygame.draw.rect(self.screen, (50, 50, 50),
                             shadow_rect, border_radius=12)

        pygame.draw.rect(self.screen, fill_color, rect, border_radius=12)
        pygame.draw.rect(self.screen, border_color, rect, 4, border_radius=12)

    def _get_card_text_lines(self, card):
        """Determines the text lines to be displayed on the card based on its type."""
        color_name, value = card
        text = value if color_name != "villi" else (
            value if value else "villi")

        if text.lower() == "suunnanvaihto":
            return ["suunnan", "vaihto"]
        if color_name == "villi" and text == "nosta 4":
            return ["villi", "nosta 4"]
        return [text]

    def _render_card_text_lines(self, rect, lines, text_color):
        """Renders and blits the given text lines onto the card rectangle."""
        font_size = 24 if len(lines) > 1 else 36
        font = pygame.font.Font(None, font_size)

        total_text_height = sum(font.render(
            line, True, text_color).get_height() for line in lines)
        start_y = rect.centery - total_text_height // 2

        for i, line in enumerate(lines):
            text_surface = font.render(line, True, text_color)
            line_height = text_surface.get_height()
            text_rect = text_surface.get_rect(center=(
                rect.centerx,
                start_y + i * line_height + line_height // 2
            ))
            self.screen.blit(text_surface, text_rect)

    def _draw_text(self, text, x, y, color=(0, 0, 0)):
        self.screen.blit(self.font.render(text, True, color), (x, y))

    def draw_color_choice(self, selected_index=0):
        """
        Draws the color choice screen for a wild card.

        Displays selectable color options for the player to choose from.

        Args:
            selected_index (int): The index of the color card currently selected (default is 0).
        """
        self.screen.fill((255, 255, 255))
        self._draw_text("Valitse väri:", 50, 100)

        colors = ["punainen", "vihreä", "sininen", "keltainen"]
        for i, color in enumerate(colors):
            x = 100 + i * 150
            y = 200
            card = (color, "")
            is_selected = i == selected_index
            card_rect = pygame.Rect(x, y, 100, 150)
            render_params = {"rect": card_rect, "is_selected": is_selected}
            self.draw_card(card, render_params)

        pygame.display.flip()

    def draw_end_screen(self, message):
        """
        Draws the end-game screen with a message and restart options.

        Args:
            message (str): The message to display on the end screen (e.g., win/loss message).
        """
        self.screen.fill((255, 255, 255))

        text_surface = self.font.render(message, True, (0, 0, 0))
        text_rect = text_surface.get_rect(
            center=(self.screen.get_width() // 2, 300))
        self.screen.blit(text_surface, text_rect)

        restart_message = "Palaa alkuvalikkoon? (Kyllä = Y, Ei = N)"
        restart_surface = self.font.render(restart_message, True, (0, 0, 0))
        restart_rect = restart_surface.get_rect(
            center=(self.screen.get_width() // 2, 360))
        self.screen.blit(restart_surface, restart_rect)

        pygame.display.flip()

    def draw_scroll_arrows(self, game, cards_per_row, rows_in_view):
        """
        Draws up and down arrows for scrolling the player's hand view if needed.

        Args:
            game: The current Game object containing game state (specifically player's hand).
            cards_per_row (int): The number of cards displayed per row in the hand view.
            rows_in_view (int): The number of rows visible in the hand view.
        """
        total_rows = (len(game.player.hand) +
                      cards_per_row - 1) // cards_per_row
        if total_rows > rows_in_view:
            if game.view_start_row > 0:
                self._draw_triangle(25, 500, direction="up")
            if game.view_start_row + rows_in_view < total_rows:
                self._draw_triangle(25, 700, direction="down")

    def _draw_triangle(self, x, y, direction="up"):
        triangle_size = 30
        color = (0, 0, 0)

        if direction == "up":
            points = [
                (x, y - triangle_size),
                (x - triangle_size // 2, y),
                (x + triangle_size // 2, y),
            ]
        else:
            points = [
                (x, y + triangle_size),
                (x - triangle_size // 2, y),
                (x + triangle_size // 2, y),
            ]

        pygame.draw.polygon(self.screen, color, points)
