import nltk
import os
import random


def create_dataset_before_49(source_path):
    source_path = 'C:/Users/j.hammerschmitt/Downloads/Data_before49/'
    unwanted_beginnings = [' ', '.', ':', '=', '-', '—', '$', '(', ')', '1', '2', '3',
                           '4', '5', '6', '7', '8', '9']
    number_random_sentences = 1000
    random.seed(100)

    selected_sentences = []
    _, _, filenames = next(os.walk(source_path))
    for file in filenames:
        f = open(os.path.join(source_path, file), encoding='utf-8')
        raw = f.read()
        all_sentences_file = [sent for sent in nltk.sent_tokenize(raw) if
                              sent[0] not in unwanted_beginnings and
                              sent[-1] != ')' and len(sent) > 20 and sent[-1] == '.']
        random_sentences = random.choices(all_sentences_file[60:],
                                          k=number_random_sentences)
        selected_sentences += random_sentences

    return selected_sentences
