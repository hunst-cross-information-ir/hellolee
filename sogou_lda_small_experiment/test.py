import os
import jieba
from gensim import corpora,models,similarities
from gensim.models import LdaModel
import sys

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
	filename=get_allfiles('./test collection/')
	corpus_all=[]
	for file in filename:
		with open(file,'r',encoding='gb18030',errors='ignore') as rf:
			texts=rf.read().strip()
			item=[]
			for word in jieba.cut(texts):
				if word not in b:
					item.append(word)
			corpus_all.append(item)

	dictionary=corpora.Dictionary.load('sougou_lda.dict')          #加载训练集词典


	corpus=[dictionary.doc2bow(text) for text in corpus_all]        #将文档中词转变成词典中序号
	#lda = models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=9)
	# lda.save('sogou_lda.model')
	# topic_list=lda.print_topics(-1)
	# for topic in topic_list:
	# 	print(topic)
	# # print(corpus_all)
	lda=LdaModel.load('sogou_lda.model')          #加载训练好的模型

	vector=lda[corpus]                    #利用已经训练好的LDA预测新的文档


	c=[]
	for item in vector:
		max_topic=item[0][0]
		max_pass=item[0][1]
		for i in range(len(item)):
			if item[i][1]>max_pass:
				max_topic=item[i][0]
				max_pass=item[i][1]
		c.append(max_topic)

	for j in range(9):
		print(c[j*10:j*10+9])



