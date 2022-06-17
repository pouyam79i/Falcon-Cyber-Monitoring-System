# encoding: utf-8
from __future__ import unicode_literals
import hazm
from polyglot.text import Text, Word, WordList, Chunk, Sentence
import symbols
symbols.import_symbols()

normalizer = hazm.Normalizer()
stemmer = hazm.Stemmer()
lemmatizer = hazm.Lemmatizer()
tagger = hazm.POSTagger(model='resources/postagger.model')
chunker = hazm.Chunker(model='resources/chunker.model')


def count_symbols(words: list['str'], symbols_count: dict):
    for w in words:
        if symbols.symbols.get(w):
            symbols_count[w] = symbols_count[w] + 1 if symbols_count.get(w) else 1
    return symbols_count


def parse_text(txt):
    symbols_count = {}
    polarity = 0
    # print('normalizer')
    # print(normalizer.normalize(txt))
    # print('sent tokenize')
    # print(hazm.sent_tokenize(txt))
    # print('stem')
    # print(stemmer.stem(txt))
    # print('lemmatize')
    # print(lemmatizer.lemmatize(txt))
    print('tag')
    tag = tagger.tag(hazm.word_tokenize(txt))
    print(tag)
    # print('tree2brackets')
    # print(hazm.tree2brackets(chunker.parse(tag)))
    # parser = hazm.DependencyParser(tagger=tagger, lemmatizer=lemmatizer)
    # print('parse')
    # print(parser.parse(hazm.word_tokenize(txt)))

    # WordList([symbol.symbol for symbol in symbols.symbols], language='fa')
    text = Text(txt)
    print(text.words)
    symbols_count = count_symbols(text.words, symbols_count)
    print(text.sentences)
    for w in text.words:
        polarity += w.polarity
    print(symbols_count)
    print(polarity)
    # print("Language Detected: Code={}, Name={}\n".format(text.language.code, text.language.name))


if __name__ == '__main__':
    txt = '''فاذر 15 درصد سودین الان هم زیر مقاومت 120 هست که یه کم سخته رد کردنش.
    حد ضرر همون 100
    خرید جدید فعلا ممنوع'''
    parse_text(txt)
