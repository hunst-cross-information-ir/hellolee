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
# print(rev_assess)
length=len(rev_assess.keys())
count=0
for value in rev_assess.values():
    if len(value)==0:
        count+=1

pre_results={}
with open('xiang_guan/doc_score.txt','r',encoding='utf-8') as cf:
# with open('xiang_guan/doc_score.txt','r',encoding='utf-8') as cf:
    lines=cf.readlines()
    for line in lines:
        line=line.strip().split()
        if line[0] not in pre_results.keys():
            pre_results[line[0]]=[line[1]]
        else:
            pre_results[line[0]].append(line[1])

# docs=np.load('id_docs.npy').item()['141']

all_sum=0
for query in rev_assess.keys():
    sum=0
    nums=0
    if query in pre_results.keys():
        for i,doc in enumerate(pre_results[query]):
            if doc in rev_assess[query]:
                map=float((nums+1)/(i+1))
                sum+=map
                nums+=1           
        if nums!=0:
            sum=sum/nums
    all_sum+=sum

print(all_sum/(length-count))





