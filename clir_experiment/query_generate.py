from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
import nltk
import os

#当处理英文文本，加载英文停用词，当处理其他语言文本加载其他语言停用词
# sr=stopwords.words("english")

#在停用词表中加入标点
# sr.extend([',','.','(',')',"'",'?',':',"``",';','!','...'])
# s=nltk.stem.SnowballStemmer('dutch')

def stem(text,sr,porter):
    words=word_tokenize(text)
    cc=[]
    for word in words:
        if word not in sr:
            cc.append(porter.stem(word).lower())
    return ' '.join(cc)+'\n'

#存储需要移除的查询
#由于评估文档中会有查询没有相关文档的情况，因此对应的查询需要剔除    
en_query_remove=[149,161,166,186,191,195]
nl_query_remove=[160,166,191,194]

#读取荷兰语的topic
def get_query(indir,outdir,query_language,test_language):
    porter=nltk.PorterStemmer()
    sr=stopwords.words(query_language)
    if test_language=='english':
        query_remove=en_query_remove
    else:
        query_remove=nl_query_remove
    with open(indir,'r',encoding='ISO-8859-1') as rf:
        with open(outdir,'w',encoding='utf-8') as wf:
            text=''
            lines=rf.readlines()
            remove=0
            if query_language=='english':
                for line in lines:
                    if '<num>' in line:
                        query_id=line[7:len(line)-8]
                        if int(query_id) in query_remove:
                            remove=1
                    elif '<EN-title>' in line:
                        print(line)
                        text=text+line[11:len(line)-12]
                    elif '<EN-desc>' in line:
                        text=text+line[10:len(line)-12]
                    elif '</top>' in line:
                        if remove!=1:
                            print(text)
                            text=stem(text,sr,porter)
                            wf.write('<id>'+query_id+'</id>\n')
                            wf.write('<query>'+text.strip('\n')+'</query>\n')
                        text=''
                        remove=0
            else:
                for line in lines:
                    if '<num>' in line:
                        query_id=line[7:len(line)-8]
                        if int(query_id) in query_remove:
                            remove=1
                    elif '<NL-title>' in line:
                        text=text+line[11:len(line)-12]
                    elif '<NL-desc>' in line:
                        text=text+line[10:len(line)-12]
                    elif '</top>' in line:
                        if remove!=1:
                            text=stem(text,sr,porter)
                            wf.write('<id>'+query_id+'</id>\n')
                            wf.write('<query>'+text.strip('\n')+'</query>\n')
                        text=''
                        remove=0
get_query('Top-en03.txt','english_query-2003.xml','english','english')
