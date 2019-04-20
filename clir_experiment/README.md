# CLIR实验

#### 项目介绍
本实验旨在实现该篇论文中方法
《Monolingual and Cross-Lingual Information Retrieval
Models Based on (Bilingual) Word Embeddings》
该实验数据主要分为训练集和测试集2部分。
数据太大就没有上传，可以给我留言，我分享给你。

#### 软件架构
需要注意的一点是，nltk外部数据需要自己下载
重新编写一个py文件，文件中就2行代码
import nltk
nltk.download()
然后从弹出窗口中选择自己需要的下载即可。


#### 安装教程

1. xxxx
2. xxxx
3. xxxx

#### 使用说明

1. test_collection_process.py,对测试文档进行处理，这里主要包括荷兰语测试集和英文测试集合。
2. index.py,利用测试文档生成索引。
3. query_generate.py,生成对应的查询文件。
4. WE_training.py,用于训练词向量。
5. WeightingModel.py,自定义几种可使用的权重模型。
6. search.py,检索内容。
7. map.py,用于最后评估系统性能。

#### 参与贡献

1. Fork 本项目
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request


#### 码云特技

1. 使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2. 码云官方博客 [blog.gitee.com](https://blog.gitee.com)
3. 你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解码云上的优秀开源项目
4. [GVP](https://gitee.com/gvp) 全称是码云最有价值开源项目，是码云综合评定出的优秀开源项目
5. 码云官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6. 码云封面人物是一档用来展示码云会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)