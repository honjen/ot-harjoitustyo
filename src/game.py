from deck import CardDeck
from player import Player

import pygame

class Game:
    def __init__(self, renderer):
        self.deck = CardDeck()
        self.player = Player(self.deck)
        self.ai = Player(self.deck)
        self.current_card = self.deck.draw_card()
        self.turn = "Pelaaja"
        self.renderer = renderer
    
    def run(self):
        running = True
        while running:
            self.renderer.draw(self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and self.turn == "Pelaaja":
                    self.handle_player_turn(event)
        pygame.quit()
    
    def handle_player_turn(self, event):
        if event.key >= pygame.K_a and event.key <= pygame.K_z:
            index = event.key - pygame.K_a
            card = self.player.play_card(index, self.current_card, self.is_valid_play)
            if card:
                self.current_card = card
                self.player.last_action = f", viimeksi pelasi kortin {card[0]} {card[1]}"
                self.turn = "Tietokone"
                self.ai_turn()
        elif event.key == pygame.K_RETURN:
            self.player.draw_card(self.deck)
            self.turn = "Tietokone"
            self.ai_turn()
    
    def ai_turn(self):
        for i, card in enumerate(self.ai.hand):
            if self.is_valid_play(card, self.current_card):
                self.current_card = self.ai.hand.pop(i)
                self.ai.last_action = f", viimeksi pelasi kortin {card[0]} {card[1]}"
                self.turn = "Pelaaja"
                return
        self.ai.draw_card(self.deck)
        self.turn = "Pelaaja"
    
    @staticmethod
    def is_valid_play(card, current_card):
        return card[0] == current_card[0] or card[1] == current_card[1]
