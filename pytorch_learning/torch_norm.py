import torch

#官方例子
#torch.norm(input, p, dim, out=None) → Tensor
#返回输入张量给定维dim 上每行的p 范数。 输出形状与输入相同，除了给定维度上为1.
a=torch.randn(1,3)
print(a)
print(torch.norm(a,3))
b=torch.randn(4,2)
print(b)
print(torch.norm(b,2,1))
print(torch.norm(b,0,1))

#怎么来计算范数
#用上述的例子进行验证
c=a.numpy()  #将tensor转变成numpy,1*3的二维数组
print(c)
result=0
for s in c[0]:
    result+=round(s,4)**3  #因为是求p3范式，所以每列中数的3次方,round(s,4)是小数点后四位四舍五入。多运行几次，因为randn生成是随机数
result=pow(result,1.0/3)  #最后还要开3次根号
print(round(result,4))

#探讨给定维度
m=torch.randn(2,3)
print(m)
print(torch.norm(m,2))
n=m.numpy()
p=0
for i in n:
    for j in i:
        p+=round(j,4)**2
p=round(pow(p,1.0/2),4)
print(p)
#如果不设置维度就对所有的值进行范式计算，最后得到一个数






