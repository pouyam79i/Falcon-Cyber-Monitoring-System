import json
from symbols import Symbol


class Signal:
    def __init__(self, uid, text,  symbols: [Symbol], polarity, date, time, info=''):
        self.uid = uid
        self.symbols = symbols
        self.polarity = polarity
        self.text = text
        self.info = info
        self.date = date
        self.time = time

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def serialize(self):
        return {
            'uid': str(self.uid),
            'symbols': str(self.symbols),
            'polarity': str(self.polarity),
            'text': str(self.text),
            'info': str(self.info),
            'date': str(self.date),
            'time': str(self.time),
        }

    def set_polarity(self, polarity):
        self.polarity = polarity

    def set_text(self, text):
        self.text = text

    def add_symbols(self, *symbols: list[Symbol]):
        if isinstance(self.symbols, list):
            self.symbols.append(*symbols)
        else:
            self.symbols = symbols
