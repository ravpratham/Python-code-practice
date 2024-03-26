import numpy as np
from PIL import Image
import os
import string
from pickle import dump
from pickle import load
from keras.applications.xception import Xception  # to get pre-trained model Xception
from keras.applications.xception import preprocess_input
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.text import Tokenizer  # for text tokenization
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from tensorflow.keras.layers import merge
from keras.models import Model, load_model
from keras.layers import Input, Dense  # Keras to build our CNN and LSTM
from keras.layers import LSTM, Embedding, Dropout
from tqdm import tqdm_notebook as tqdm  # to check loop progress

tqdm().pandas()


# Load the document file into memory
def load_fp(filename):
    # Open file to read
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text

def load_doc(filename):
    # Opening the file as read only
    with open(filename, 'r') as fh:
        return fh.read()


# get all images with their captions
def img_capt(filename):
    file = load_doc(filename)
    captions = file.split('n')
    descriptions = {}
    for caption in captions[:-1]:
        img, caption = caption.split('t')
        if img[:-2] not in descriptions:
            descriptions[img[:-2]] = [caption]
        else:
            descriptions[img[:-2]].append(caption)
        return descriptions


# Data cleaning function will convert all upper case alphabets to lowercase, removing punctuations and words containing numbers
def txt_clean(captions):
    table = str.maketrans('', '', string.punctuation)
    for img, caps in captions.items():
        for i, img_caption in enumerate(caps):
            img_caption.replace("-", " ")
            descp = img_caption.split()
            # uppercase to lowercase
            descp = [wrd.lower() for wrd in descp]
            # remove punctuation from each token
            descp = [wrd.translate(table) for wrd in descp]
            # remove hanging 's and a
            descp = [wrd for wrd in descp if (len(wrd) > 1)]
            # remove words containing numbers with them
            descp = [wrd for wrd in descp if (wrd.isalpha())]
            # converting back to string
            img_caption = ' '.join(descp)
            captions[img][i] = img_caption
            return captions


def txt_vocab(descriptions):
    # To build vocab of all unique words
    vocab = set()
    for key in descriptions.keys():
        [vocab.update(d.split()) for d in descriptions[key]]
        return vocab


# To save all descriptions in one file
def save_descriptions(descriptions, filename):
    lines = list()
    for key, desc_list in descriptions.items():
        for desc in desc_list:
            lines.append(key + 't' + desc)
            data = "n".join(lines)
            file = open(filename, "w")
            file.write(data)
            file.close()

# Set these path according to project folder in you system, like i create a folder with my name shikha inside D-drive
dataset_text = "D:shikhaProject - Image Caption GeneratorFlickr_8k_text"
dataset_images = "D:shikhaProject - Image Caption GeneratorFlicker8k_Dataset"
# to prepare our text data
filename = dataset_text + "/" + "Flickr8k.token.txt"
# loading the file that contains all data
# map them into descriptions dictionary
descriptions = img_capt(filename)
print("Length of descriptions =", len(descriptions))
# cleaning the descriptions
clean_descriptions = txt_clean(descriptions)
# to build vocabulary
vocabulary = txt_vocab(clean_descriptions)
print("Length of vocabulary = ", len(vocabulary))
# saving all descriptions in one file
save_descriptions(clean_descriptions, "descriptions.txt")
