import os
import jieba
from gensim import corpora,models,similarities
import sys
# import pyltp
# from pyltp import SentenceSplitter
# from pyltp import Segmentor
def get_allfiles(filedir):
	# for root,dirs,files in os.walk(filedir):
	# 	print()
	a=[]
	for file in os.listdir(filedir):
		a.append(filedir+file)
	b=[]
	for fi in a:
		for filename in os.listdir(fi):
			b.append(fi+'/'+filename)
	return b

def load_stopwords(filename):
	with open('chinese_stopwords.txt','r') as rf:
		lines=rf.readlines()
		a=['\n',' ','\u3000','\x00','nbsp','\t']
		for line in lines:
			a.append(line.strip())
	return a


if __name__=="__main__":
	b=load_stopwords('hello')
	i=0
	filename=get_allfiles('./training corpus/SogouC.reduced/Reduced/')
	corpus_all=[]
	for file in filename:
		# if i==10:
		# 	break
		with open(file,'r',encoding='gb18030',errors='ignore') as rf:
			texts=rf.read().strip()
			# i+=1
			item=[]
			for word in jieba.cut(texts):
				if word not in b:
					item.append(word)
			corpus_all.append(item)
	dictionary=corpora.Dictionary(corpus_all)

	corpus=[dictionary.doc2bow(text) for text in corpus_all]
	lda = models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=9)
	lda.save('sogou_lda.model')
	# topic_list=lda.print_topics(-1)
	# for topic in topic_list:
	# 	print(topic)
	# # print(corpus_all)

