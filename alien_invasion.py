import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Klasa przeznaczona do zarządzania zasobami i sposobem działania gry'''

    def __init__(self):
        '''Inicjalizacja gry i jej zasobów'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Inwazja obcych")
        self.ship = Ship(self)

    def run_game(self):
        '''Rozpoczęcie pętli głównej gry.'''
        while True:
            # Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                pygame.display.flip()
                self.clock.tick(60)
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
