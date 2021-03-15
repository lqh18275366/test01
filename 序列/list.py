
"""
数据可以进行增，删，改，查操作
列表提供的常用方法练习：
"""
lst1 = []
print(lst1)
print("0"+"==="*20+"定义空列表lst1")
lst = [(2,5,9),4,67,78,(3,5,6)]
print(lst)
print("1"+"==="*20+"定义lst")
#向列表中添加一个元素：append（）
lst.append(10)
print(lst)
print("2"+"==="*20+"append（10）")
#向列表中插入一个元素：insert(index,obj)
lst.insert(2,46)
print(lst)
print("3"+"==="*20+"insert（2,46）")
#修改列表中的某一个位置的值
lst[2] = 34
print(lst)
print("3"+"==="*20+"修改：lst[2] = 34")
#队列表中的元素进行排序
#lst.sort()
#print(lst)
#获取列表中的值
print(lst[0][2])
print("4"+"==="*20+"获取列表中元素：lst[0][2]")
#移除列表中的第三个元素
lst.pop(2)
print(lst)
print("4"+"==="*20+"pop（2）")
#列表反转
lst.reverse()
print(lst)
print("6"+"==="*20+"reverse")
#将列表lst中的元素复制到列表lst1中
lst1 = lst
print(lst1)
print("7"+"==="*20+"复制列表：lst1 = lst")
#清空列表lst
print(lst)
lst.clear()
print(lst)
print("8"+"==="*20+"清空lst")
"""
for x in lst:

    print(x)
"""