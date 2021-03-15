"""
封装：
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs

类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods

    注：
    __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。

    _foo: 单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *

    __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。

"""

class demo():
    #公有属性
    name1 = ''
    age1 = 10
    sno1 = 0
    #单下划线私有属性
    _grade = 2
    #定义双下划线私有属性
    __course = '语文'
    #定义类的公有方法
    def get_name1(self):
        print(self.name1)
    #定义类的单下划线(_)私有方法
    def _get_age1(self):
        print(self.age1)
    #定义类的双下划线（__）私有方法：双下划线的私有类方法仅能在Student（）中使用
    def __get_sno(self):
        print(self.sno1)
class Student():
    s_name = ""
    s_age = 0
    def get_age(self):
        return self.s_age
    def show(self):
        #实例化类demo
        d = demo()
        #调用类demo中公有方法：get_name1
        '''公共类方法get_name1在整个项目中均可调用'''
        d.get_name1()
        #调用类demo中单下划线（_）的私有的方法：get_age1
        '''仅能在该文件(Object_oriented_encapsulation05.py)中调用单线划线私有方法（get_age1)'''
        d._get_age1()
s = Student()
s.show()