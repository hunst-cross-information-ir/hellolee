import os
import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
import nltk
import sys
# language='nl'
# dir='F:/CLEF2003/test collection/NL-data/'
#自定义数据处理类

class data_process(object):
    def __init__(self,language):
        if language=='mix':
            eng_stop=stopwords.words('english')
            sr=stopwords.words('dutch')
            sr.extend(eng_stop)
        else:
            sr=stopwords.words(language)
        #在停用词表中加入标点
        # sr.extend([',','.','(',')',"'",'?',':',"''",';','!','...',"``",'-','/'])
        self.sr=sr
        #词干还原器
        self.s=nltk.PorterStemmer()
        self.lang=language
        # self.dir=indir
        self.files=[]

#适用于获取文件夹下所有可读取文件，包括子目录中文件
    def getAllfile(self,indir):
        folder=os.listdir(indir)
        for folder_item in folder:
            if os.path.isfile(indir+folder_item):
                self.files.append(indir+folder_item)
            else:
                self.getAllfile(indir+folder_item+'/')

    def getFiles(self,indir):
        files=os.listdir(indir)
        for file in files:
            if '.gz' not in file:
                self.files.append(indir+file)
#通过正则表达式移除html标签,类似<p>aaa</p>,调用此方法可以直接得到标签里面内容aaa
    def remove_html(self,text):
        dr = re.compile(r'<[^>]+>',re.S)
        dd = dr.sub('',text)
        return dd
#提取词干
    def stem_text(self,text):
        cc=[]
        #先对文本分句子
        sents=sent_tokenize(text)
        for sen in sents:
            #对句子分词
            words=word_tokenize(sen)
            for word in words:
                #去停用词
                if word not in self.sr:
                    #小写加上词干提取
                    cc.append(self.s.stem(word).lower())
        return cc
#荷兰语测试集处理
    def NL_pre_process(self,outdir):
        with open(outdir,'w',encoding='utf-8') as wf:
            for file in self.files:
                with open(file,'r',encoding='ISO-8859-1') as rf:
                    lines=rf.readlines()
                    for line in lines:
                        if '<DOCNO>' in line:
                            id=line[7:len(line)-9]
                            #只提取body部分
                        # elif '<BODY>' in line:
                        #     text=''
                        # elif '<P>' in line:
                        #     line=self.remove_html(line.strip('\n'))
                        #     if len(line.split())<1:
                        #         continue
                        #     else:
                        #         text=text+' '+' '.join(self.stem_text(line))
                        # elif '</BODY>' in line:
                        #     wf.write('<DOC>\n')
                        #     wf.write('<DOCNO>'+id+'</DOCNO>\n')
                        #     wf.write('<TEXT>'+text+'</TEXT>\n')
                        #     wf.write('</DOC>\n')
                        # else:
                        #     continue
                        elif '<DOCID>' in line:
                            continue
                        elif '<HEAD>' in line:
                            text=''
                        elif '</DOC>' in line:
                            wf.write('<DOC>\n')
                            wf.write('<DOCNO>'+id+'</DOCNO>\n')
                            wf.write('<TEXT>'+text.strip()+'</TEXT>\n')
                            wf.write('</DOC>\n')
                        else:
                            line=self.remove_html(line.strip('\n'))
                            if len(line.split())<1:
                                continue
                            else:
                                text=text+' '+' '.join(self.stem_text(line))
 #英文数据集gh处理                               
    def GH_pre_process(self,outdir):
        with open(outdir,'w',encoding='utf-8') as wf:
            for file in self.files:
                with open(file,'r',encoding='ISO-8859-1') as rf:
                    lines=rf.readlines()
                    for line in lines:
                        if '<DOCNO>' in line:
                            id=line[7:len(line)-9]
                            text=''
                        elif '<HEADLINE>' in line:
                            line=self.remove_html(line.strip('\n'))
                            text=text+' '+' '.join(self.stem_text(line))
                        elif '<' not in line:
                            text=text+' '+' '.join(self.stem_text(line.strip('\n')))
                        elif '</DOC>' in line:
                            wf.write('<DOC>\n')
                            wf.write('<DOCNO>'+id+'</DOCNO>\n')
                            wf.write('<TEXT>'+text.strip()+'</TEXT>\n')
                            wf.write('</DOC>\n')
                        else:
                            continue
#英文数据集LA处理
    def LA_pre_process(self,outdir):
        with open(outdir,'a',encoding='utf-8') as wf:
            for file in self.files:
                with open(file,'r',encoding='ISO-8859-1') as rf:
                    lines=rf.readlines()
                    check=0
                    for line in lines:
                        if '<DOCNO>' in line:
                            id=line[8:len(line)-10]
                            text=''
                        elif '<' not in line:
                            if check==0:
                                continue
                            else:
                                text=text+' '+' '.join(self.stem_text(line.strip('\n')))
                        elif '<TEXT>' in line:
                            check=1
                        elif '<HEADLINE>' in line:
                            check=1
                        elif '</HEADLINE>' in line:
                            check=0
                        elif '</TEXT>' in line:
                            check=0
                        elif '</DOC>' in line:
                            if text=='':
                                continue
                            else:
                                wf.write('<DOC>\n')
                                wf.write('<DOCNO>'+id+'</DOCNO>\n')
                                wf.write('<TEXT>'+text.strip()+'</TEXT>\n')
                                wf.write('</DOC>\n')
                        else:
                            continue
#训练集处理
    def trainData_process(self,outdir):
        i=0
        for file in self.files: 
            print(i)
            with open(outdir+str(i)+'.txt','w',encoding='utf-8') as wf:
                with open(file,'r',encoding='utf-8') as rf:
                    text=rf.read()
                    sentences=sent_tokenize(text)
                    for sen in sentences:
                        words=word_tokenize(sen)
                        for word in words:
                            if word not in self.sr:
                                wf.write(word+'\n')
            i+=1

#当该文件直接运行，执行下面操作
#当该文件以模块的形式导入到其他文件，则下面的代码不运行
if __name__=='__main__':
    #处理完成后输出的文件
    outdir='F:/CLEF2003/train data/traindata/'
    # outdir='../test collection/process_data/EN_test_collection.txt'
    #确认处理英文还是荷兰语
    # a=data_process('dutch')
    a=data_process('mix')
    # a.getAllfile('F:/CLEF2003/test collection/NL-data/')
    #英文测试集步骤是先处理gh
    #再处理LA
    # a.getAllfile('F:/CLEF2003/first test collection/English_data/GlasgowHerald95/GH95/')
    # a.getAllfile('F:/CLEF2003/first test collection/English_data/LATimes94/')
    # a.getFiles('F:/CLEF2003/first test collection/English_data/LATimes94/')
    a.getFiles('F:/corpus/wikiepENDU/AllENDU/ENDU/')


    # print(a.files)
    # a.files=['test2.txt']
    # a.LA_pre_process(outdir)
    a.trainData_process(outdir)











