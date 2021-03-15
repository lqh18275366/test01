#序列中的通用操作：索引，切片，相加，相乘，检查成员
#序列包括：列表，元组，字典，字符串，其中字典不支持索引，切片、相加和相乘操作

#1.索引
lst = ['red',10,3,29,'yy']
print("获取第二个元素：",lst[1])  #从左往右取，从0开始
print("获取第二个元素：",lst[-4])  #从右往左取，从-1开始

#2.切片：lst[start:end:step] （类似于range），start默认0，step默认1，end默认为列表长度
lst5 = ['red','green','blue','black','gold','orange']
print("获取第3~5个元素：",lst5[2:5])
print("获取奇数的值：",lst5[0:6:2]) #lst5[0:6:2]等价于lst5[:6:2]
print("获取第3个及后面的元素：",lst5[2::])  #冒号不能省略,lst5[2::]等价于lst5[2:]
print("将列表中的元素进行翻转:",lst5[::-1])

#3.相加/相乘
#相乘：列表中的内容需被赋值n次
a_lst = ['a']
b_lst = ['b']
print("两个列表相加：",a_lst+b_lst)
print("两个列表相乘：",a_lst*3)

#检查成员：in
print("检查成员：",'glod' in lst5)
print("检查成员：",'glod' in lst)