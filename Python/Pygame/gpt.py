import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.jump_speed = -10
        self.jump_height = 100
        self.jumped = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            if self.jumped < self.jump_height:
                self.rect.y += self.jump_speed
                self.jumped += abs(self.jump_speed)
            else:
                self.jumped = 0
        elif self.rect.y < height - 50:
            self.rect.y += self.speed
        else:
            self.rect.y = height - 50

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

player = Player(width // 2, height - 50)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

walls = [
    Wall(200, height - 100, 50, 100),
    Wall(400, height - 150, 50, 150),
    Wall(600, height - 50, 50, 50),
]
all_sprites.add(walls)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()
    
    player_hits = pygame.sprite.spritecollide(player, walls, False)
    for wall in player_hits:
        if player.rect.bottom > wall.rect.top:
            player.rect.bottom = wall.rect.top
            player.jumped = 0

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
