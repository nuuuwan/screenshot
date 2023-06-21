import os

from googletrans import Translator as GoogleTranslator
from utils import File, Log

log = Log(__name__)


class Translator:
    def __init__(self, source_lang: str, target_lang: str):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.translator = GoogleTranslator()
        self.idx = {}
        self.load_idx()

    def translate_nocache(self, text: str) -> str:
        try:
            translated_text = self.translator.translate(
                text, src=self.source_lang, dest=self.target_lang
            ).text
        except Exception as e:
            log.error(f'Failed to translate {text}: {e}')
            translated_text = text
        self.idx[text] = translated_text
        log.debug(f'Translated {text} to {translated_text}')
        self.store_idx()
        return translated_text

    def translate(self, text: str) -> str:
        if text in self.idx:
            return self.idx[text]
        return self.translate_nocache(text)

    def idx_path(self) -> str:
        return os.path.join(
            'src',
            'utils_future',
            f'Translator.{self.source_lang}.{self.target_lang}.txt',
        )

    def load_idx(self):
        if not os.path.exists(self.idx_path()):
            return {}

        lines = File(self.idx_path()).read_lines()
        n = len(lines)
        assert n % 2 == 0
        for i in range(0, n, 2):
            self.idx[lines[i]] = lines[i + 1]
        log.debug(
            f'Loaded {len(self.idx)} translations from {self.idx_path()}'
        )

    def store_idx(self):
        lines = []
        for k, v in self.idx.items():
            lines.append(k)
            lines.append(v)
        log.debug(f'Storing {len(lines)} translations to {self.idx_path()}')
        File(self.idx_path()).write_lines(lines)


class EnglishToSinhala(Translator):
    def __init__(self):
        super().__init__('en', 'si')


class EnglishToTamil(Translator):
    def __init__(self):
        super().__init__('en', 'ta')


if __name__ == '__main__':
    print(EnglishToSinhala().translate('Hello World'))
    print(EnglishToTamil().translate('Hello World'))
