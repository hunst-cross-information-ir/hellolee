# # import copy
# import torch
# from random import randint
# from data_process import process as ps
# import numpy as np

# from arrange_docs import transform as tf
# from predict import Prediction
# from collection_extractors import *
# import numpy as np
# import sys
# import time
# from multiprocessing import Pool
# import multiprocessing
# import nltk
# from nltk.corpus import stopwords
# import nltk.stem.porter as pt

# stopword=stopwords.words('english')
# stem=pt.PorterStemmer()
# def cut(docs):
#     new_dict={}
#     for key,value in docs:
#         sents=nltk.sent_tokenize(value)
#         new_doc=[]
#         for sen in sents:
#             new_sen=sen.lower()
#             word_list=nltk.word_tokenize(sen)
#             filtered=[stem.stem(w) for w in word_list if (w not in stopword)]
#             new_doc.append(filtered)
#         new_dict[key]=new_doc
#     # print(str(i)+'hah')
#     return new_dict

# if __name__=="__main__":
#     docu_base='../../data/collections/'
#     doc_dirs={docu_base+'english/GH95/':extract_english_gh95,docu_base+'english/LATimes94/':extract_english_latimes}
#     query_base='../../data/query/'
#     query_dir=query_base+'Top-it03.txt'
#     queries_dirs=[query_dir,['it','italian']]
#     docs=tf(doc_dirs)
#     queries=tf(queries_dirs)
#     docs_dict=docs.docs_dict
#     # print(len(docs_dict.items()))
#     # sys.exit(0)

#     new_dict={}
#     length=len(docs_dict.keys())
#     # i=0
#     # index=0
#     # ap={}
#     start=time.time()
#     doc_list=list(docs_dict.items())
#     nan_docs=['LA091794-0059','LA030494-0028','LA070794-0146','LA092294-0013','LA091194-0065']
#     for key,value in docs_dict.items():
#         if key in nan_docs:
#             print(value)
#     sys.exit(0)

#     # for key,value in docs_dict.items():
#     #     # print(key)
#     #     # print(ps.cut_text(value))
#     #     # sys.exit(0)
#     #     i+=1
#     #     new_dict[key]=value
#     #     if i%100==0 or i==length:
#     #         ap[index]=copy.copy(new_dict)
#     #         new_dict.clear()
#     #         index+=1
#     #         if index==10:
#     #             end=time.time()
#     #             print(end-start)
#     #             break
#     #             # sys.exit(0)
#     p=Pool(4)
#     results=[]
#     arg=[]
#     for i in range(170):
#         if i==169:
#             docs=doc_list[1000*i:length]
#         else:
#             docs=doc_list[1000*i:1000*(i+1)]
#         arg.append(docs)
#         # result=cut(docs,i)
#         # result=p.map(cut,args=(docs,i,),)
#         # result=p.map(cut,[docs,i])
#         # results.append(result.get())
#         # end=time.time()
#         # print(end-start)
#     result=p.map(cut,arg)
#     p.close()
#     p.join()
#     # print(results)
#     np.save('doc_list.npy',result)
#     # while True:
#     #     results=quene.get()
#     #     if quene.empty():
#     #         break
import random
import numpy as np
# a=[]
# b=[1,2,3]
# for i in range(3):
#     print(b[i])
# # if a==Null:
#     # print('1')
# if len(a)<1 or len(b)<1:
#     print('enb')
# print(len(a))
# random.shuffle(b)
# print(b)
# a=np.load('sum_new_negative_result/1.npy').item()
# print(a)
# new={}
# for key,value in a.items():
#     b=[]
#     #单个查询下的所有文档中的句子得分。
#     for nc in value:
#         #单个文档中所有句子得分，nc此时对应一个字典
#         for m,n in nc.items():
#             b.append((m,np.mean(n)))
#     new[key]=b
# np.save('sum_new_negative_result/2.npy',new)
# a={1:2,2:4,3:6}
# for key,value in a.items():
#     value=value/2
# print(a)
# a=np.load('tbtqt_docs_id.npy')
# print(len(a))
# tmp_ranked_documents=['ss','ee','gg']
# doc_rank = {d_id: r for r, d_id in enumerate(tmp_ranked_documents, 1)}
# print(doc_rank)
# ensemble_scores=[(1,'ss'),(3,'gg'),(2,'hh')]
# ranking_with_doc_ids = sorted(ensemble_scores, key=lambda v: (v[0], random.random()))
# print(ranking_with_doc_ids)
# def normal(f_dict):
#     pw = sorted(f_dict.items(),key=lambda tb_dict:tb_dict[1],reverse=True)
#     length=len(pw)
#     max=pw[0][1]
#     min=pw[length-1][1]
#     num=max-min
#     new_dict={}
#     for key,value in pw:
#         score=(value-min)/num
#         new_dict[key]=score
#     return new_dict
# aa={1:2,2:4,3:3}
# res=sorted(aa.items(),key=lambda scores_dict:scores_dict[1],reverse=True)
# print(normal(aa))
import os
k=1
os.mkdir('res'+str(k))
