import os
import pandas as pd

from create_dataset_after_49 import create_dataset
from create_dataset_before_49 import create_dataset_before_49

###
# Create dataset of BRD Protokolle
###

source_path = 'C:/Users/j.hammerschmitt/Downloads/Data/BRD Protokolle/'
selected_sentences = create_dataset(source_path)

df = pd.DataFrame(selected_sentences, columns=["sentence"])
df.to_csv(os.path.join(source_path, "sentences_after_49.csv"), index=False,
          encoding="utf-8-sig")

# Load dataset and add epochs for dataset after 49

df = pd.read_csv(os.path.join(source_path, "sentences_after_49.csv"),
                 encoding="utf-8-sig")
_, folders, _ = next(os.walk(source_path))
names = []
for folder in folders:
    path = os.path.join(os.path.join(source_path, folder), folder + "_Wahlperiode_TXT")
    _, _, filenames = next(os.walk(path))
    name = filenames[1][-8:-4] + " - " + filenames[-1][-8:-4]
    names.append(name)

names[10] = '2018 - 2020'

names_final = []
for name in names:
    for i in range(1000):
        names_final.append(name)

df['epoch'] = names_final
df.to_csv(os.path.join(source_path, "sentences_after_49.csv"), index=False,
          encoding="utf-8-sig")

###
# Create dataset of data before 49
###

source_path = 'C:/Users/j.hammerschmitt/Downloads/Data_before49/'
selected_sentences = create_dataset_before_49(source_path)

df = pd.DataFrame(selected_sentences, columns=["sentence"])
df.to_csv(os.path.join(source_path, "sentences_before_49.csv"), index=False,
          encoding="utf-8-sig")