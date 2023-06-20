from screenshot.config.ConfigImage import ConfigImage


class ConfigTE(ConfigImage):
    def __init__(self, te_id, description, frequency):
        elem_img_id = 'ImageChart'
        id = f'te.{te_id}'
        url = f'https://tradingeconomics.com/sri-lanka/{te_id}'

        super().__init__(id, description, url, frequency, elem_img_id)
