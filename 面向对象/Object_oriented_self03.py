#self作用
"""
1. 不同的对象实例使用着相同的类（可理解为模板），但是不同的对象实例的属性以及方法不相同，所以python使用self来区分不同的对象实例。
2. python规定，类内的方法，至少要包括一个参数，这个参数名就是self.当然如果你改成其它的名称也不会报错
"""

#定义一个students类
class Students():
    name = ""
    grade = ""
    #打印出不同的实例对象对应的内存地址值
    def show_self(self):
        print("当前对象的值：{}".format(self))
    def study(self):
        print("{}现在上{}年级".format(self.name,self.grade))

#创建第一个实例对象
zhangsan = Students()
'''zhangsan的实例对象值'''
zhangsan.show_self()

#创建第二个实例对象
lisi = Students()
'''zhangsan的实例对象值'''
lisi.show_self()

#7.访问变量方法
    # 实例对象
zhangsan = Students()
zhangsan.name = '李桥红'
zhangsan.grade = 6
zhangsan.study()

    # 类名
lisi = Students()
Students.name = '李智慧'
Students.grade = 7
lisi.study()