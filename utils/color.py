# Basic Colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)

WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def rgb_to_gl_color(rgb_color: tuple[int, int, int], alpha: float = 1.0) -> tuple[float, float, float, float]:
    """Convert RGB color (0-255) to OpenGL color format (0-1)"""
    return (rgb_color[0] / 255.0, rgb_color[1] / 255.0, rgb_color[2] / 255.0, alpha)