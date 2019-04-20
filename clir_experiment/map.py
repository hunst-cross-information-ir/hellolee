import os


#读取标准文件
access_dir='F:/CLEF2003/relaccess/qrels_EN'
file_relevant={}
a=set()
file_unrelevant={}
with open(access_dir,'r',encoding='utf-8') as rf:
    lines=rf.readlines()
    for line in lines:
        line=line.strip('\n')
        line_sp=line.split()
        if line_sp[3]=='1':
            if line_sp[0] in file_relevant.keys():
                file_relevant[line_sp[0]].append(line_sp[2])
            else:
                file_relevant[line_sp[0]]=[line_sp[2]]
# print(file_relevant)
print(file_relevant.keys())
#测试集为荷兰语时，查询不需要包括160，166，191，194
#测试集为英文时，查询不需要包括149,161,166,186,191,195

def evolution(file,file_relevant):
    with open(file,'r',encoding='utf-8') as pf:
        lines=pf.readlines()
        sum=0
        avg=0
        count=0
        query_id='141'
        for line in lines:
            line=line.strip('\n')
            line_sp=line.split()
            if query_id!=line_sp[0]:
                if count!=0:
                    avg=avg+sum/count
                sum=0
                count=0
            query_id=line_sp[0]
            if line_sp[0] not in file_relevant.keys():
                continue
            else:
                if line_sp[2] in file_relevant[line_sp[0]]:
                    count=count+1
                    sum=sum+count/int(line_sp[3])
        avg=avg/len(file_relevant.keys())
    return avg


#读取评测文件
evolution_dir='F:/CLEF2003/result/monolingual/en/'
# evolution_dir='F:/CLEF2003/result/bilingual/nl-en/'

filelist=os.listdir(evolution_dir)
for file in filelist:
    score=evolution(evolution_dir+file,file_relevant)
    print(file+' '+str(score))

