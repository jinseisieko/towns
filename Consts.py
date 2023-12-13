from ctypes import windll

MAP_WIDTH = 100
MAP_HEIGHT = 100
CHUNK_SIZE = 100

WIDTH: int = windll.user32.GetSystemMetrics(0)
HEIGHT: int = windll.user32.GetSystemMetrics(1)

TICKS = 60
FPS = 60
