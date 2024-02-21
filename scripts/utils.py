"""Contains game utils"""

import os
from typing import List
import pygame


BASE_IMAGE_PATH = "data/images"


def load_image(path: str) -> pygame.Surface:
    """
    Load a given image

    Arguments:
        path: image path

    Returns:
        loaded image
    """
    img = pygame.image.load(os.path.join(BASE_IMAGE_PATH, path)).convert()
    img.set_colorkey((0, 0, 0))
    return img


def load_dir_images(path: str) -> List[pygame.Surface]:
    """
    Load all images in a given path

    Arguments:
        path: directory path

    Returns:
        list contains all directory images loaded
    """
    images = []

    for image in sorted(os.listdir(os.path.join(BASE_IMAGE_PATH, path))):
        image = pygame.image.load(
            os.path.join(BASE_IMAGE_PATH, path, image)
        ).convert()
        image.set_colorkey((0, 0, 0))
        images.append(image)

    return images
