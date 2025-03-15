import pygame
from entities.bullet import Bullet, ExplosiveBullet

class Player:
    def __init__(self, x, y,sprite_path):
        self.x = x
        self.y = y
        self.speed = 4
        self.sprite = pygame.image.load(sprite_path)
        self.cooldown = 0
        self.cooldown_time = 10
    
    def shoot(self):
        if self.cooldown <= 0:
            self.cooldown = self.cooldown_time
            return Bullet(self.x + 20, self.y)
        return None
    
    def move(self, keys, width):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < width - 50:
            self.x += self.speed
    
    def update_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1
    
    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

class FastPlayer(Player):
    def __init__(self, x, y, sprite_path):
        super().__init__(x, y, sprite_path)
        self.speed = 6

class ExplosivePlayer(Player):
    def __init__(self, x, y, sprite_path):
        super().__init__(x, y, sprite_path)
        self.speed = 4
        self.cooldown_time = 30
    
    def shoot(self):
        if self.cooldown <= 0:
            self.cooldown = self.cooldown_time
            return ExplosiveBullet(self.x + 20, self.y)
        return None