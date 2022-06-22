import os

from transformers import (
    BertTokenizerFast,
    EncoderDecoderConfig,
    EncoderDecoderModel
)


def summarize(txt):
    def assign_gpu(tokenizer_output):
        print(tokenizer_output)
        tokens_tensor = tokenizer_output['input_ids'].to('cuda:0')
        token_type_ids = tokenizer_output['token_type_ids'].to('cuda:0')
        attention_mask = tokenizer_output['attention_mask'].to('cuda:0')

        output = {
            'input_ids': tokens_tensor,
            'token_type_ids': token_type_ids,
            'attention_mask': attention_mask
        }

        return output

    # from datasets import load_dataset
    #
    # cache_dir = None
    #
    # # Version 2.0.0
    # train_set = load_dataset('./resources/wiki-summary/datasets/wiki_summary_persian', '2.0.0', split='train', cache_dir=cache_dir)
    # dev_set = load_dataset('./resources/wiki-summary/datasets/wiki_summary_persian', '2.0.0', split='validation', cache_dir=cache_dir)
    # test_set = load_dataset('./resources/wiki-summary/datasets/wiki_summary_persian', '2.0.0', split='test', cache_dir=cache_dir)
    #
    # print('VERSION 2.0.0')
    # print(f'train_set \n {train_set}')
    # print(f'dev_set \n {dev_set}')
    # print(f'test_set \n {test_set}')
    # print()
    # print()

    model_name = 'm3hrdadfi/bert2bert-fa-wiki-summary'
    model_basepath = './resources/'
    model_path = model_basepath + model_name
    save = False
    if not os.path.exists(model_path):
        model_path = model_name
        save = True
    tokenizer = BertTokenizerFast.from_pretrained(model_path)
    config = EncoderDecoderConfig.from_pretrained(model_path)
    model = EncoderDecoderModel.from_pretrained(model_path, config=config)
    if save:
        tokenizer.save_pretrained(model_path)
        config.save_pretrained(model_path)
        model.save_pretrained(model_path)

    sequence = txt
    # inputs = assign_gpu(tokenizer([sequence], padding="max_length", truncation=True, max_length=512, return_tensors="pt"))
    inputs = tokenizer([sequence], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids
    attention_mask = inputs.attention_mask

    outputs = model.generate(input_ids, attention_mask=attention_mask)
    generated = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return generated
