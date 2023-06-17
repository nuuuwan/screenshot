from screenshot.config.ConfigImage import ConfigImage


class ConfigTE(ConfigImage):
    def __init__(self, id, description, url, frequency):
        elem_img_id = 'ImageChart'
        super().__init__(id, description, url, frequency, elem_img_id)
