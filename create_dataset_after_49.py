import nltk
import os
import random


def create_dataset(source_path):
    _, folders, _ = next(os.walk(source_path))
    unwanted_beginnings = [' ', '.', ':', '=', '-', '—', '$', '(', ')', '1', '2', '3',
                           '4', '5', '6', '7', '8', '9']
    number_random_sentences = 1000
    random.seed(100)

    selected_sentences = []
    for folder in folders:
        print("Folder: ", folder)
        path = os.path.join(os.path.join(source_path, folder), folder +
                            "_Wahlperiode_TXT_sents")
        _, _, filenames = next(os.walk(path))
        all_sentences_folder = []
        for file in filenames:
            print(" File: ", file)
            f = open(os.path.join(path, file), encoding='utf-8')
            raw = f.read()
            all_sentences_file = [sent for sent in nltk.sent_tokenize(raw) if sent[0] not
                                  in unwanted_beginnings and sent[-1] != ')' and
                                  len(sent) > 20 and sent[-1] == '.']
            all_sentences_folder += all_sentences_file[5:]

        random_sentences = random.choices(all_sentences_folder,
                                          k=number_random_sentences)
        selected_sentences += random_sentences

    return selected_sentences
