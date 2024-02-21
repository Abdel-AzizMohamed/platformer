"""Contains game tile system"""

from typing import Tuple, List
import pygame


NEIGHBOR_OFFSETS = [
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (0, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]
PHYSICS_TILES = {"grass", "stone"}


class Tilemap:
    """Define a tile map class"""

    def __init__(self, game, tile_size: int = 16) -> None:
        """Init a new tile map object"""
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ";10"] = {
                "type": "grass",
                "variant": 1,
                "pos": (3 + i, 10),
            }
            self.tilemap["10;" + str(5 + i)] = {
                "type": "stone",
                "variant": 1,
                "pos": (10, 5 + i),
            }

    def tiles_around(self, pos: Tuple[int]) -> List[dict]:
        """Checks the nearby tiles that around an given object position"""
        nearby_tiles = []

        tile_loc = (
            int(pos[0] // self.tile_size),
            int(pos[1] // self.tile_size),
        )
        for offset in NEIGHBOR_OFFSETS:
            check_loc = (
                str(tile_loc[0] + offset[0])
                + ";"
                + str(tile_loc[1] + offset[1])
            )
            if check_loc in self.tilemap:
                nearby_tiles.append(self.tilemap.get(check_loc))

        return nearby_tiles

    def physics_rects_around(self, pos):
        """"""
        rects = []
        for tile in self.tiles_around(pos):
            if tile.get("type") in PHYSICS_TILES:
                rects.append(
                    pygame.Rect(
                        tile.get("pos")[0] * self.tile_size,
                        tile.get("pos")[1] * self.tile_size,
                        self.tile_size,
                        self.tile_size,
                    )
                )
        return rects

    def render(self, surf: pygame.Surface) -> None:
        """Render tilemap in a given surface"""
        for tile in self.offgrid_tiles:
            surf.blit(
                self.game.assets[tile.get("type")[tile.get("variant")]],
                tile.get("pos"),
            )

        for tile in self.tilemap.values():
            surf.blit(
                self.game.assets[tile.get("type")][tile.get("variant")],
                (
                    tile.get("pos")[0] * self.tile_size,
                    tile.get("pos")[1] * self.tile_size,
                ),
            )
