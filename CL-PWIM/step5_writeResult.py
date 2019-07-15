import numpy as np
import sys
scores=np.load('result/1.npy').item()
new_dict={}
for query in scores.keys():
    scores_dict={}
    for key,value in scores[query]:
        scores_dict[key]=value
    res = sorted(scores_dict.items(),key=lambda scores_dict:scores_dict[1],reverse=True)
    new_dict[query]=res
# print(new_dict)
with open('results/doc_score.txt','w',encoding='utf-8') as wf:
    for q,docs in new_dict.items():
        for doc,score in docs:
            wf.write(str(q)+' '+doc+' '+str(score)+'\n')
