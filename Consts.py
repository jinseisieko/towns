from ctypes import windll

MAP_WIDTH = 30
MAP_HEIGHT = 30
CHUNK_SIZE = 100


WIDTH: int = windll.user32.GetSystemMetrics(0)
HEIGHT: int = windll.user32.GetSystemMetrics(1)

TICKS = 60
FPS = 60
