import csv

class Symbol:
    def __init__(self, args):
        faname, symbol, enname, ensymbol, board, industry_group, group, code, *extra = args[::-1]
        self.faname = faname
        self.symbol = symbol
        self.enname = enname
        self.board = board
        self.industry_group = industry_group
        self.group = group
        self.code = code

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.symbol

symbols = {}

def import_symbols():
    with open('resources/TSETMC/symbols/symbols.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter='	')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                symbol = Symbol(row)
                symbols[symbol.symbol] = symbol
                line_count += 1