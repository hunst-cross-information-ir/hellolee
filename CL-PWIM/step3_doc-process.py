import copy
import torch
from random import randint
from data_process import process as ps
import numpy as np

from arrange_docs import transform as tf
from predict import Prediction
from collection_extractors import *
import numpy as np
import sys
import time
from multiprocessing import Pool
import multiprocessing
import nltk
from nltk.corpus import stopwords
import nltk.stem.porter as pt

stopword=stopwords.words('english')
stem=pt.PorterStemmer()
def cut(docs):
    new_dict={}
    for key,value in docs:
        sents=nltk.sent_tokenize(value)
        new_doc=[]
        for sen in sents:
            new_sen=sen.lower()
            word_list=nltk.word_tokenize(sen)
            filtered=[stem.stem(w) for w in word_list if (w not in stopword)]
            new_doc.append(filtered)
        new_dict[key]=new_doc
    # print(str(i)+'hah')
    return new_dict

if __name__=="__main__":
    docu_base='../../data/collections/'
    doc_dirs={docu_base+'english/GH95/':extract_english_gh95,docu_base+'english/LATimes94/':extract_english_latimes}
    query_base='../../data/query/'
    query_dir=query_base+'Top-it03.txt'
    queries_dirs=[query_dir,['it','italian']]
    docs=tf(doc_dirs)
    queries=tf(queries_dirs)
    docs_dict=docs.docs_dict
    # print(len(docs_dict.items()))
    # sys.exit(0)

    new_dict={}
    length=len(docs_dict.keys())
    # i=0
    # index=0
    # ap={}
    start=time.time()
    doc_list=list(docs_dict.items())
    nan_docs=['LA091794-0059','LA030494-0028','LA070794-0146','LA092294-0013','LA091194-0065']
    for key,value in docs_dict.items():
        if key in nan_docs:
            print(value)
    sys.exit(0)

    # for key,value in docs_dict.items():
    #     # print(key)
    #     # print(ps.cut_text(value))
    #     # sys.exit(0)
    #     i+=1
    #     new_dict[key]=value
    #     if i%100==0 or i==length:
    #         ap[index]=copy.copy(new_dict)
    #         new_dict.clear()
    #         index+=1
    #         if index==10:
    #             end=time.time()
    #             print(end-start)
    #             break
    #             # sys.exit(0)
    p=Pool(4)
    results=[]
    arg=[]
    for i in range(170):
        if i==169:
            docs=doc_list[1000*i:length]
        else:
            docs=doc_list[1000*i:1000*(i+1)]
        arg.append(docs)
        # result=cut(docs,i)
        # result=p.map(cut,args=(docs,i,),)
        # result=p.map(cut,[docs,i])
        # results.append(result.get())
        # end=time.time()
        # print(end-start)
    result=p.map(cut,arg)
    p.close()
    p.join()
    # print(results)
    np.save('doc_list.npy',result)
    # while True:
    #     results=quene.get()
    #     if quene.empty():
    #         break


# print(len())
# a={1,2,3}

# a={1:2,3:4}
# np.save('1.npy',a)
# b=np.load('1.npy').item()
# print(b)
# c='as'
# print(type(c))
# if isinstance(randint,str):
#     print('haha')
#     print(len(type(randint)))
# # print(len(randint))
# b=randint(0,4)
# print(b)
# for i in range(3):
#     print(i)
# a=[1,2,3]
# del(a[1])
# print(a)
# b=copy.copy(a)
# b.append(4)
# print(a)
# a='word_embedding.weight'
# b='copied_word_embedding.weight'
# model=torch.load('model_static.pkl')
# model.pop(a)
# model.pop(b)
# for key,_ in model.items():
#     print(key)
# a=[]
# b=[[1,2],[3,4]]
# c=[[1,2,3],[4,5],[7,8]]
# a.extend(b)
# a.extend(c)
# print(a)
# model.eval()
# en='This argument is irrational and lacks objectivity.'
# it='Tale argomentazione manca di razionalità e di obiettività.'
# eng=ps.handle_sen(en,'english')
# iti=ps.handle_sen(it,'italian')
# # one=[eng]
# # two=[iti]
# a,b=model(eng,iti,1)
