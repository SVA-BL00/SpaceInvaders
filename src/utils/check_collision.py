def check_collision(bullet, enemy):
    bullet_width = bullet.width if hasattr(bullet, 'width') else bullet.sprite.get_width()
    bullet_height = bullet.height if hasattr(bullet, 'height') else bullet.sprite.get_height()
    enemy_width = enemy.width if hasattr(enemy, 'width') else enemy.sprite.get_width()
    enemy_height = enemy.height if hasattr(enemy, 'height') else enemy.sprite.get_height()
    
    return (bullet.x < enemy.x + enemy_width and bullet.x + bullet_width > enemy.x and bullet.y < enemy.y + enemy_height and bullet.y + bullet_height > enemy.y)
