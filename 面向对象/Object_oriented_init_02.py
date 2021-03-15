#2.初始化数据：将类中的部分属性设置为默认值，
"""pthon的构造方法，语法格式：
def __init__(self,……):
    代码块
"""
#优点：每次生实例成对象时会自动调用此方法

# 例: 创建学生类，要求有属性：姓名和年级 ; 方法有：学习的方法，打印学生的上课情况
    # 1.定义类
class Students():
    # 2. 定义属性
    name = ""
    grade = ""
    # 3. 构造方法：初始化数据
    def __init__(self,name,grade):
        # 从构造方法中获取的参数值赋值给类student()中对应的属性
        self.name = name
        self.grade = grade
    # 4. 定义方法
    def study(self):
        print("{}现在上{}年级".format(self.name,self.grade))

    def show_self(self):
        print("当前对象的值：{}".format(self))

# 5. 初始化对象：创建实例对象时确定参数值并入到构造方法__init__(self,name,grade)中

# 例1：此例中的对象实例（zhangsan）的属性值（name=张三，grade=3）
zhangsan = Students('张三',3)
zhangsan.study()

# 例2：此例中的对象实例（lisi）的属性值（name=李四，grade=6）
lisi = Students('李四',6)
lisi.study()


#6.self
'''zhangsan的实例对象值'''
zhangsan.show_self()
'''zhangsan的实例对象值'''
lisi.show_self()

