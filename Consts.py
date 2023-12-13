from ctypes import windll

MAP_WIDTH = 50
MAP_HEIGHT = 50
CHUNK_SIZE = 48

WIDTH: int = windll.user32.GetSystemMetrics(0)
HEIGHT: int = windll.user32.GetSystemMetrics(1)

TICKS = 120
FPS = 120
