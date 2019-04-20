import torch
from torch import nn
from torch.autograd import Variable
'''
官方说明
class torch.nn.Embedding(num_embeddings, embedding_dim, padding_idx=None, max_norm=None, norm_type=2, scale_grad_by_freq=False, sparse=False)
一个保存了固定字典和大小的简单查找表。
这个模块常用来保存词嵌入和用下标检索它们。模块的输入是一个下标的列表，输出是对应的词嵌入。
参数
num_embeddings (int) - 嵌入字典的大小
embedding_dim (int) - 每个嵌入向量的大小
padding_idx (int, optional) - 如果提供的话，输出遇到此下标时用零填充
max_norm (float, optional) - 如果提供的话，会重新归一化词嵌入，使它们的范数小于提供的值
norm_type (float, optional) - 对于max_norm选项计算p范数时的p
scale_grad_by_freq (boolean, optional) - 如果提供的话，会根据字典中单词频率缩放梯度

变量
weight (Tensor) -形状为(num_embeddings, embedding_dim)的模块中可学习的权值

形状
输入： LongTensor (N, W), N = mini-batch, W = 每个mini-batch中提取的下标数
输出： (N, W, embedding_dim)

'''
embedding=nn.Embedding(10,3)
print(embedding.weight)
input=Variable(torch.LongTensor([[1,2,4,5],[4,3,2,9]]))
print(embedding(input))

embedding=nn.Embedding(10,3,padding_idx=5)
input=Variable(torch.LongTensor([0,2,0,5]))
print(embedding(input))

embedding=nn.Embedding(10,3,padding_idx=0)
input=Variable(torch.LongTensor([0,2,0,5]))
print(embedding(input))
#通过输出我们发现
#nn.Embedding初始化这个类，相当于一个词表，横坐标代表词的序号，纵坐标对应词向量的维度
#（10，3）代表初始化10个词，每个词的词向量维度是3
#通过weight属性我们可以得到随机初始化词表中的词向量
#而input的输入代表神经网络中常用的概念，batch_size。把训练的数据分成多少个批次，每个批次的数据量是多少
#比如我们有512章图片，每个batch大小为128.那么我们可以分为4个批次。input的shape就是4*128.
#而input的数据则是embedding.weight中对应的序号，也就是行数。
#padding_idx=n代表序号为n的词向量全部设置为0
