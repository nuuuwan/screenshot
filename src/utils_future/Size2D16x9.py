
from utils_future.Size2D import Size2D
class Size2D16x9(Size2D):
    def __init__(self, width):
        super().__init__(width, int(width * 9 / 16))
