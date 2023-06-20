import os

import imageio
from utils import Log

log = Log(__name__)
DURATION = 0.5


class AnimatedGif:
    def __init__(self, image_path_list: list[str]):
        assert len(image_path_list) > 0
        self.image_path_list = image_path_list

    def write(self, animation_image_path: str):
        images = []
        for image_path in self.image_path_list:
            assert os.path.exists(image_path)
            images.append(imageio.imread(image_path))
        duration = DURATION
        imageio.mimsave(animation_image_path, images, duration=duration)
        file_size_m = os.path.getsize(animation_image_path) / 1_000_000

        log.debug(
            f'Saved AnimatedGif ({self.image_path_list})'
            + f' to {animation_image_path} ({file_size_m:.1f}MB)'
        )
        return animation_image_path
