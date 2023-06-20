import os

import imageio
from utils import Log

log = Log(__name__)
FPS = 1
MAX_ANIMATED_GIF_SIZE = 5_000_000


class AnimatedGif:
    def __init__(self, image_path_list: list[str]):
        assert len(image_path_list) > 0
        self.image_path_list = image_path_list

    def write(self, animation_image_path: str):
        images = []
        for image_path in self.image_path_list:
            assert os.path.exists(image_path)
            images.append(imageio.imread(image_path))

        imageio.mimsave(animation_image_path, images, fps=FPS)
        file_size_m = os.path.getsize(animation_image_path) / 1_000_000

        log.debug(
            f'Saved AnimatedGif ({self.image_path_list})'
            + f' to {animation_image_path} ({file_size_m:.1f}MB)'
        )
        if file_size_m > MAX_ANIMATED_GIF_SIZE:
            raise Exception(
                f'AnimatedGif ({self.image_path_list})'
                + f' is too large ({file_size_m:.1f}MB)'
                + f' for {animation_image_path}'
            )
        return animation_image_path
