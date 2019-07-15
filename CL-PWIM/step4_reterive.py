from arrange_docs import transform as tf
from predict import Prediction
from collection_extractors import *
import numpy as np
import sys
import time
from multiprocessing import Pool
import multiprocessing
import torch
from data_process import process as ps
import copy
import random
# docu_base='../../data/collections/'
# doc_dirs={docu_base+'english/GH95/':extract_english_gh95,docu_base+'english/LATimes94/':extract_english_latimes}
query_base='../data/query/'
query_dir=query_base+'Top-en03.txt'
queries_dirs=[query_dir,['en','english']]
# docs=tf(doc_dirs)
queries=tf(queries_dirs)
# docs_dict=docs.docs_dict
# np.save('doc.npy',docs_dict)
query_dict=queries.docs_dict
# np.save('query.npy',query_dict)
# query_dict=queries.process_docs()

def sample_doc(docs):
    # for c in docs.keys():
    a=random.sample(docs.keys(),10000)
    b={}
    for key in a:
        b[key]=docs[key]
    # print(len(b.keys()))
    return b
def dream(i):
    return i*i

if __name__=='__main__':
    docs_dict={}
    doc_list=np.load('doc_list.npy')
    h=0
    id_docs=np.load('id_docs.npy').item()
    # print(id_docs)
    # sys.exit(0)
    pretrained_dict=torch.load('new_model_static.pkl')
    new_set=ps.load_word_vecs('../data/bilingual embeddings/fasttext.txt')
    start=time.time()
    may=0
    p=Pool(6)
    for key,value in query_dict.items():
        if str(key) not in id_docs.keys():
            continue
        for a in doc_list:
            for ob,ov in a.items():
                if ob in id_docs[str(key)]:
                    docs_dict[ob]=ov
        strat=time.time()
        arg=[]
        results=[]
        for id,doc in docs_dict.items():
            sentences=[]
            queries=[]
            lg=len(doc)
            sentences.extend(doc)
            for j in range(lg):
                queries.append(value)
            result=p.apply_async(Prediction,(queries,sentences,new_set,pretrained_dict,id))
            results.append(result.get())

        np.save('results/'+str(key)+'_doc_score-test.npy',results)
        docs_dict={}
        end=time.time()
        print(end-start)
    p.close()
    p.join()
        # break





