import numpy as np
import sys
#加载sum方法的文档得分、文档id和文档名字
sum_scores=np.load('xiang_guan/sum_scores.npy')
sum_ids=np.load('xiang_guan/sum_ids.npy')
id_docs=np.load('xiang_guan/doc_ids.npy')
# print(len(sum_ids[0]))
# sys.exit(0)
scores=np.load('sum_new_negative_result/2.npy').item()
new_dict={}
# print(scores.keys())
# sys.exit(0)
k=0
sign=141
for query in scores.keys():
    sum_dict={}
    scores_dict={}
    #加载IDF方法的相关文档得分
    j=int(query)-sign
    docs=sum_ids[j]
    for i,id in enumerate(docs):
        doc=id_docs[id]
        sum_dict[doc]=sum_scores[j][i]
    #加载我们提出的方法的相关文档得分
    for key,value in scores[query]:
        scores_dict[key]=k*value+(1-k)*sum_dict[key]
    res = sorted(scores_dict.items(),key=lambda scores_dict:scores_dict[1],reverse=True)
    new_dict[query]=res
    j+=1
# print(new_dict)
with open('xiang_guan/doc_score.txt','w',encoding='utf-8') as wf:
    for q,docs in new_dict.items():
        for doc,score in docs:
            wf.write(str(q)+' '+doc+' '+str(score)+'\n')



