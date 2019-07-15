import numpy as np
import os
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
length=len(rev_assess.keys())
count=0
for value in rev_assess.values():
    if len(value)==0:
        count+=1

dir='result-0.5/'
dict_all={}
filelist=os.listdir(dir)
for file in filelist:
    pre_results={}
    with open(dir+file,'r',encoding='utf-8') as cf:
        lines=cf.readlines()
        for line in lines:
            line=line.strip().split()
            if line[0] not in pre_results.keys():
                pre_results[line[0]]=[line[1]]
            else:
                pre_results[line[0]].append(line[1])

    # docs=np.load('id_docs.npy').item()['141']

    # all_sum=0
    # for query in rev_assess.keys():
    #     sum=0
    #     nums=0
    #     for doc in rev_assess[query]:
    #         if doc in pre_results[query]:
    #             index=pre_results[query].index(doc)
    #             print(index)
    #             map=float((nums+1)/(index+1))
    #             sum+=map
    #             nums+=1
    #     if nums!=0:
    #         sum=sum/nums
    #     all_sum+=sum
    # sp=all_sum/(length-count)
    # dict_all[file]=sp
    # print(all_sum/(length-count))

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
        sp=all_sum/(length-count)
        dict_all[file]=sp

res = sorted(dict_all.items(),key=lambda dict_all:dict_all[1],reverse=True)
print(res[0:10])




