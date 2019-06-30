import numpy as np
scores=np.load('results/141_doc_score-test.npy')
scores_dict={}
for key,value in scores:
    scores_dict[key]=value
res = sorted(scores_dict.items(),key=lambda scores_dict:scores_dict[1],reverse=True)
with open('results/141_doc_score.txt','w',encoding='utf-8') as wf:
    for key,value in res:
        wf.write('141 '+key+' '+value+'\n')
