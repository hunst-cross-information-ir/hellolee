from whoosh.fields import Schema,STORED,ID,KEYWORD,TEXT
import os.path
from whoosh.index import create_in
from whoosh.query import *
import sys

data_dir='F:/CLEF2003/test collection/process_data/EN_test_collection2.txt'

schema=Schema(id=ID(stored=True),content=TEXT(stored=True))

#检测路径下是否存在index目录
if not os.path.exists("index"):
    os.mkdir("index")
ix=create_in("index",schema)
writer=ix.writer()

#读取要索引的内容
with open(data_dir,'r',encoding='utf-8') as rf:
    lines=rf.readlines()
    one_text=''
    for line in lines:
        if line.find('<DOCNO>')>-1:
            fileid=line[7:len(line)-9]
        if line.find('<TEXT>')>-1:
            one_text=line[6:len(line)-8]
        if line.find('</DOC>')>-1:
            text_sp=one_text.split()
            if len(text_sp)==0:                                    #过滤掉文本内容为空的文档
                continue
            writer.add_document(id=fileid,content=one_text)        #写入索引
#提交
writer.commit()

