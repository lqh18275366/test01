# 面向对象设计

"""
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
# 抽象设计出一个电梯类
class Elevator():
    #  1. 定义属性（变量）
    button = "开门"          # 1）按钮
    max_people_nums = 15    # 2） 荷载人数
    floor = 9               # 3） 层数

    # 2. 定义方法（函数）
    def open(self):
        print("开门")       # 1.开门
    def close(self):
        print("关门")       # 2. 关门
    def run(self,nums):
        print("我要去{}层".format(nums))  # 3. 升降
#3. 创建实例对象：et（实例可自定义）
et = Elevator()
#实例et（et，也可以是其他实例）需要实现电梯的升降功能
et.run(6)
# 4. 访问类的属性：用点号 . 来访问对象的属性
print(Elevator.floor)
print("=="*30+"定义class步骤")



# 5. 访问类的属性：增删改查
# 添加一个 'warning' = 1
Elevator.warning = 1

# 访问类的属性：用点号 . 来访问对象的属性
print("获取属性warning=",Elevator.warning)

#修改 'warning' = 0
Elevator.warning= 0
print("修改属性warning=",Elevator.warning)

# 删除 'warning' 属性
del Elevator.warning
print("=="*30+"访问类的属性：增删改查")


# 6. 函数的方式来访问类的属性：增删改查
#删除属性：'max_people_nums'
class_properties = {"创建属性":setattr(Elevator, 'max_people_nums', 5),"删除属性":delattr(Elevator, 'max_people_nums')}
for i in [0,1]:
    if i:
        #删除属性：'max_people_nums
        delattr(Elevator, 'warning_01')
        #检查是否存在属性：warning_01
        print("属性warning_01不存在，warning=",hasattr(Elevator, 'warning_01'))
        # 创建一个新属性：max_people_nums = 5
        setattr(Elevator, 'warning_01', 5)
        # 访问对象的属性值:max_people_nums
        print("删除属性warning_01=", getattr(Elevator, 'warning_01'))
    else:
        #创建属性：'max_people_nums', 7
        setattr(Elevator, 'warning_01', 7)
        #检查是否存在属性：warning_01
        print("属性warning_01存在，warning=",hasattr(Elevator, 'warning_01'))

        # 访问对象的属性值:max_people_nums
        print("读取属性warning_01=", getattr(Elevator, 'warning_01'))

        # 修改对象的属性：max_people_nums=18
        setattr(Elevator, 'warning_01', 18)

        # 访问对象的属性值:max_people_nums
        print("修改属性warning_01=", getattr(Elevator, 'warning_01'))
    print("=="*30+"函数的方式来访问类的属性：增删改查")
