from __future__ import division
import torch
from arrange_docs import transform as tf
from collection_extractors import *
import numpy as np
from data_process import process as ps
import numpy as np

#tuan

import torch
from torch.autograd import Variable
import torch.nn as nn
import random
import time
from datetime import datetime
from datetime import timedelta
import pickle
import numpy
from model import DeepPairWiseWord
from util import *
import argparse
import os

from train_set import Get_trainset as gs
from data_process import process as ps
import array
import time
import sys

def Prediction(lsents,rsents,new_set,pretrained_dict,id):
    # =arg
    deep_CNN=True
    EMBEDDING_DIM = 200
    HIDDEN_DIM = 250
    num_epochs = 20
    task='masr'
    granularity='word'
    dict={}
    dict_char_ngram={}
    word_freq={}
    fake_dict={}
    oov=[]
    feature_maps = [50, 100, 150, 200, 200, 200, 200]
    kernels = [1, 2, 3, 4, 5, 6, 7]
    charcnn_embedding_size = 15
    max_word_length = 20
    c2w_mode = False
    character_ngrams = 3
    character_ngrams_2 = None
    character_ngrams_overlap = False
    glove_mode = None
    update_inv_mode = None
    update_oov_mode = None
    combine_mode=None
    lm_mode=None
    word_mode = (glove_mode, update_inv_mode, update_oov_mode)

    basepath= os.path.dirname(os.path.abspath(__file__))


    num_class = 2
    # get_data=gs('../../data/parallel sentences/it-en/europarl-v7.it-en.en','../../data/parallel sentences/it-en/europarl-v7.it-en.it','english','italian')
    # get_data.filter_sents()
    # get_data.sample_negative()
    # trainset=get_data.shuffle()
    # trainset=(one,two,[[1],[0]])

    tokens = []
    count = 0
    num_inv = 0
    num_oov = 0

    glove_mode = True

    update_inv_mode = False
    update_oov_mode = False
    word_mode = (glove_mode, update_inv_mode, update_oov_mode)

        #for line in open(basepath + '/data/' + task + '/vocab.txt'):
        #   tokens.append(line.strip())
    tokens=set()
    # lsents, rsents, labels = testset
    all=0
    for sent in lsents:
        for word in sent:
            tokens.add(word)
            all+=1
    for sent in rsents:
        for word in sent:
            tokens.add(word)
            all+=1
    tokens=list(tokens)
    tokens.append('oov')
    dict = {}
    EMBEDDING_DIM = 300
    wv_dict, wv_arr, wv_size = new_set
    for word in tokens:
        fake_dict[word] = torch.Tensor([random.uniform(-0.05, 0.05) for i in range(EMBEDDING_DIM)])
        try:
            dict[word] = wv_arr[wv_dict[word]]
            num_inv += 1
        except:
            num_oov += 1
            oov.append(word)
            dict[word] = torch.Tensor([random.uniform(-0.05, 0.05) for i in range(EMBEDDING_DIM)])
    # print("all of words"+str(all)+",out of words,"+str(num_oov))
    # print('finished loading word vector, there are ' + str(num_inv) + ' INV words and ' + str(
    #     num_oov) + ' OOV words.')
    # print('current task: ' + task + ', glove mode = ' + str(glove_mode) + ', update_inv_mode = ' + str(
    #     update_inv_mode) + ', update_oov_mode = ' + str(update_oov_mode))
    # saved_file = 'current task: ' + task + ', glove mode = ' + str(glove_mode) + ', update_inv_mode = ' + str(
    #     update_inv_mode) + ', update_oov_mode = ' + str(update_oov_mode) + '.txt'

    model=DeepPairWiseWord(EMBEDDING_DIM,HIDDEN_DIM,1,task,granularity,num_class,dict,fake_dict, dict_char_ngram, oov,tokens, word_freq,
                           feature_maps,kernels,charcnn_embedding_size,max_word_length,character_ngrams,c2w_mode,character_ngrams_overlap, word_mode,
                           combine_mode, lm_mode, deep_CNN)#, corpus)
    if torch.cuda.is_available():
        model=model.cuda()
    for name,parameters in model.named_parameters():
        print(name,':',parameters.size())
    sys.exit(0)

    criterion = nn.MultiMarginLoss(p=1, margin=1.0, weight=None, size_average=True)
    if torch.cuda.is_available():
        criterion = criterion.cuda()
    optimizer = torch.optim.RMSprop(model.parameters(), lr=0.0001)#, momentum=0.1, weight_decay=0.05)#,momentum=0.9,weight_decay=0.95)

    print('start predicting')
    # max_result=-1
    # batch_size=32
    # report_interval=50000
    model_dict=model.state_dict()
    # a='word_embedding.weight'
    # b='copied_word_embedding.weight'
    # pretrained_dict.pop(a)
    # pretrained_dict.pop(b)
    model_dict.update(pretrained_dict)
    model.load_state_dict(model_dict)
    model.eval()
    # test_lsents, test_rsents, test_labels = testset
    test_lsents=lsents
    test_rsents=rsents
    # test_lsents, test_rsents= testset
    predicted = []
    # gold = []
    # correct = 0
    for test_i in range(len(test_lsents)):
        sentA = test_lsents[test_i]
        sentB = test_rsents[test_i]
        output, loss = model(sentA, sentB, 1)
        output = np.exp(output.data[0].cpu().numpy())
        pre=output[1]
        predicted.append(pre)
    print(predicted)
    # return predicted
    score=np.nanmean(np.array(predicted))
    # print(score)
    return (id,score)







