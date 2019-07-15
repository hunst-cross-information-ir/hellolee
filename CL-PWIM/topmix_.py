import numpy as np
import sys
import os
#加载TbTQT方法的文档得分、文档id和文档名字
sum_scores=np.load('xiang_guan/tbtqt_sc.npy')
sum_ids=np.load('xiang_guan/tbtqt_scores.npy')
id_docs=np.load('xiang_guan/tbtqt_docs_id.npy')
# print(sum_scores[0][0:10])
# print(sum_ids[0][0:10])
# print(id_docs[0:10])
# # print(len(sum_ids[0]))
# sys.exit(0)
scores=np.load('tbtqt_negative_result/1.npy').item()
# print(scores)

# print(len(scores.keys()))
# sys.exit(0)
pp=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
wx=[]
for k in range(11):
    for i in range(11):
        for j in range(11):
            hp=[pp[k],pp[i],pp[j]]
            wx.append(hp)
# wx=[1,0.,0.3]
# sb=10
#得到赋权重之后的得分
def resort(cc,w):
    cc.sort(reverse=True)
    score=0
    count=0
    for i,new in enumerate(cc):
        # score+=w*cc[i]
        count+=1
        score+=new*w[i]
        if len(w)==i+1:
            break
    # score=score/count
    return score
#归一化
def normal(f_dict):
    pw = sorted(f_dict.items(),key=lambda tb_dict:tb_dict[1],reverse=True)
    length=len(pw)
    max=pw[0][1]
    min=pw[length-1][1]
    num=max-min
    new_dict={}
    for key,value in pw:
        score=(value-min)/num
        new_dict[key]=score
    return new_dict

# k=0.5
for k in pp:
    os.mkdir('result-'+str(k))
    for w in wx:
        pg=0
        sign=141
        new_dict={}
        mik=str(w[0])+'-'+str(w[1])+'-'+str(w[2])
        for query in scores.keys():
            sum_dict={}
            scores_dict={}
            #加载TBTQT方法的相关文档得分
            j=int(query)-sign
            # print(len(sum_ids[j]))
            docs=sum_ids[j][0:100]
            # h=[]
            for i,id in enumerate(docs):
                doc=id_docs[id]
                # h.append(doc)
                sum_dict[doc]=sum_scores[pg][id]
            # print(sum_dict['AGZ.950609.0067'])
            # sys.exit(0)
            #加载我们提出的方法的相关文档得分
            # print(h[0:100])   
            # for it in scores[query]:
            #     for key,value in it.items():
            #         if not key in h[0:100]:
            #             print('enen')
            # print(len(scores[query]))
            # sys.exit(0)
            # print(h[0:100])
            # sys.exit(0)
            new_sum=normal(sum_dict)
            tb_dict={}
            # cw={}
            for zz in scores[query]:
                for key,value in zz.items():
                    sc=resort(value,w)
                    tb_dict[key]=k*sc+(1-k)*new_sum[key]
            # pw = sorted(tb_dict.items(),key=lambda tb_dict:tb_dict[1],reverse=True)
            # i=1
            # for key,value in pw:
            #     i+=1
            #     scores_dict[key]=k*sc+(1-k)*new_sum[key]
            res = sorted(tb_dict.items(),key=lambda scores_dict:scores_dict[1],reverse=True)
            new_dict[query]=res
            pg+=1
            # j+=1
            # print(new_dict)
        with open('result-'+str(k)+'/'+mik+'doc_score.txt','w',encoding='utf-8') as wf:
            for q,docs in new_dict.items():
                for doc,score in docs:
                    wf.write(str(q)+' '+doc+' '+str(score)+'\n')



