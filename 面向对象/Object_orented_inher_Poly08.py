"""
1. 类的继承
    #多个类有一定的关联关系
    #子类继承父类后，子类具备父类的所有功能
    #子类可以继承多个父类
    语法格式：
        class 子类名(父类名1,父类名2,……)
        ...
2. 父类方法重写（多态）
(1)存在多态的条件：
            # 1.必须是继承关系
            # 2.子类复写父类的方法
            # 3.子类的方法中调用父类的方法可使用关键词super.方法名
            #注意：当子类复写父类中的方法时，优先调用子类的方法，
(2)作用：对父类的方法进行优化和更新

"""

class People():
    def say(self):
        print("父类的say方法")
#子类Students继承父类People
class Students(People):
    def __init__(self,sf):
        self.sf = sf
    def study(self):
        self.say()          #调用子类中的方法
        super().say()       #调用父类中的方法
        print("子类的sudy方法")
    #重复写父类People的say方法
    def say(self):
        print("子类中的say方法")
# 子类Students存在参数初始化：sf（身份），创建实例化对象时需要输入参数；’初中生‘
zs = Students('初中生')
zs.study()