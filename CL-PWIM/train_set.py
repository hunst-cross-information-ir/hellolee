from data_process import process as ps
import copy
from random import randint
import random
class Get_trainset(object):
    def __init__(self,path1,path2,lang1,lang2):
        self.left=self.read_sent(path1,lang1)
        self.right=self.read_sent(path2,lang2)
        self.labels=[]
    def read_sent(self,path,lang):
        sents=[]
        with open(path,'r',encoding='utf-8') as rf:
            lines=rf.readlines()
            for i,line in enumerate(lines):
                sent=ps.handle_sen(line.strip(),lang)
                sents.append(sent)
                if i==50:
                    break
        return sents
    def filter_sents(self):
        for i in range(len(self.left)):
            if len(self.left[i])<1 or len(self.right[i])<1:
                del(self.left[i])
                del(self.right[i])
    def sample_negative(self):
        length=len(self.left)
        a=copy.copy(self.left)
        b=copy.copy(self.right)
        print(len(a))
        print(len(b))
        #c,d用于存储负样例
        c=[]
        d=[]
        signals=[]
        for i,sent in enumerate(a):
            self.labels.append([1])
            #随机生成10个整数
            for j in range(10):
                num=randint(0,length-1)
                signals.append([0])
                d.append(b[num])
                c.append(a[i])
        self.left.extend(c)
        self.right.extend(d)
        self.labels.extend(signals)
    def shuffle(self):
        lengths=len(self.left)
        index=[]
        for i in range(lengths):
            index.append(i)
        random.shuffle(index)
        new_left=[]
        new_right=[]
        new_labels=[]
        for j in index:
            new_left.append(self.left[j])
            new_right.append(self.right[j])
            new_labels.append(self.labels[j])
        data=(new_left,new_right,new_labels)
        return data




        






