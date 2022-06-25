from typing import List

from symbols import Symbol


class Signal:
    def __init__(self, text, symbols: [Symbol], polarity, info):
        self.symbols = symbols
        self.polarity = polarity
        self.text = text
        self.info = info

    def set_polarity(self, polarity):
        self.polarity = polarity

    def set_text(self, text):
        self.text = text

    def add_symbols(self, *symbols: List[Symbol]):
        if isinstance(self.symbols, list):
            self.symbols.append(*symbols)
        else:
            self.symbols = symbols
