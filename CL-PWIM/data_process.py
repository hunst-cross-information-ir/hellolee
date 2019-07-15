import nltk
from nltk.corpus import stopwords
import nltk.stem.porter as pt
from tqdm import tqdm
import array
import torch

stem=pt.PorterStemmer()
class process(object):
    def cut_text(text):
        sents=nltk.sent_tokenize(text)
        return sents
    def handle_sen(sen,lang):
        new_sen=sen.lower()
        word_list=nltk.word_tokenize(sen) 
        filtered=[stem.stem(w) for w in word_list if (w not in stopwords.words(lang))]
        return filtered
    def handle_query(sen,stop):
        new_sen=sen.lower()
        word_list=nltk.word_tokenize(sen) 
        filtered=[stem.stem(w) for w in word_list if (w not in stop)]
        return filtered
    def load_word_vecs(path):
        itos, vectors, dim = [], array.array(str('d')), None
        with open(path, 'r',encoding='utf-8') as f:
            lines = [line for line in f]
        for line in tqdm(lines, total=len(lines)):
            # Explicitly splitting on " " is important, so we don't
            # get rid of Unicode non-breaking spaces in the vectors.
            entries = line.rstrip().split(" ")
            word, entries = entries[0], entries[1:]
            # print(word)
            if dim is None and len(entries) > 1:
                dim = len(entries)
            elif len(entries) == 1:
                continue
            elif dim != len(entries):
                raise RuntimeError(
                    "Vector for token {} has {} dimensions, but previously "
                    "read vectors have {} dimensions. All vectors must have "
                    "the same number of dimensions.".format(word, len(entries), dim))
            vectors.extend(float(x) for x in entries)
            itos.append(word)
        stoi = {word: i for i, word in enumerate(itos)}
        vectors = torch.Tensor(vectors).view(-1, dim)
        dim = dim
        return stoi, vectors, dim






