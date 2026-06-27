a=1
b=2
c=3
my_dic={}
my_dic[(a,b,c)]=39
my_dic[(c,b,a)]=10
my_dic[(a,b)]=20
sum=0
for k in my_dic:
    sum+=my_dic[k]
print(sum)
