import json
from symbols import Symbol


class Signal:
    def __init__(self, text,  symbols: [Symbol], polarity, info=None):
        self.symbols = symbols
        self.polarity = polarity
        self.text = text
        self.info = info

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def set_polarity(self, polarity):
        self.polarity = polarity

    def set_text(self, text):
        self.text = text

    def add_symbols(self, *symbols: list[Symbol]):
        if isinstance(self.symbols, list):
            self.symbols.append(*symbols)
        else:
            self.symbols = symbols
