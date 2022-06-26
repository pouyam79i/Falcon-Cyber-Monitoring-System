import os
import nlu

text = ["""من یادگیری ماشین را دوست دارم"""]
# model_path = 'resources/persian_w2v_cc_300d_fa_2.7.0_2.4_1607169840793.zip'
# model_path = 'resources/persian_w2v_cc_300d_fa_2.7.0_2.4_1607169840793/persian_w2v_cc_300d_fa_2.7.0_2.4_1607169840793/storage/EMBEDDINGS_glove_300d'
model_path = 'resources/persian_w2v_cc_300d_fa_2.7.0_2.4_1607169840793/persian_w2v_cc_300d_fa_2.7.0_2.4_1607169840793/'
print(os.listdir(model_path))
# farvec_df = nlu.load('resources/persian_w2v_cc_300d_fa_2.7.0_2.4_1607169840793/persian_w2v_cc_300d_fa_2.7.0_2.4_1607169840793/storage/EMBEDDINGS_glove_300d').predict(text, output_level='token')
# farvec_df = nlu.load(path=model_path, verbose=True).predict(text)
nlu.auth()
farvec_df = nlu.load('persian_w2v_cc_300d_fa_2.7.0_2.4_1607169840793', verbose=True).predict(text)
print(farvec_df)