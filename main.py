import pygame
import os
import sys

pygame.init()
Pusk = False
size = width, height = 1200, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 50
all_sprites = pygame.sprite.Group()
ground_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
sky_group = pygame.sprite.Group()
bomb_group = pygame.sprite.Group()
klad_group = pygame.sprite.Group()
stone_group = pygame.sprite.Group()
blockedsky_group = pygame.sprite.Group()
greenground_group = pygame.sprite.Group()
fon_group = pygame.sprite.Group()
WIN = 0
IMAGES_GIR = 'images/'

tile_width = tile_height = 50


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    # если файл не существует, то выходим
    if not os.path.isfile(IMAGES_GIR + name):
        print(f"Файл с изображением '{name}' не найден")
        sys.exit()
    image = pygame.image.load(IMAGES_GIR + name)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def start_screen():
    intro_text = ['ДЛЯ ПРОДОЛЖЕНИЯ НАЖМИТЕ ПРОБЕЛ']

    fon = pygame.transform.scale(load_image('FirstScreen.png'), (1200, 800))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 650
        intro_rect.top = text_coord
        intro_rect.x = 400
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                if event.key == pygame.K_SPACE and WIN == 0:
                    return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def Completelevel():
    intro_text = ['']

    fon = pygame.transform.scale(load_image('Complete.png'), (1200, 800))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 650
        intro_rect.top = text_coord
        intro_rect.x = 400
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def Lose():
    intro_text = ['']

    fon = pygame.transform.scale(load_image('EndScreen2.png'), (1200, 800))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 650
        intro_rect.top = text_coord
        intro_rect.x = 400
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                pass
        pygame.display.flip()
        clock.tick(FPS)


player_image = pygame.transform.scale(load_image("K0.png"), (30, 40))
boom_image = load_image
tile_images = {
    'empty': pygame.transform.scale(load_image('земля.png'), (50, 50)),
    'greenground': pygame.transform.scale(load_image('трава.png'), (50, 50)),
    'bomb': pygame.transform.scale(load_image('bomb.png'), (50, 50)),
    'sky': pygame.transform.scale(load_image('небо.png'), (50, 50)),
    'stone': pygame.transform.scale(load_image('stone.png'), (50, 50)),
    'blockedsky': pygame.transform.scale(load_image('небо.png'), (50, 50)),
    'fon': pygame.transform.scale(load_image('fonground.png'), (50, 50)),
    'klad': pygame.transform.scale(load_image('klad1.gif'), (50, 50))
}


def load_level(name):
    filename = name
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


Level = load_level('map1.txt')


class Ground(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(ground_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Fon(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(fon_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Bomb(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(bomb_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Klad(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(klad_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Blockedsky(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(blockedsky_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Stone(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(stone_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Sky(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(sky_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Greenground(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(greenground_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def update(self, x, y):
        global WIN
        global Level
        self.rect = self.rect.move(x, y)
        print(self.rect.top)
        if self.rect.left < 0:
            self.rect.x = 0
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.right > 1200:
            self.rect.right = 1200
        elif self.rect.bottom > 800:
            self.rect.bottom = 800
        if pygame.sprite.spritecollideany(self, stone_group) or pygame.sprite.spritecollideany(self, blockedsky_group):
            self.rect = self.rect.move(-x, -y)
        if Level[self.rect.y // 50][self.rect.x // 50] == '2':
            Fon('fon', (self.rect.x // 50), self.rect.y // 50)
            Bomb('bomb', (self.rect.x // 50), self.rect.y // 50)
            WIN = -1
        if Level[self.rect.y // 50][self.rect.x // 50] == '3':
            Level[self.rect.y // 50] = Level[self.rect.y // 50][:(self.rect.x // 50)] \
                                       + '8' + Level[self.rect.y // 50][
                                               (self.rect.x // 50) + 1:]
            Fon('fon', (self.rect.x // 50), self.rect.y // 50)
            Stone('stone', (self.rect.x // 50), self.rect.y // 50)
            self.rect = self.rect.move(-x, -y)
        if Level[self.rect.y // 50][self.rect.x // 50] == '4':
            Level[self.rect.y // 50] = Level[self.rect.y // 50][:(self.rect.x // 50)] \
                                       + '9' + Level[self.rect.y // 50][
                                               (self.rect.x // 50) + 1:]
            Fon('fon', (self.rect.x // 50), self.rect.y // 50)
            Klad('klad', (self.rect.x // 50), self.rect.y // 50)
            WIN += 1
        if Level[self.rect.y // 50][self.rect.x // 50] == '.':
            Level[self.rect.y // 50] = Level[self.rect.y // 50][:(self.rect.x // 50)] \
                                       + '1' + Level[self.rect.y // 50][
                                               ((self.rect.x // 50) + 1):]
            Fon('fon', (self.rect.x // 50), self.rect.y // 50)
        if Level[self.rect.y // 50][self.rect.x // 50] == '6':
            Level[self.rect.y // 50] = Level[self.rect.y // 50][:(self.rect.x // 50)] \
                                       + '1' + Level[self.rect.y // 50][
                                               ((self.rect.x // 50) + 1):]
            Fon('fon', (self.rect.x // 50), self.rect.y // 50)


def generate_level(Level):
    global Pusk
    new_player, x, y = None, None, None
    for y in range(len(Level)):
        for x in range(len(Level[y])):
            if Level[y][x] == '.':
                Ground('empty', x, y)
            elif Level[y][x] == '0':
                Sky('sky', x, y)
            elif Level[y][x] == '1':
                Fon('fon', x, y)
            elif Level[y][x] == '2':
                Ground('empty', x, y)
            elif Level[y][x] == '3':
                Ground('empty', x, y)
            elif Level[y][x] == '4':
                Ground('empty', x, y)
            elif Level[y][x] == '6':
                Greenground('greenground', x, y)
            elif Level[y][x] == '5':
                Blockedsky('sky', x, y)
            elif Level[y][x] == '7':
                Fon('fon', x, y)
                Bomb('bomb', x, y)
            elif Level[y][x] == '8':
                Fon('fon', x, y)
                Stone('stone', x, y)
            elif Level[y][x] == '9':
                Fon('fon', x, y)
                Klad('klad', x, y)
            elif Level[y][x] == '@' and Pusk == False:
                Sky('sky', x, y)
                new_player = Player(x, y)

    # вернем игрока, а также размер поля в клетках
    if Pusk == False:
        Pusk = True
        return new_player, x, y
    else:
        Pusk = True
        return x, y


game_over = True


def main():
    global WIN
    global Pusk
    global Level
    if WIN == 0:
        start_screen()
    fps = 60
    clock = pygame.time.Clock()
    player, level_x, level_y = generate_level(Level)
    running = True
    while running:
        screen.fill((101, 67, 33))
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and WIN == 0:
                    player.update(0, -50)
                elif event.key == pygame.K_DOWN and WIN == 0:
                    player.update(0, 50)
                if event.key == pygame.K_LEFT and WIN == 0:
                    player.update(-50, 0)
                elif event.key == pygame.K_RIGHT and WIN == 0:
                    player.update(50, 0)
        all_sprites.draw(screen)
        player_group.draw(screen)
        if WIN % 2 == 1 and WIN >= 0:
            Completelevel()
        if WIN == -1:
            Lose()
        # обновление экрана
        all_sprites.draw(screen)
        player_group.draw(screen)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()
