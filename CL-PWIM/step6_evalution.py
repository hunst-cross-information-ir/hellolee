import numpy as np

eva_dir='../data/RelAssess/2003/qrels_italian'
rev_assess={}
with open(eva_dir,'r',encoding='utf-8') as rf:
    lines=rf.readlines()
    for line in lines:
        line=line.strip().split()
        assess=line[3]
        query_id=line[0]
        sign=0
        if query_id not in rev_assess.keys():
            rev_assess[query_id]=[]
        if int(assess)==1:
            rev_assess[query_id].append(line[2])
print(rev_assess)


docs=[]
with open('results/141_doc_score.txt','r',encoding='utf-8') as cf:
    lines=cf.readlines()
    for line in lines:
        line=line.strip().split()
        docs.append(line[1])

# docs=np.load('id_docs.npy').item()['141']
sum=0
for doc in rev_assess['141']:
    if doc in docs:
        index=docs.index(doc)
        print(index)
        map=float(1/(index+1))
        sum+=map
print(sum)





