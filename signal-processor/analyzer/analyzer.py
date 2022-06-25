# encoding: utf-8
from __future__ import unicode_literals
import hazm
from polyglot.text import Text, Word, WordList, Chunk, Sentence
from typing import List

import symbols
import os
import summarizer

symbols.import_symbols()

normalizer = hazm.Normalizer()
stemmer = hazm.Stemmer()
lemmatizer = hazm.Lemmatizer()

tagger = hazm.POSTagger(model='../resources/hazm/postagger.model')
chunker = hazm.Chunker(model='../resources/hazm/chunker.model')


def count_symbols(words: List['str'], symbols_count: dict):
    for w in words:
        if symbols.symbols.get(w):
            symbols_count[w] = symbols_count[w] + 1 if symbols_count.get(w) else 1
    return symbols_count


def parse_text(txt):
    txt = normalizer.normalize(txt)
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
    lemmatized_arr = []
    for w in text.words:
        lemmatized_arr.append(lemmatizer.lemmatize(w))
    sentence = ' '.join(lemmatized_arr)
    text = Text(sentence)
    symbols_count = count_symbols(text.words, symbols_count)
    for w in text.words:
        print('{:<16}{:>2}'.format(w, w.polarity))
        polarity += w.polarity
    print(symbols_count)
    print(polarity)
    # print("Language Detected: Code={}, Name={}\n".format(text.language.code, text.language.name))


if __name__ == '__main__':
    txt = '''فاذر 15 درصد سودین الان هم زیر مقاومت 120 هست که یه کم سخته رد کردنش.
    حد ضرر همون 100
    خرید جدید فعلا ممنوع'''
    # parse_text(txt)
    article = '''ترکیب یونی گونه‌ای ترکیب شیمیایی است که ذره‌های سازندهٔ آن یون‌های مثبت و منفی هستند. شکل متداول 
    ترکیبات یونی از یک فلز به‌عنوان کاتیون و یک نافلز به‌عنوان آنیون تشکیل می‌شود؛ فلزها تمایل به ازدست‌دادن الکترون 
    و تبدیل‌شدن به یون مثبت را دارند، و نافلزها تمایل به گرفتن الکترون و تبدیل‌شدن به یون منفی را دارند. ترکیبات یونی 
    به‌طور طبیعی در سنگ‌های معدنی و به صورت محلول در آب دریاها و اقیانوس‌ها یافت می‌شوند اما در هواکره وجود ندارند. 
    نخستین توضیحات علمی در مورد این ترکیب‌ها به دانشمند انگلیسی مایکل فارادی بر می‌گردد که نام «یون» به معنی «رونده» 
    یا «متحرک» را بر روی اجزای سازنده این ترکیبات قرار داد. نخستین توصیف علمی از ساختار بلوری این ترکیبات توسط ویلیام 
    هنری و ویلیام لورنس براگ در سال ۱۹۱۳ انجام گرفت. 

ترکیبات یونی به‌وسیله گونه‌ای پیوند شیمیایی بسیار قوی به نام پیوند یونی تشکیل می‌شوند؛ در نتیجه، این ترکیبات از دمای 
ذوب و جوش بالایی برخوردارند و عمدتاً در دمای اتاق به صورت جامد هستند. در حالت جامد، ترکیبات یونی می‌توانند شکل بلورین 
منظم داشته باشند که از قواعد موجود برای توصیف ساختارهای بلوری در علم بلورشناسی پیروی می‌کند. در حالت محلول در 
حلال‌های قطبی نظیر آب، این ترکیبات به یون‌های مثبت و منفی تفکیک و توسط مولکول حلال، حلال‌پوشیده می‌شوند. این مواد به 
دلیل این که از یک شبکه بلورین یکپارچه تشکیل شده‌اند، فاقد مولکول‌اند؛ در نتیجه، ساده‌ترین نسبت کاتیون‌ها به آنیون‌ها 
در ترکیب — که به آن سلول واحد گفته می‌شود — به‌عنوان فرمول شیمیایی ترکیبات یونی ذکر می‌شود. سختی، شکنندگی، نارسانایی 
الکتریکی در حالت جامد، رسانایی الکتریکی در حال مذاب و محلول، و تنوع رنگی بالا از ویژگی‌های این ترکیبات است. عدهٔ 
اندکی از ترکیبات یونی در دماهای متعارف مایع هستند که به آن‌ها مایع یونی گفته می‌شود. 

ترکیبات یونی از دیرباز برای بشر شناخته شده بودند؛ از جمله نمک طعام که به‌عنوان طعم‌دهنده در غذاها کاربرد دارد. اسامی 
متعددی بر روی برخی از ترکیبات یونی گذاشته شده‌است اما روش نظام‌مند و یکپارچه در نام گذاری این مواد توسط اتحادیهٔ 
بین‌المللی شیمی محض و کاربردی (آیوپاک) تعیین شده‌است و امروزه از این روش برای نامگذاری آن‌ها استفاده می‌شود. ترکیبات 
یونی در بدن جانداران، از جمله انسان، به فراوانی یافت می‌شوند و نقشی حیاتی در فرآیندهای زیستی ایفا می‌کنند؛ همچون 
یون‌های آهن که در ساختار گلبول‌های قرمز خونی وجود دارند یا یون‌های پتاسیم که در عملکرد عضلات نقشی کلیدی ایفا می‌کنند. 

ترکیبیات یونی کاربردهای فراوانی در صنایع دارند؛ همچون مواد رنگزا، مواد اولیه برای تولید محصولات دیگر، فرآوری بسیاری 
از فلزات، تولید باتری و پیل‌های الکتروشیمیایی. در صنایع غذایی از این ترکیبات به‌عنوان نگه‌دارنده، طعم‌دهنده و عامل 
ورآورنده استفاده می‌شود و در صنایع دارویی به‌عنوان تأمین‌کننده برخی ریزمغذی‌ها کاربرد دارند. همچنین برخی داروها با 
روش‌های ویژه به صورت ترکیبات یونی درآورده می‌شوند تا میزان فراهمی زیستی و اثرگذاری آن‌ها افزایش یابد. 

'''
    # print(parse_text('وقت مناسبی برای فروش است'))
    # print(parse_text(txt))
    # import fasttext
    # model_path = 'resources/Persian-Wikipedia-Corpus/models/fasttext-cbow/fasttext.model-size=200-window=5.bin'
    # data = 'resources/Dataset-TSE-chat-in-Telegram-group/chat.clean.txt'
    # model_path = 'resources/fasttext.telegram.tse.chat.bin'
    # model = fasttext.train_supervised(data)
    # model.save_model(model_path)
    # print('سلام!0')
    # model = fasttext.load_model(model_path, encoding='utf-8')
    # model = fasttext.load_model(model_path)
    # print('سلام!')
    # model.predict_output_word('سلام')
    print(parse_text(txt))
