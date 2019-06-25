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
query_base='../../data/query/'
query_dir=query_base+'Top-it03.txt'
queries_dirs=[query_dir,['it','italian']]
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
    # doc_ids=np.load('doc_id.npy')
    h=0
    # nan_docs=['LA091794-0059','LA030494-0028','LA070794-0146','LA092294-0013','LA091194-0065']
    for a in doc_list:
        for key,value in a.items():
            docs_dict[key]=value
    docs_dict2=sample_doc(docs_dict)
    np.save('sample_doc_10000.npy',docs_dict2)
    del doc_list
    pretrained_dict=torch.load('new_model_static.pkl')
    new_set=ps.load_word_vecs('../../data/bilingual embeddings/fasttext.txt')
    start=time.time()
    may=0
    p=Pool(6)
    for key,value in query_dict.items():
        strat=time.time()
        arg=[]
        results=[]
        for id,doc in list(docs_dict2.items())[0:1000]:
            sentences=[]
            queries=[]
            lg=len(doc)
            sentences.extend(doc)
            for j in range(lg):
                queries.append(value)
            result=p.apply_async(Prediction,(queries,sentences,new_set,pretrained_dict,id))
            results.append(result.get())
        # try:
        # doc_score=p.map(Prediction,arg)
        p.close()
        p.join()
        np.save('results/'+str(key)+'_doc_score-test.npy',results)
        # np.save('do_dict.npy',do_dict)
        end=time.time()
        print(end-start)
        break





