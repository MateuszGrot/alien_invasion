import  sys
import pygame

class AlienInvasion:
    '''Klasa przeznaczona do zarządzania zasobami i sposobem działania gry'''

    def __init__(self):
        '''Inicjalizacja gry i jej zasobów'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Inwazja obcych")

    def run_game(self):
        '''Rozpoczęcie pętli głównej gry.'''
        while True:
            #Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                pygame.display.flip()
                self.clock.tick(60)
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()