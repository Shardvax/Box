import pygame
import sys

pygame.init()
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

sprite_sheet = pygame.image.load("characters/player.png")

# characters are 48x48
sprite_width = 48
sprite_height = 48
num_sprites_x = 6
num_sprites_y = 10

sprites = []
for row in range(num_sprites_y):
    for col in range(num_sprites_x):
        x = col * sprite_width
        y = row * sprite_height
        sprite = sprite_sheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
        sprites.append(sprite)

# Create a sprite class that inherits from Pygame's Sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Create a sprite group
all_sprites = pygame.sprite.Group()
# Instantiate sprite objects and add them to the sprite group
sprite1 = MySprite(100, 100, sprites[0])
sprite2 = MySprite(200, 100, sprites[1])
sprite3 = MySprite(300, 100, sprites[2])
sprite4 = MySprite(400, 100, sprites[3])
sprite5 = MySprite(500, 100, sprites[4])
sprite6 = MySprite(600, 100, sprites[5])
sprite7 = MySprite(100, 200, sprites[6])
sprite8 = MySprite(200, 200, sprites[7])
sprite9 = MySprite(100, 300, sprites[30])
all_sprites.add(sprite1, sprite2, sprite3, sprite4, sprite5, sprite6, sprite7, sprite8, sprite9)


print(all_sprites)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update sprites
    all_sprites.update()

    # Draw sprites
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    pygame.display.flip()
