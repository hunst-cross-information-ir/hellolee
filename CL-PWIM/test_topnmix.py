import numpy as np
import sys
#加载sum方法的文档得分、文档id和文档名字
sum_scores=np.load('xiang_guan/sum_scores.npy')
sum_ids=np.load('xiang_guan/sum_ids.npy')
id_docs=np.load('xiang_guan/doc_ids.npy')
# print(len(sum_ids[0]))
# sys.exit(0)
scores=np.load('sum_new_negative_result/1.npy').item()
new_dict={}
# print(scores.keys())
# sys.exit(0)
pp=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
wx=[]
for k in range(11):
    # for i in range(11):
    #     for j in range(11):
    hp=[1,1,0.5,pp[k]]
    wx.append(hp)
# wx=[1,0.,0.3]
def resort(cc,pw):
    cc.sort(reverse=True)
    score=0
    print(cc)
    print(pw)
    for i,w in enumerate(pw):
        score+=w*cc[i]
        if (i+1)==len(cc):
            break
    return score

k=1.0
sign=141
for pw in wx:
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
        # print(scores[query])
        for zz in scores[query]:
            for key,value in zz.items():
                # print(value)
                sc=resort(value,pw)
                scores_dict[key]=k*sc+(1-k)*sum_dict[key]
        res = sorted(scores_dict.items(),key=lambda scores_dict:scores_dict[1],reverse=True)
        new_dict[query]=res
        j+=1
    # print(new_dict)
    with open('4test_topn/doc_score'+str(pw[3])+'.txt','w',encoding='utf-8') as wf:
        for q,docs in new_dict.items():
            for doc,score in docs:
                wf.write(str(q)+' '+doc+' '+str(score)+'\n')



