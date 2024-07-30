import pygame

class Ship:

    def __init__(self, ai_game):
        '''Inicjalizacja statku kosmicznego i jego położenie początkowe.'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Każdy nowy statek kosmiczny pojawia się na dole ekranu.
        self.rect.midbottom = self.screen_rect.midbottom

        #Opcje wskazujące na poruszanie się statku.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.x +=1
        if self.moving_left:
            self.rect.x -= 1
    def blitme(self):
        '''Wyświetlanie statku kosmicznego w jego aktualnym położeniu.'''
        self.screen.blit(self.image, self.rect)
