import os
import sys
import yaml
import pygame
from high_scores import HighScores


class Menu:
    """
    Manages the main menu for the game.

    Handles displaying menu options, navigating through them, and
    triggering actions based on user selection (starting game, showing ranking,
    showing instructions, exiting).
    """
    def __init__(self, renderer):
        self.renderer = renderer
        self.options = ["Aloita peli", "Ranking", "Ohjeet", "Poistu"]
        self.selected = 0

    def show_main_menu(self):
        """
        Displays the main menu and handles user interaction.

        Renders the menu options and processes keyboard events for selection
        until an action (like starting the game or exiting) is chosen.
        """

        font = pygame.font.Font(None, 72)

        while True:
            self.renderer.screen.fill((255, 255, 255))

            for i, option in enumerate(self.options):
                color = (0, 0, 0)
                if i == self.selected:
                    color = (0, 128, 255)
                text_surf = font.render(option, True, color)
                text_rect = text_surf.get_rect(
                    center=(self.renderer.screen.get_width() // 2, 200 + i * 100))
                self.renderer.screen.blit(text_surf, text_rect)

            pygame.display.flip()
            if not self._handle_events():
                return

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_w]:
                    self.selected = (self.selected - 1) % len(self.options)
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    self.selected = (self.selected + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    return self._handle_selection()
        return True

    def _handle_selection(self):
        if self.selected == 0:
            return False
        if self.selected == 1:
            self._show_ranking()
        elif self.selected == 2:
            self._show_instructions()
        elif self.selected == 3:
            pygame.quit()
            sys.exit()
        return True

    def _show_instructions(self):
        screen = self.renderer.screen
        font = pygame.font.Font(None, 36)

        screen.fill((255, 255, 255))
        lines = self._read_instructions()

        y = 40
        for line in lines:
            text = font.render(line, True, (0, 0, 0))
            screen.blit(text, (50, y))
            y += font.get_linesize() + 2

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    waiting = False

    def _read_instructions(self):
        base_directory = os.path.dirname(__file__)
        filepath = os.path.join(base_directory, "data", "instructions.yaml")
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                lines = data.get("instructions", [])
        except (yaml.YAMLError, OSError) as e:
            lines = ["Virhe ohjeiden lataamisessa:", str(e)]
        return lines

    def _show_ranking(self):
        repository = HighScores()
        data = repository.get_top_scores()
        if len(data) < 1:
            message = ["Ei rankingeja vielä..."]
        else:
            message = [f"{i + 1}. {name} - {score}" for i,
                       (name, score) in enumerate(data)]
        self._show_simple_screen(message)

    def _show_simple_screen(self, message):
        screen = self.renderer.screen
        while True:
            screen.fill((255, 255, 255))
            font = pygame.font.Font(None, 48)
            y = 40
            for line in message:
                text = font.render(line, True, (0, 0, 0))
                screen.blit(text, (50, y))
                y += font.get_linesize() + 2

            back_text = font.render(
                "Paina ESC palataksesi", True, (128, 128, 128))
            back_rect = back_text.get_rect(
                center=(self.renderer.screen.get_width() // 2, 400))
            screen.blit(back_text, back_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
