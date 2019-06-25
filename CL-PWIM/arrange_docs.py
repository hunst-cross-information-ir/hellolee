from data_process import process as ps
import codecs
from lxml import html as etree
import os
import sys
import time
from multiprocessing import Pool
from nltk.corpus import stopwords

class transform(object):
    def __init__(self,doc_dirs):
        self.docs_dict={}
        self.get_all(doc_dirs)
    def _decode_xml(self,path):
        with codecs.open(path, encoding='ISO-8859-1') as f:
            xml = f.read()
            xml = xml.replace("<BODY>", "<BODYY>").replace("</BODY>", "</BODYY>")
            xml = xml.replace("<HEAD>", "<HEADD>").replace("</HEAD>", "</HEADD>")
        xml = "<root>" + xml + "</root>"
        return etree.fromstring(xml)
    def doc_dm(self,path, extractor, limit=None):
        tree = self._decode_xml(path)
        st=time.time()
        for i, doc in enumerate(list(tree)):
            document_id, full_text = extractor(doc)
            # sents=ps.cut_text(full_text)
            # new_doc=[]
            # for sen in sents:
            #     filters=ps.handle_sen(sen,'english')
            #     new_doc.append(filters)
            self.docs_dict[document_id.strip()]=full_text.strip()
    # def process_docs(self):
    #     new_dict={}
    #     for id,doc in self.docs_dict.items():
    #         sents=ps.cut_text(doc)
    #         new_doc=[]
    #         for sen in sents:
    #             filters=ps.handle_sen(sen,'english')
    #             new_doc.append(filters)
    #         new_dict[id]=new_doc
    #     return new_dict
    def load_queries(self,path, language, limit=None):
        language_tag=language[0]
        tag_title = language_tag + '-title'
        tag_desc = language_tag + '-desc'
        # tag_narr = language_tag + '-narr'
        tree = self._decode_xml(path)
        # queries = []
        # ids = []
        stop=stopwords.words(language[1])
        for i, topic in enumerate(list(tree)):
            _id = topic.findtext('num').strip() # e.g. 'C041'
            _id = int(_id[1:]) # e.g. 41
            title = topic.findtext(tag_title)
            desc = topic.findtext(tag_desc)
            query = ' '.join([title, desc])
            query=ps.handle_query(query.strip(),stop)
            # queries.append(clean(query))
            self.docs_dict[_id]=query
            # queries.append(query)
            # ids.append(_id)
            # if i == limit:
            #     break
        # return ids, queries
    def get_all(self,doc_dirs):
        if isinstance(doc_dirs,list):
            self.load_queries(doc_dirs[0],doc_dirs[1])
        else:
            for doc_dir, extractor in doc_dirs.items():
                # if 'GH' in doc_dir:
                #     continue
                # else:
                for file in next(os.walk(doc_dir))[2]:
                    self.doc_dm(doc_dir + file, extractor)
                # documents.extend(tmp_documents)
                # doc_ids.extend(tmp_doc_ids)


