# 类的继承
    #多个类有一定的关联关系
    #自雷继承父类后，自雷就具备父类的所有功能
class People():
    def say(self):
        print("可以说话")

class Students(People):
    def study(self):
        print("学生学习")

class Teachers(People):
    def tearch(self):
        print("老师教书")

zs = Students()
zs.say()

ls = Teachers()
ls.say()