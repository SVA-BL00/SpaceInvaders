import pygame

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 7
        self.color = (255,0,0)
        self.width = 5
        self.height = 20
    
    def move(self):
        self.y -= self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class ExplosiveBullet(Bullet):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 5
        self.radius = 100
        self.color = (255, 165, 0)
    
    def explode(self, enemies, score):
        for enemy in enemies[:]:
            distance = ((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2) ** 0.5
            if distance <= self.radius:
                enemies.remove(enemy)
                score += 100
        return score