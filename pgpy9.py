my_dic={}
my_dic[(1,2,4)]=8
my_dic[(4,2,1)]=10
my_dic[(1,2)]=12
sum=0
for k in my_dic:
    sum+=my_dic[k]
print(sum)
print(my_dic)
