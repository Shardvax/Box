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
        self.frame_row = []
        for i in range(6):  # there are 6 frames in each row
            frame = self.spritesheet.get_sprite(0, i)  # first row
            self.frame_row.append(frame)
        self.image = self.frame_row[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.current_frame < len(self.frame_row) - 1:
            self.current_frame += 1
        else:
            self.current_frame = 0
        self.image = self.frame_row[self.current_frame]

spritesheet = SpriteSheet("characters/player.png", 48, 48)
player = Player(200, 200, spritesheet)
sprites = pygame.sprite.Group(player)
# all_sprites.add(player2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        else:
            player.update()

    sprites.draw(screen)

    pygame.display.flip()
    clock.tick(11)