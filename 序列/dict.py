#字典格式：dt = {}
#定义两个字典
dt1 = {}
dt2 = {'name1':'lqh','name':'lzh'}
#获取字典中的元素
dt2['name1']
print("获取dt2中的值：",dt2['name1'])
#获取字典中不存在的值将会报错
#print("获取dt2中的值：",dt2['name4'])

#修改字典中元素：dt2['name1']= 'lxg'
dt2['name1']= 'lxg'
print("修改dt2中name1：",dt2)

#增加字典中元素：dt2['name3']= 'lhz'
dt2['name3']= 'lhz'
print("增加dt2中name3：",dt2)

#字典中常用的方法
dt3 = {'zhangsan': 23, 'lisi': 35}

#获取字典中key对应的值:get(key)
    #相同点
print("获取字典中zhangsan的值：",dt3.get('zhangsan'))
print("获取dt2中的值：",dt2['name1'])
    #不同点
#print("获取字典中zhangsan的值：",dt3.get('zhang'))  #若key不存在返回none
#print("获取dt2中的值：",dt2['name9'])            #若不存在则程序报错
print("***"+"==="*20+"dt3.get('zhangsan')")

#获取字典中偶有的键值对：dt3.items()
for key,value in dt3.items():
    print("key=",key,"value=",value)
print("***"+"==="*20+"dt3.items()")
#获取字典中所有的键：dt3.keys()
for key in dt3.keys():
    print("key=",key)
print("***"+"==="*20+"dt3.keys()")
#获取字典中所有的值：dt3.values()
for value in dt3.values():
    print("value=",value)
print("***"+"==="*20+"dt3.values()")

#更新一组字典中的键值对：dt3.update(dt2)
dt3.update(dt2)
print(dt3)
print("***"+"==="*20+"dt3.update(dt2)")