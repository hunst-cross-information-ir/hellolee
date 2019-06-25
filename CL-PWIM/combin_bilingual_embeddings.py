path1='../../data/bilingual embeddings/supervised-it/vectors-en.txt'
path2='../../data/bilingual embeddings/supervised-it/vectors-it.txt'
with open('fasttext.txt','w',encoding='utf-8') as wf:
    with open(path1,'r',encoding='utf-8') as rf:
        lines=rf.readlines()
        for line in lines[1:]:
            wf.write(line)
    with open(path2,'r',encoding='utf-8') as pf:
        lines=pf.readlines()
        for line in lines[1:]:
            wf.write(line)