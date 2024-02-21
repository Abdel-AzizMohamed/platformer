"""Contains game entities"""

import pygame


class PhysicsEntity:
    """Define game physics entity"""

    def __init__(self, game, e_type: str, pos, size: int):
        """init a new physics entity object"""
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
        }

    def rect(self):
        """Creates a new rect for the object"""
        return pygame.Rect(
            self.pos[0], self.pos[1], self.size[0], self.size[1]
        )

    def update(self, tilemap, movement=(0, 0)):
        """Update entity position"""
        self.collisions = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
        }

        frame_movement = (
            movement[0] + self.velocity[0],
            movement[1] + self.velocity[1],
        )

        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions["right"] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions["left"] = True
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions["down"] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions["up"] = True
                self.pos[1] = entity_rect.y

        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        if self.collisions.get("down") or self.collisions.get("up"):
            self.velocity[1] = 0

    def render(self, surf: pygame.Surface):
        """Render entity in a given surface"""
        surf.blit(self.game.assets["player"], self.pos)
