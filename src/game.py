import sys
import random
import pygame
from deck import CardDeck
from player import Player
from menu import Menu
from high_scores import HighScores


class Game:
    """
    Represents the main game logic for a card game.

    Manages game state, player turns, card play, special card effects,
    and interactions with rendering and menus.
    """
    def __init__(self, renderer, restart_callback=None):
        self.deck = CardDeck()
        self.player = Player(self.deck)
        self.ai = Player(self.deck)
        self.current_card = self.deck.draw_first_card()
        self.turn = "Pelaaja"
        self.renderer = renderer
        self.pending_ai_action = False
        self.ai_action_start_time = 0
        self.ai_delay_ms = 2500
        self.selected_card_index = 0
        self.view_start_row = 0
        self.menu = Menu(self.renderer)
        self.restart_callback = restart_callback

        self.hand_len = None
        self.cards_per_row = None
        self.total_rows = None
        self.current_row = None
        self.current_col = None
        self.selected_index = None

    def run(self): # pragma: no cover
        """
        Starts and runs the main game loop.

        Handles game state updates, AI turns, event processing, and rendering calls.
        The loop continues until the game is quit or a game-ending condition is met.
        """
        self.menu.show_main_menu()
        running = True
        while running:
            self.renderer.draw(self, self.selected_card_index)
            now = pygame.time.get_ticks()
            if self.pending_ai_action:
                if now - self.ai_action_start_time >= self.ai_delay_ms:
                    self.pending_ai_action = False
                    self._ai_turn()
                else:
                    pygame.time.wait(50)
                    continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if self.turn == "Pelaaja":
                        self._player_turn(event)

    def _player_turn(self, event):
        self.hand_len = len(self.player.hand)
        if self.hand_len == 0:
            return

        self.cards_per_row = 10
        self.total_rows = (
            self.hand_len + self.cards_per_row - 1) // self.cards_per_row

        self.current_row = self.selected_card_index // self.cards_per_row
        self.current_col = self.selected_card_index % self.cards_per_row

        if event.key in (pygame.K_LEFT, pygame.K_a):
            self.selected_card_index = (
                self.selected_card_index - 1 + self.hand_len) % self.hand_len

        elif event.key in (pygame.K_RIGHT, pygame.K_d):
            self.selected_card_index = (
                self.selected_card_index + 1) % self.hand_len

        elif event.key in (pygame.K_UP, pygame.K_w):
            self._up()

        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self._down()

        elif event.key == pygame.K_RETURN:
            self._enter()

        elif event.key == pygame.K_SPACE:
            self._space()

        self._card_view()

    def _card_view(self): # pragma: no cover
        if self.hand_len > 0:
            selected_row_for_view = self.selected_card_index // self.cards_per_row
            rows_in_view = 3

            if selected_row_for_view < self.view_start_row:
                self.view_start_row = selected_row_for_view
            elif selected_row_for_view >= self.view_start_row + rows_in_view:
                self.view_start_row = selected_row_for_view - rows_in_view + 1

            self.view_start_row = max(0, self.view_start_row)
            if self.total_rows <= rows_in_view:
                self.view_start_row = 0
            else:
                self.view_start_row = min(
                    self.view_start_row, self.total_rows - rows_in_view)
        else:
            self.view_start_row = 0

    def _up(self): # pragma: no cover
        if self.total_rows > 1:
            target_row = self.current_row - 1
            if target_row < 0:
                new_potential_index = (
                    self.total_rows - 1) * self.cards_per_row + self.current_col
                if new_potential_index >= self.hand_len:
                    self.selected_card_index = self.hand_len - 1
                else:
                    self.selected_card_index = new_potential_index
            else:
                new_index = target_row * self.cards_per_row + self.current_col
                self.selected_card_index = new_index

    def _down(self): # pragma: no cover
        if self.total_rows > 1:
            target_row = self.current_row + 1
            if target_row >= self.total_rows:
                new_potential_index = self.current_col
                if (
                    new_potential_index >= self.cards_per_row
                    or new_potential_index >= self.hand_len
                ):
                    self.selected_card_index = 0
                else:
                    self.selected_card_index = new_potential_index
            else:
                new_index = target_row * self.cards_per_row + self.current_col
                if new_index >= self.hand_len:
                    self.selected_card_index = self.hand_len - 1
                else:
                    self.selected_card_index = new_index

    def _enter(self): # pragma: no cover
        if self._play_card(self.player, self.selected_card_index):
            self.selected_card_index = 0
            if len(self.player.hand) == 0:
                self.selected_card_index = 0
            else:
                self.selected_card_index = min(
                    self.selected_card_index, len(self.player.hand) - 1)
                self.selected_card_index = max(self.selected_card_index, 0)

    def _space(self): # pragma: no cover
        if not self.player.draw_card(self.deck):
            self.check_game_over(draw=True)
            return
        if self.selected_card_index >= len(self.player.hand):
            self.selected_card_index = len(self.player.hand) - 1
        self.turn = "Tietokone"
        self.pending_ai_action = True
        self.ai_action_start_time = pygame.time.get_ticks()

    def _ai_turn(self):
        if self._play_card(self.ai):
            return
        if not self.ai.draw_card(self.deck):
            self.check_game_over(draw=True)
            return
        self.turn = "Pelaaja"

    def _play_card(self, player, index=None):
        card = None
        if index is not None:
            card = player.play_card(
                index, self.current_card, self.is_valid_play)
        else:
            for i, c in enumerate(player.hand):
                if self.is_valid_play(c, self.current_card):
                    card = player.hand.pop(i)
                    break

        if card:
            self.deck.discard_pile.append(self.current_card)
            self.current_card = card
            player.last_action = f", viimeksi pelasi kortin {card[0]} {card[1]}"
            if self.check_game_over():
                return True
            self._special_card_effects(card, is_human=player == self.player)
            return True
        return False

    def _special_card_effects(self, card, is_human):
        player = self.player if is_human else self.ai
        opponent = self.ai if is_human else self.player
        extra_turn = False

        if card[0] == "villi":
            if is_human:
                self._ask_for_color_choice()
            else:
                self._choose_random_color()
            if card[1] == "nosta 4":
                self._draw_cards(opponent, 4, ", viimeksi nosti 4 korttia")
                extra_turn = True
            else:
                player.last_action = ", viimeksi pelasi kortin villi ja vaihtoi väriä"
        elif card[1] == "nosta 2":
            self._draw_cards(opponent, 2, ", viimeksi nosti 2 korttia")
            extra_turn = True
        elif card[1] in ["ohita", "suunnanvaihto"]:
            extra_turn = True

        self._switch_turn(is_human, extra_turn)

    def _draw_cards(self, player, amount, message):
        for _ in range(amount):
            player.draw_card(self.deck)
        player.last_action = message

    def _switch_turn(self, is_human, extra_turn):
        if extra_turn:
            current = self.player if is_human else self.ai
            current.last_action += ", sai toisen vuoron"
            if not is_human:
                self.pending_ai_action = True
                self.ai_action_start_time = pygame.time.get_ticks()
        else:
            self.turn = "Tietokone" if is_human else "Pelaaja"
            self.pending_ai_action = is_human
            if is_human:
                self.ai_action_start_time = pygame.time.get_ticks()

    def _ask_for_color_choice(self):
        self.renderer.draw_color_choice()
        color = self._get_color_choice()
        if color:
            self.current_card = (color, self.current_card[1])

    def _get_color_choice(self):
        colors = ["punainen", "vihreä", "sininen", "keltainen"]
        self.selected_index = 0
        self.renderer.draw_color_choice(self.selected_index)

        while True:
            color_choice = self._color_choice_key(colors)
            if color_choice:
                return color_choice
            self.renderer.draw_color_choice(self.selected_index)

    def _color_choice_key(self, colors): # pragma: no cover
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    self.selected_index = (
                        self.selected_index - 1) % len(colors)
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    self.selected_index = (
                        self.selected_index + 1) % len(colors)
                elif event.key == pygame.K_RETURN:
                    return colors[self.selected_index]
        return False

    def _choose_random_color(self):
        colors = ["punainen", "vihreä", "sininen", "keltainen"]
        self.current_card = (random.choice(colors), self.current_card[1])

    def check_game_over(self, draw=False):
        if draw:
            self.renderer.draw_end_screen("Peli päättyi tasapeliin :/")
            self._handle_end_screen_input()
            return True

        if len(self.player.hand) == 0:
            score = self._calculate_score(self.ai.hand)
            self.renderer.draw_end_screen(
                f"Voitit pelin :) Sait {score} pistettä!")
            self._save_score("Pelaaja", score)
            self._handle_end_screen_input()
            return True

        if len(self.ai.hand) == 0:
            score = self._calculate_score(self.player.hand)
            self.renderer.draw_end_screen(
                f"Hävisit pelin :( Tietokone sai {score} pistettä.")
            self._handle_end_screen_input()
            return True
        return False

    def _save_score(self, name, score):
        repository = HighScores()
        repository.add_score(name, score)

    def _handle_end_screen_input(self): # pragma: no cover
        while True:
            for event in pygame.event.get():
                self._handle_end_event(event)

    def _handle_end_event(self, event): # pragma: no cover
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            self._handle_keydown(event.key)

    def _handle_keydown(self, key): # pragma: no cover
        if key == pygame.K_y and self.restart_callback:
            self.restart_callback()
        elif key == pygame.K_n:
            pygame.quit()
            sys.exit()

    def _start_ai_turn(self):
        self.turn = "Tietokone"
        self.pending_ai_action = True
        self.ai_action_start_time = pygame.time.get_ticks()

    def _calculate_score(self, hand):
        score = 0
        for color, value in hand:
            if value.isdigit():
                score += int(value)
            elif value in ["ohita", "suunnanvaihto", "nosta 2"]:
                score += 20
            elif color == "villi":
                score += 50
        return score

    @staticmethod
    def is_valid_play(card, current_card):
        """
        Checks if a given card can be played on top of the current card.

        Args:
            card (tuple): The card to check (color, value).
            current_card (tuple): The card currently on top of the discard pile (color, value).

        Returns:
            bool: True if the card can be played, False otherwise.
        """
        return (
            card[0] == "villi" or
            card[0] == current_card[0] or
            card[1] == current_card[1]
        )
