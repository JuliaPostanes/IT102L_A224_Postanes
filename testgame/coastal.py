import sys
import os
import random
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
SAND_COLOR = (250, 187, 92)
WATER_COLOR = (38, 201, 255)
PLAYER_COLOR = (40, 90, 60)
TRASH_COLOR = (90, 90, 90)
PLAYER_SIZE = 48
TRASH_SIZE = 18
PLAYER_SPEED = 4
TOTAL_TRASH = 20
FPS = 60


class Player:
    """The character walking around the beach, controlled with arrow keys / WASD."""

    def __init__(self, x, y, image_path=None):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = PLAYER_SPEED
        self.image = None
        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))

    def handle_input(self, keys):
        dx = dy = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += self.speed
        self.rect.x = max(0, min(SCREEN_WIDTH - self.rect.width, self.rect.x + dx))
        self.rect.y = max(0, min(SCREEN_HEIGHT - self.rect.height, self.rect.y + dy))

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, PLAYER_COLOR, self.rect, border_radius=6)


class TrashItem:
    """A single piece of litter on the beach, waiting to be collected."""

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TRASH_SIZE, TRASH_SIZE)
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            pygame.draw.rect(screen, TRASH_COLOR, self.rect, border_radius=3)


class Game:
    """Owns the player, the trash items, score, and win state."""

    def __init__(self):
        self.player = Player(
            SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60,
            image_path=os.path.join(BASE_DIR, "assets", "BERDLY_PLAYER.png"),
        )
        self.trash_items = [self._random_trash() for _ in range(TOTAL_TRASH)]
        self.collected_count = 0

    def _random_trash(self):
        x = random.randint(10, SCREEN_WIDTH - TRASH_SIZE - 10)
        y = random.randint(90, SCREEN_HEIGHT - TRASH_SIZE - 10)
        return TrashItem(x, y)

    def update(self, keys):
        self.player.handle_input(keys)
        for item in self.trash_items:
            if not item.collected and self.player.rect.colliderect(item.rect):
                item.collected = True
                self.collected_count += 1

    def beach_health(self):
        return int(100 * self.collected_count / TOTAL_TRASH)

    def is_won(self):
        return self.collected_count >= TOTAL_TRASH

    def draw(self, screen, font):
        screen.fill(WATER_COLOR)
        pygame.draw.rect(screen, SAND_COLOR, (0, 80, SCREEN_WIDTH, SCREEN_HEIGHT - 80))

        for item in self.trash_items:
            item.draw(screen)
        self.player.draw(screen)

        hud = f"Trash collected: {self.collected_count}/{TOTAL_TRASH}   Cleaned: {self.beach_health()}%"
        screen.blit(font.render(hud, True, (0, 6, 31)), (10, 10))

        if self.is_won():
            msg = font.render("Beach restored! Press ESC to quit.", True, (0, 6, 31))
            screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Coastal Restoration")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    game = Game()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()
        game.update(keys)
        game.draw(screen, font)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()