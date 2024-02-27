"""Project start point"""

# pylint: disable=E1101
import sys
import pygame

from scripts.debug import print_info
from scripts.utils import load_image, load_dir_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds


class Game:
    """Define game class"""

    def __init__(self):
        """Init a new game object"""
        pygame.init()
        pygame.mixer.init()

        pygame.display.set_caption("Platformer")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))
        self.clock = pygame.time.Clock()

        self.assets = {
            "decor": load_dir_images("tiles/decor"),
            "grass": load_dir_images("tiles/grass"),
            "large_decor": load_dir_images("tiles/large_decor"),
            "stone": load_dir_images("tiles/stone"),
            "player": load_image("entities/player.png"),
            "background": load_image("background.png"),
            "clouds": load_dir_images("clouds"),
        }

        self.movement = [False, False]
        self.player = PhysicsEntity(self, "player", (50, 50), (8, 15))
        self.clouds = Clouds(self.assets.get("clouds"))

        self.tilemap = Tilemap(self)

        self.scroll = [0, 0]

    def run(self):
        """Starts the game"""
        while True:
            self.display.blit(self.assets["background"], (0, 0))

            self.scroll[0] += (
                self.player.rect().centerx
                - self.display.get_width() / 2
                - self.scroll[0]
            ) / 20
            self.scroll[1] += (
                self.player.rect().centery
                - self.display.get_height() / 2
                - self.scroll[1]
            ) / 20
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.clouds.update()
            self.clouds.render(self.display, render_scroll)

            self.tilemap.render(self.display, offset=render_scroll)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)

            print_info(
                self.display,
                str(self.scroll[0]),
                "#000000",
            )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()),
                (0, 0),
            )
            self.clock.tick(60)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
