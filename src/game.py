import sys
import random
import pygame
from deck import CardDeck
from player import Player


class Game:
    """Represents the game logic and state."""

    def __init__(self, renderer):
        """
        Initializes the game with a deck, players (human and AI), and renderer.

        Args:
            renderer: The game renderer object.
        """
        self.deck = CardDeck()
        self.player = Player(self.deck)
        self.ai = Player(self.deck)
        self.current_card = self.deck.draw_first_card()
        self.turn = "Pelaaja"
        self.renderer = renderer
        self.pending_ai_action = False
        self.ai_action_start_time = 0
        self.ai_delay_ms = 3000

    def run(self): # pragma: no cover
        """Runs the main game loop."""
        running = True
        while running:
            self.renderer.draw(self)
            now = pygame.time.get_ticks()
            if self.pending_ai_action:
                if now - self.ai_action_start_time >= self.ai_delay_ms:
                    self.pending_ai_action = False
                    self.ai_turn()
                else:
                    pygame.time.wait(50)
                    continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and self.turn == "Pelaaja":
                    self.handle_player_turn(event)

    def handle_player_turn(self, event): # pragma: no cover
        """
        Handles the player's turn based on keyboard input.

        Args:
            event: The Pygame event object.
        """
        if event.key >= pygame.K_a and event.key <= pygame.K_z:
            index = event.key - pygame.K_a
            card = self.player.play_card(
                index, self.current_card, self.is_valid_play)
            if card:
                self.current_card = card
                self.player.last_action = f", viimeksi pelasi {card[0]} {card[1]}"
                self.deck.discard_pile.append(self.current_card)
                if self.check_game_over():
                    return
                self.player_special_card_check(card)

        elif event.key == pygame.K_RETURN:
            if not self.player.draw_card(self.deck):
                self.renderer.draw_end_screen("Peli päättyi tasapeliin!")
                return
            self.turn = "Tietokone"
            self.pending_ai_action = True
            self.ai_action_start_time = pygame.time.get_ticks()

    def player_special_card_check(self, card):
        if card[0] == "villi":
            self._ask_for_color_choice()
            if card[1] == "nosta 4":
                for _ in range(4):
                    self.ai.draw_card(self.deck)
                self.player.last_action = ", viimeksi pelasi villi nosta 4"
                self.player.last_action += ", sai toisen vuoron"
                self.ai.last_action = ", viimeksi nosti 4 korttia"
                return
            self.player.last_action = ", viimeksi pelasi villi ja vaihtoi väriä"
            self.turn = "Tietokone"
            self.pending_ai_action = True
            self.ai_action_start_time = pygame.time.get_ticks()
            return
        if card[1] in ["ohita", "suunnanvaihto"]:
            self.player.last_action += ", sai toisen vuoron"
        elif card[1] == "nosta 2":
            self.ai.draw_card(self.deck)
            self.ai.draw_card(self.deck)
            self.player.last_action += ", sai toisen vuoron"
            self.ai.last_action = ", viimeksi nosti 2 korttia"
        else:
            self.turn = "Tietokone"
            self.pending_ai_action = True
            self.ai_action_start_time = pygame.time.get_ticks()

    def ai_turn(self):
        """Handles the AI's turn logic."""
        for i, card in enumerate(self.ai.hand):
            if self.is_valid_play(card, self.current_card):
                self.deck.discard_pile.append(self.current_card)
                self.current_card = self.ai.hand.pop(i)
                self.ai.last_action = f", viimeksi pelasi {card[0]} {card[1]}"
                if self.check_game_over():
                    return
                if card[0] == "villi":
                    self._choose_random_color()
                    if card[1] == "nosta 4":
                        for _ in range(4):
                            self.player.draw_card(self.deck)
                        self.ai.last_action = ", viimeksi pelasi villi nosta 4 ja sai toisen vuoron"
                        self.player.last_action = ", viimeksi nosti 4 korttia"
                    else:
                        self.ai.last_action = ", viimeksi pelasi villi ja vaihtoi väriä"
                        self.turn = "Pelaaja"
                        return
                elif card[1] in ["ohita", "suunnanvaihto"]:
                    self.ai.last_action += ", sai toisen vuoron"
                elif card[1] == "nosta 2":
                    self.player.draw_card(self.deck)
                    self.player.draw_card(self.deck)
                    self.ai.last_action += ", sai toisen vuoron"
                    self.player.last_action = ", viimeksi nosti 2 korttia"
                else:
                    self.turn = "Pelaaja"
                    return
        self.ai.draw_card(self.deck)
        if not self.ai.draw_card(self.deck):
            self.renderer.draw_end_screen("Peli päättyi tasapeliin!")
            return
        self.turn = "Pelaaja"

    def _ask_for_color_choice(self): # pragma: no cover
        """Asks the player to choose a color for villi card."""
        self.renderer.draw_color_choice()
        waiting = True
        while waiting:
            if not self._handle_events():
                waiting = False

    def _handle_events(self): # pragma: no cover
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.current_card = ("punainen", self.current_card[1])
                elif event.key == pygame.K_g:
                    self.current_card = ("vihreä", self.current_card[1])
                elif event.key == pygame.K_b:
                    self.current_card = ("sininen", self.current_card[1])
                elif event.key == pygame.K_y:
                    self.current_card = ("keltainen", self.current_card[1])
                return False
        return True

    def _choose_random_color(self):
        """Randomly chooses a color for the AI's wild card play."""
        colors = ["punainen", "vihreä", "sininen", "keltainen"]
        self.current_card = (random.choice(colors), self.current_card[1])

    def check_game_over(self):
        """Checks if the game is over and displays the end screen."""
        if len(self.player.hand) == 0:
            self.renderer.draw_end_screen("Voitit pelin :)")
            return True
        if len(self.ai.hand) == 0:
            self.renderer.draw_end_screen("Hävisit pelin :(")
            return True
        return False

    @staticmethod
    def is_valid_play(card, current_card):
        """
        Checks if a card can be played on the current card.

        Args:
            card: The card to be played.
            current_card: The current card on the discard pile.

        Returns:
            True if the play is valid, False otherwise.
        """
        return (
            card[0] == "villi" or
            card[0] == current_card[0] or
            card[1] == current_card[1]
        )
