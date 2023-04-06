import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

class SpriteSheet:
    def __init__(self, filename, sprite_width, sprite_height):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height

    def get_sprite(self, row, column):
        x = self.sprite_width * column
        y = self.sprite_height * row
        return self.sheet.subsurface(pygame.Rect(x, y, self.sprite_width, self.sprite_height))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, spritesheet):
        super().__init__()
        self.spritesheet = spritesheet
        self.current_frame = 0
        self.frames_row_1 = []
        self.frames_row_2 = []
        for i in range(6):  # there are 6 frames in each row
            frame = self.spritesheet.get_sprite(0, i)  # first row
            self.frames_row_1.append(frame)
        for i in range(6):  # there are 6 frames in each row
            frame = self.spritesheet.get_sprite(1, i)  # second row
            self.frames_row_2.append(frame)
        self.image = self.frames_row_1[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.current_frame < len(self.frames_row_1) - 1:
            self.current_frame += 1
        else:
            self.current_frame = 0
        self.image = self.frames_row_1[self.current_frame]

    def update_row_2(self):
        if self.current_frame < len(self.frames_row_2) - 1:
            self.current_frame += 1
        else:
            self.current_frame = 0
        self.image = self.frames_row_2[self.current_frame]

spritesheet = SpriteSheet("characters/player.png", 48, 48)
player = Player(100, 100, spritesheet)
player2 = Player(100, 200, spritesheet)
all_sprites = pygame.sprite.Group(player, player2)
# all_sprites.add(player2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.update_row_2()
    else:
        player.update()
        player2.update()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(10)
