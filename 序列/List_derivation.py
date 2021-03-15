#列表推导式

#需求：生成一个存放着1~10的列表
    #常规写法
lst = []
for t in range(1,11):
    lst.append(t)
print(lst)

    #列表推导式:expB for x in iterable expA
        #expB:对x运算，如加减乘除以及条件判断
        #for x in iterable：循环序列
        #expA：条件筛选或再次循环
        #执行顺序：循环体————条件筛选————对x运算
print([x for x in range(1,11)])
print("*"*60)



# 生成一个列表，列表中存放着1~10的数,输出偶数的值*2
lst = [1,3,6,8,5,3,7,5,9,10,11,60,13,14]
lst1 = []
    #传统方法
for i in lst:
    while i % 2 == 0 :
        lst1.append(i+2)
        i += 1
print(lst1)

print('*'*70+'传统方法：生成列表且偶数+2')
    #列表推导式
print([x*2 for x in lst if x % 2==0])

print('*'*70+'列表推导式：生成列表且偶数*2')
# 将两次循环的值连接起来放在列表中
    # 常规写法
a = 'abc'
b = '123'
c = []
for x in a:
    for y in b:
        c.append(x+str(y))
print(c)

a = [3,4,5]
b = ['h','j','l']
lst = []
for x in a:
    for y in b:
        lst.append(y+str(x))
print(lst)
    #列表推导式
print([y+str(x) for x in a for y in b])

