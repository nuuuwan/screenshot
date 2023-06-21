import os

import imageio
from utils import Log

from utils_future.Image import Image

log = Log(__name__)
DEFAULT_DURATION_MS = 1000
MAX_ANIMATED_GIF_SIZE = 5


class AnimatedGif:
    def __init__(
        self,
        image_path_list: list[str],
        duration_ms: int = DEFAULT_DURATION_MS,
    ):
        assert len(image_path_list) > 0
        self.image_path_list = image_path_list
        self.duration_ms = duration_ms

    def write(self, animation_image_path: str):
        images = []
        for image_path in self.image_path_list:
            assert os.path.exists(image_path)

            resized_image_path = (
                Image.load(image_path).resize(0.5).write_temp()
            )

            img = imageio.imread(resized_image_path)
            images.append(img)

        imageio.mimsave(
            animation_image_path, images, duration=self.duration_ms
        )
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
