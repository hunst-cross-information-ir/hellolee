import gensim
from gensim.models import word2vec
import os
import random
import sys

SIZE=300
WINDOW=60
outdir='F:/CLEF2003/we-vs_new/size300/'

#直接利用别人已经分词和词干提取的文档来训练
def main():
#由于二者文件名一致，所以只需要获取其中一个文件夹中文件名即可
    dir='F:/corpus/wikiepENDU/AllENDU/Stemmed/'
    en_dir=dir+'EN/'
    nl_dir=dir+'DU/'
    en_filename=os.listdir(en_dir)
    nl_filename=os.listdir(nl_dir)
    sentences=[]
    for file in en_filename:
        print(file)
        with open(en_dir+file,'r',encoding='utf-8') as rf:
            lines=rf.readlines()
            text=[]
            for line in lines:
                # print(line)
                text.append(line.strip('\n'))
        with open(nl_dir+file,'r',encoding='utf-8') as pf:
            lines=pf.readlines()
            for line in lines:
                text.append(line.strip('\n'))
        sentences.append(text)
        # print(sentences)
        # sys.exit(0)
    return sentences

#利用我们自己分词和词干化的文档来训练
def another():
    indir='F:/CLEF2003/train data/traindata/'
    filelist=os.listdir(indir)
    sentences=[]
    for file in filelist:
        with open(indir+file,'r',encoding='utf-8') as rf:
            text=[]
            lines=rf.readlines()
            for line in lines:
                text.append(line.strip('\n'))
            sentences.append(text)
    return sentences

sentences=main()
# sentences=another()
for i in range(10):
    for sen in sentences:
        random.shuffle(sen)
    model=word2vec.Word2Vec(sentences, size=SIZE,window=WINDOW)

    model.save(outdir+'we_vs'+str(i)+'.model')


