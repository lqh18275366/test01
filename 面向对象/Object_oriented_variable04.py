#变量
"""
1. 变量的分类：
    （1）类变量
        所有类的实例化对象都同时共享类变量，属于类的公共资源数据。
        类方法的调用方式有 2 种，既可以使用类名直接调用，也可以使用类的实例化对象调用。
    （2）实例变量
        实例变量指的是在任意类方法内部，以“self.变量名”的方式定义的变量，其特点是只作用于调用方法的对象。
        实例变量只能通过对象名访问，无法通过类名访问。
    （3）局部变量
        局部变量直接在方法内定义的变量且以“变量名=值”的方式进行定义
        局部变量的使用范围也仅限于所定义的方法内
2. 访问变量：使用点号 . 来访问对象的属性
    (1) 使用实例对象
            lqh.Inst_var(25,90)
    (2) 使用类名：增删改查
            Students.age = 7  # 添加一个 'age' 属性
            Students.age = 8  # 修改 'age' 属性
            del Students.age  # 删除 'age' 属性
    (3) 使用pthon函数：增删改查
            hasattr(Students, 'age')    # 如果存在 'age' 属性返回 True。
            getattr(Students, 'age')    # 返回 'age' 属性的值
            setattr(Students, 'age', 8) # 添加属性 'age' 值为 8
            delattr(Students, 'age')    # 删除属性 'age'
"""

#定义一个students类
class Students():
    #定义类变量：name和grade
    name = ""
    def Inst_var(self,age,grade):
        #定义实例变量：age
        self.age = age
        self.grade = grade
        print("类方法1 ；类变量：名字（name）={}    实例变量（age）={}".format(self.name,self.grade,self.age))
    def local_var(self,sno):
        #定义局部变量：sno
        sno = sno
        print("类方法2 ：局部变量（sno）={}  多个方法可引用实例变量（age）={} ".format(sno,self.age))

    def show_self(self):
        return self

lqh = Students()
lzh = Students()

#1.访问类变量:使用点号 . 来访问对象的属性
    #（1）使用实例对象
lqh.name = '李桥红'
lzh.name = '李智慧'
lqh.grade = 6
lqh.Inst_var(25,90)
print("=="*30+"类的实例")

    #（2）使用类名：增删改查
        # ① 添加一个 'warning' = 1
Students.Instance_object_value = lqh.show_self()
print("添加属性；对象实例={}，name={}：".format(Students.Instance_object_value,lqh.name))
        # ② 访问类的属性：用点号 . 来访问对象的属性
print("获取实例对象值=",Students.Instance_object_value)
        # ③ 修改 'warning' = 0
Students.Instance_object_value = lzh.show_self()
print("修改属性；对象实例={}，name={}：".format(Students.Instance_object_value,lzh.name))
        # ④ 删除 'warning' 属性
del Students.Instance_object_value
print("=="*30+"类的属性")

    # (3) 使用pthon函数：增删改查
for i in [0,1]:
    if i:
        #删除属性：'max_people_nums
        delattr(Students, 'grade_01')
        #检查是否存在属性：warning_01
        print("属性grade_01不存在，grade_01=",hasattr(Students, 'grade_01'))
        # 创建一个新属性：max_people_nums = 5
        setattr(Students, 'grade_01', 5)
        # 访问对象的属性值:max_people_nums
        print("删除属性grade_01=", getattr(Students, 'grade_01'))
    else:
        #创建属性：'max_people_nums', 7
        setattr(Students, 'grade_01', 7)
        #检查是否存在属性：warning_01
        print("属性warning_01存在，warning=",hasattr(Students, 'grade_01'))

        # 访问对象的属性值:max_people_nums
        print("读取属性grade_01=", getattr(Students, 'grade_01'))

        # 修改对象的属性：max_people_nums=18
        setattr(Students, 'grade_01', 18)

        # 访问对象的属性值:max_people_nums
        print("修改属性grade_01=", getattr(Students, 'grade_01'))
    print("=="*30+"pthon函数的方式")

#2.访问实例变量：必须使用正确的实例对象
lzh.Inst_var(20,80)

#3. 访问局部变量：仅在方法内使用
lqh.local_var(2015)
lzh.local_var(2016)

