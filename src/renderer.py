import pygame

class GameRenderer:
    def __init__(self, width=1025, height=800):
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
    
    def draw(self, game):
        self.screen.fill((255, 255, 255))
        self._draw_text(f"Vuoro: {game.turn}", 50, 20)
        self._draw_text(f"Tietokone: {len(game.ai.hand)} korttia{game.ai.last_action}", 50, 60)
        self._draw_text("Poistopakan ylin kortti:", 50, 100)
        self._draw_text(f"{game.current_card[0]} {game.current_card[1]}", 50, 130, self.colors.get(game.current_card[0], (0, 0, 0)))
        self._draw_text(f"Pelaaja: {len(game.player.hand)} korttia{game.player.last_action}", 50, 190)
        self._draw_text("Pelaajan kortit:", 50, 250)
        for i, card in enumerate(game.player.hand):
            self._draw_text(f"[{chr(97 + i)}] {card[0]} {card[1]}", 50 + (i % 4) * 260, 280 + (i // 4) * 50, self.colors.get(card[0], (0, 0, 0)))
        pygame.display.flip()
    
    def _draw_text(self, text, x, y, color=(0, 0, 0)):
        self.screen.blit(self.font.render(text, True, color), (x, y))

