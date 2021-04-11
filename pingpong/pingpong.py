from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 151:
            self.rect.y += self.speed
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 151:
            self.rect.y += self.speed

back = (255,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
game = True
finish = False
clock = time.Clock()
FPS = 60
raket1 = Player('ROCKET.png', 30, 200, 4, 40, 150)
raket2 = Player('ROCKET.png', 520, 200, 4, 40, 150)
Ball = GameSprite('Ball.png', 200, 200, 4, 50, 50)
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
                game = False
    if finish != True:
        window.fill(back)
        raket1.update_L()
        raket2.update_R()
        Ball.rect.x += speed_x
        Ball.rect.y += speed_y

        if sprite.collide_rect(raket1, Ball) or sprite.collide_rect(raket2, Ball):
            speed_x *= -1
            speed_y *= 1

        if Ball.rect.y > win_height-50 or Ball.rect.y < 0:
            speed_y *= -1

        if Ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
            game_over = True
        
        if Ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))
            game_over = True
        
        raket1.reset()
        raket2.reset()
        Ball.reset()

        display.update()
        clock.tick(FPS)