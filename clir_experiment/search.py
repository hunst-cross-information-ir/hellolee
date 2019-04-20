from whoosh.index import *
from whoosh.qparser import QueryParser,OrGroup,SimpleParser
from whoosh.scoring import *
from whoosh.searching import Results
from whoosh import scoring
import sys
import gensim
from gensim.models import Word2Vec
from WeightingModel import WEvs,LM

#查询文件地址，输出文件地址，索引地址
def query(querydir,outdir,indexdir):
    index=open_dir(indexdir)
    #加载已经训练好的词向量模型
    # model=Word2Vec.load('F:/CLEF2003/we-vs/size300-wiki/we_vs1.model')
    # print(model['tv'])
    # sys.exit(0)
    query_items={}
    with open(querydir,'r',encoding='utf-8') as pf:
        lines=pf.readlines()
        i=0
        for line in lines:
            if i%2==0:
                query_id=line[4:len(line)-6]
            else:
                query=line[7:len(line)-10]
                query_items[query_id]=query
            i=i+1
    #weighting=scoring.Frequency
    #weighting=scoring.DFree()
    #
    # with open("F:/CLEF2003/result/bilingual/en-nl/pysize600-1.txt",'w',encoding='utf-8') as wf:
    #
    with open(outdir,'w',encoding='utf-8') as wf:
        with index.searcher(weighting=WEvs()) as searcher:
            parser=QueryParser("content",schema=index.schema,group=OrGroup)
            #
            # parser=SimpleParser("content",index.schema)
            for query in query_items.items():

                myquery=parser.parse(query[1])

                print(myquery)

                results=searcher.search(myquery,limit=None)

                # sys.exit(0)
                i=1

                for result in results:
                    wf.write(query[0]+' Q0 '+result['id']+' '+str(i)+' '+str(results.score(i-1))+' LM\n')
                    i+=1
                    if i==1001:
                        break

# query('F:/CLEF2003/query/modutch_query-2003.xml',"F:/CLEF2003/result/monolingual/nl/pysize600.txt","../../index/index_nl/index")
query('F:/CLEF2003/query/moenglish_query-2003.xml',"F:/CLEF2003/result/monolingual/en/pysize600.txt","../../index/index_en/index")

