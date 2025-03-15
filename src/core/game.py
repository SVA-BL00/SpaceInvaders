import pygame
import random
from entities.bullet import Bullet, ExplosiveBullet
from core.config import Config
from entities.player import FastPlayer, ExplosivePlayer
from builder.director import EnemyDirector
from builder.enemy_builder import EnemyBuilder
from utils.check_collision import check_collision
from core.selection_screen import selection_screen

def main():
    pygame.init()

    ## Configuration
    config = Config()
    WIDTH, HEIGHT = config.get('WIDTH'), config.get('HEIGHT')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders")
    font = pygame.font.Font(None, 50)
    score = 0


    selected_option = selection_screen(screen, WIDTH, HEIGHT)
    if selected_option is None:
        return 

    if selected_option == 0:
        player = FastPlayer(WIDTH // 2, HEIGHT - 80, "assets/images/flash.png")
    else:
        player = ExplosivePlayer(WIDTH // 2, HEIGHT - 80, "assets/images/bomberman.png")

    ## Enemies
    director = EnemyDirector()
    builder = EnemyBuilder()

    enemies = [
        director.construct_enemy(builder, "normal"),
        director.construct_enemy(builder, "fast"),
        director.construct_enemy(builder, "strong"),
    ]

    bullets = []

    enemy_spawn_timer = 0

    running = True

    while running:
        pygame.time.delay(30)
        screen.fill((0,0,0))

        ## Events

        for enemy in enemies[:]:
            enemy.move()
            if check_collision(enemy, player):
                running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        player.move(keys, WIDTH)
        player.update_cooldown()

        if keys[pygame.K_SPACE]:
            bullet = player.shoot()
            if bullet:
                bullets.append(bullet)
        
        for bullet in bullets[:]:
            bullet.move()
            if bullet.y < 0:
                bullets.remove(bullet)
        
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if check_collision(bullet, enemy):
                    if isinstance(bullet, ExplosiveBullet):
                        score = bullet.explode(enemies, score)
                    else:
                        enemies.remove(enemy)
                        score += 100
                    bullets.remove(bullet)
                    break
        
        enemy_spawn_timer += 1
        enemy_types = ["normal", "fast", "strong"]

        if enemy_spawn_timer >= 30:
            random_enemy_type = random.choice(enemy_types)

            enemies.append(director.construct_enemy(builder, random_enemy_type))
            enemy_spawn_timer = 0
        
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.update()

    pygame.quit()

main()