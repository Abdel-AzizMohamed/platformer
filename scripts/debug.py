"""Debug module"""

import pygame


def print_info(display: pygame.Surface, text: str, color: str, pos: tuple = (25, 25)):
    """Print info into the game screen"""
    font = pygame.font.Font(None, 16)
    render_font = font.render(text, False, color)
    display.blit(render_font, pos)
