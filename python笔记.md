#  python 笔记
- 注释/取消多行代码快捷键
    - 选中需要注释/取消注释的所有代码
    - 按快捷键：windows系统（同时按一下键：”ctrl / + “或 ”ctr ？“）

## 1   if条件语句
### 1.1  if 单分支 ：

```python
"""
    语法格式：
    if 条件判断:
        条件代码块
"""
```

### 1.2  if多分支 ：

```python
"""
    #语法格式：
    if 条件1：
        代码块1
    elif 条件2：
        代码块2
    else:
        代码块n
"""
```
### 1.3  条件判断说明

- 表达式 ： 比较表达式
- 单一的值 ： 字符串，数字，None，序列


## 2  循环语句
### 2.1  循环语句定义
```python
# for循环：语法格式
"""
for x in seq:
    print("xxx")
"""

# while循环：语法格式
"""
while 条件判断:
    代码块
"""
# range()
"""
    range(start,end,step)
    start : 开始位置 ，默认从0开始
    end : 结束位置
    step : 步长 ，默认步长是1
"""
```
### 2.2  思考总结
#### 2.2.1  for 与 while
    - for 循环的结束条件是将序列中的所有元素都取完，结束循环
    - while循环的结束条件是判断语句为False时，结束循环

#### 2.2.2  break 与 continue
    - break
        1.break 语句可用于跳出循环。
        2.break 所在的循环体已经结束。
    - continue
        1.continue 语句中断循环中的迭代，如果出现了指定的条件，然后继续循环中的下一个迭代。
        2.continue 所在的循环体并没有结束。
#### 2.2.3  for in 与 for in range()
    -for in range([start], stop, [step])
        1.在一个范围内历遍
        2.返回等差数列。构建等差数列，起点是start，终点是stop，但不包含stop，公差是step。
        3.start和step是可选项，没给出start时，从0开始；没给出step时，默认公差为1。
    -for in
        in : 判断一个元素是否在另外一个元素中
        for in是直接历遍一个数据组
#### 2.2.4  is 与 ==
    - is : 判断两个对象的引用地址是否相等,例如：id()
    - == : 比较两个对象的内容是否相等

## 3  列表：顺序存储

```python
# 定义 ： lst = [] or list()

# eg :
lst = [1,2,4]

# 常用的方法
# 添加元素：append(x)
# 插入元素 ： insert(index,x)
# 删除元素： clear()
# 修改元素 ： lst[1] = 'abc'
# 获取元素 ： lst[1]
```

## 4  元组：顺序存储
- 元组定义：tp = （）
- 元组特点：元组定义后就不能修改

## 5  字典：无序存储
    - 特征
        - 键必须是唯一的
        - 值可以是任何数据类型
    - 定义字典
        - d = {key1:value1,key2:value2}
    - 字典常用方法
        - 修改字典中元素：dt2['name1']= 'lxg'
        - 增加字典中元素：dt2['name3']= 'lhz'
        - 获取字典中key对应的值:get(key)或dt2['name1' 不同如下：
                ```python
                    #若key不存在返回none
                    #print("获取字典中zhangsan的值：",dt3.get('zhang'))  
                    #若不存在则程序报错
                    #print("获取dt2中的值：",dt2['name9'])            
                ```
  
    
    -  获取字典中偶有的键值对：dt3.items()，例如：
                ```python
                        for key,value in dt3.items():
                        print("key=",key,"value=",value)
                ```
    - 获取字典中所有的键：dt3.keys()
    - 获取字典中所有的值：dt3.values()
    - 更新一组字典中的键值对：dt3.update(dt2)
    

## 6  字符串格式化：str
### 6.1  %方式
```python
#%s：格式化字符串
#%d：格式化整数
#%f：格式化浮点数

#例：
print("我的名字叫：%s"%"李桥红")
print("他的年龄是%d" % 25)
print("他今天花了%.2f钱" % 238.9)
```   

### 6.2  format()方式
- 普通：
        - “{}”.format("传入的字符串")
 - 位置参数：
        - “{0},{1},{2},……”.format("位置0的值","位置1的值”,"位置2的值",……)
```python
           print("我的名字：{0}，年龄{1}，现居城市：{2}".format('李桥红',25,"北京"))
```

- 关键字参数：可更换位置
        - “{x},{y},{z},……”.format(x="位置0的值",z="位置1的值”,y="位置2的值",……)
```python
            print("我的名字：{x}，年龄{y}，现居城市：{z}".format(y=25,z="北京",x='李桥红'))
```
- 组合使用：位置参数必须放在关键字前面
```python
            print("我的名字：{0}，年龄{y}，现居城市：{1}".format('李桥红',"北京",y=25))
```
## 7  序列中的通用操作
- 序列中的通用操作：索引，切片，相加，相乘，检查成员
- 序列包括：列表，元组，字典，字符串，其中字典不支持索引，切片、相加和相乘操作
### 7.1  索引
```python
lst = ['red',10,3,29,'yy']
print("获取第二个元素：",lst[1])  #从左往右取，从0开始
print("获取第二个元素：",lst[-4])  #从右往左取，从-1开始
```
### 7.2  切片
```python
#2.切片：lst[start:end:step] （类似于range），start默认0，step默认1，end默认为列表长度
lst5 = ['red','green','blue','black','gold','orange']
print("获取第3~5个元素：",lst5[2:5])
print("获取奇数的值：",lst5[0:6:2]) #lst5[0:6:2]等价于lst5[:6:2]
print("获取第3个及后面的元素：",lst5[2::])  #冒号不能省略,lst5[2::]等价于lst5[2:]
print("将列表中的元素进行翻转:",lst5[::-1])
```
### 7.3  相加/相乘
```python
#3.相加/相乘
#相乘：列表中的内容需被赋值n次
a_lst = ['a']
b_lst = ['b']
print("两个列表相加：",a_lst+b_lst)
print("两个列表相乘：",a_lst*3)
```
### 7.4  检查成员
```python
#检查成员：in
print("检查成员：",'glod' in lst5)
print("检查成员：",'glod' in lst)
```

## 8  列表推导式
    序列：字典，元组，字符串以及range()方法,for循环体被优先执行
    表达式：+，-，*，%，|
    两个for循环后面的for循环是内嵌循环体
### 8.1  [表达式 for 变量 in 序列 ] 
```python
#需求：生成一个存放着1~10的列表
    #常规写法
lst = []
for t in range(1,11):
    lst.append(t)
print(lst)

    #列表推导式:expB for x in iterable expA
        #expB:对x运算，如加减乘除以及条件判断
        #for x in iterable：循环序列
        #expA：条件筛选或再次循环
        #执行顺序：循环体————条件筛选————对x运算
print([x for x in range(1,11)])
```

### 8.2  [表达式 for 变量 in 序列 if 条件]
```python
# 生成一个列表，列表中存放着1~10的数,输出偶数的值*2
lst = [1,3,6,8,5,3,7,5,9,10,11,60,13,14]
lst1 = []
    #传统方法
for i in lst:
    while i % 2 == 0 :
        lst1.append(i+2)
        i += 1
print(lst1)

print('*'*70+'传统方法：生成列表且偶数+2')
    #列表推导式
print([x*2 for x in lst if x % 2==0])

print('*'*70+'列表推导式：生成列表且偶数*2')
```
### 8.3  [表达式 for 变量 in 序列 for 变量2 in 序列]
```python
# 将两次循环的值连接起来放在列表中
    # 常规写法
a = 'abc'
b = '123'
c = []
for x in a:
    for y in b:
        c.append(x+str(y))
print(c)

a = [3,4,5]
b = ['h','j','l']
lst = []
for x in a:
    for y in b:
        lst.append(y+str(x))
print(lst)
    #列表推导式
print([y+str(x) for x in a for y in b])

```
## 9  函数
### 9.1  函数定义
```python
"""
def 函数名字(参数列表):
    函数体
"""
#定义一个加法函数:
# 参数列表数量可以没有，也可以是多个，形参不能是具体的值

def add(a,b):
    c = a + b
    print(c)
# 使用函数:add(a,b) ，a和b也可以是序列
# 其中3是a的实参，4是b的实参
add('e','d')
print('*'*60+'函数使用：函数名字(参数列表)')
```
### 9.2  return语句的3种返回方式
return返回none(默认)
```python
    # return返回none(默认)
def add_default(a1,b1):
    c1 = a1 +b1
print(add_default(3,8))
print('*'*60+'reurn值：none')
```
return返回表达式
```python
    # return返回表达式
        #方式1
def add_expression01(a2,b2):
    return a2+b2
print(add_expression01(5.4, 1))
```
return返回多个值
```python
    #return返回多个值
def calc(a4,b4):
    add = a4 + b4
    min = a4 - b4
    cf = a4 * b4
    div = a4 / b4
    return add,min,cf,div
print(calc(4,8))
print('*'*60+'reurn值：多个值')
```
### 9.3  定义函数时有/无返回值（return）的区别
```python
def add(a,b):
     a + b
def add_expression01(a2,b2):
    return a2+b2
# 无return返回的是none
print("无return语句函数add（）返回：",add(3,7))

# 有return返回的是函数运行结果
result = add_expression01(4,2)
print("有return语句函数add1（）返回：",result)
print('*'*60+'有/无return的区别')
```

### 9.4  参数类型

#### 9.4.1  无默认参数

```python
def student_lesson(name,programing_language,parameter_type):
    z = "姓名：{}，编程语言：《{}》，参数类型：（{}）".format(name,programing_language,parameter_type)
    return z

#1.位置参数
'''位置参数：不可可以交换位置且实参必须按照形参格式输入，即，不能多也不能少实参'''
print(student_lesson('李桥红',"python_01","位置参数"))

#2.关键字参数传入方式：
'''关键字参数：可以交换位置'''
print(student_lesson(name='李慧',programing_language="python_02",parameter_type="关键字参数"))

#3. 位置参数和关键字参数 混合使用：
'''关键字参数必须放在最后，否则程序报错'''
print(student_lesson('李丹',parameter_type='位置参数和关键字参数 混合使用',programing_language='python_03'))
```
#### 9.4.2  有默认参数
```python
''''查找学生信息'''
name = input("姓 名：")
sno = input("学 号：")
def check_stu_msg(name,sno,school="tjcu"):
    student_information = ("学生信息表 \n姓名：{} \t学号：{} \t学校：{}".format(name,sno,school))
    return student_information
print(check_stu_msg(name,sno))
```
优化程序：对实参进行过滤操作并给出提示
```python
print('*'*20+"对姓名和学号进行判断过滤")
name1 = input("姓 名：")
sno1 = int(input("学 号："))
def check_stu_filter_msg(name1,sno1,school1="tjcu"):
    """
    实现思路：当输入的x和y是非整数或非浮点数，返回提示信息
            若输入的是整数或浮点数，则进行相加操作
    :param : int or float
    :param b: int or float
    :return: student_information
    判断两个类型是否相同推荐使用 isinstance()，类似 type()
    (name1 >= u'一' and name1<=u'龥'):name为中文名
    (name1 >= u'A' and name1<=u'Z') or (name1 >= u'a' and name1<=u'z')：name为英文名
    """
    if not ((name1 >= u'一' and name1<=u'龥') or (name1 >= u'A' and name1<=u'Z') or (name1 >= u'a' and name1<=u'z')):
        return '姓名应为汉字或英文字母'
    if not (isinstance(sno1,float) or len(str(sno1)) < 9):
        return '输入的参数sno要求必须是整数且学号长度小于9'
    student_information = ("学生信息表 \n姓名：{} \t学号：{} \t学校：{}".format(name1,sno1,school1))
    return student_information
print(check_stu_filter_msg(name1,sno1))
```
#### 9.4.3  可变化参数
```python
#5.可变化参数
#语法格式：
def 函数名(位置参数1,位置参数2,*列表):
    print(type(列表))
    print(列表)  #列表名为元组
    for x in 列表:
        print(x,end=' ')  #end=' ':输出显示在同一行
print(函数名(1,2,3,4,5))
```

列表形式：*args
```python
#实现add方法可以接受任意数据相加
def add(x,y,*args):
    sum = 0
    for z in args:
        sum += z
    sum = sum + x + y
    return sum
    #1.直接传入实际参数
print(add(1,2,3,4,5,6,7))
    #2.在窗口依次输入6个数据并将其以列表的形式传入add方法中，最后输出6个数据之和
def lst_input():
    i = 0
    lst = []
    print("请依次输入6个数据")
    while i <= 5:
        a = int(input("\t \t请第{}输入数据：".format(i)))
        lst.append(a)
        i += 1
    return lst
print("输入所有数据之和：",add(3,5,*lst_input()))
```

字典形式：**kwargs
```python
#6.可变参数：字典形式
def show_Dict(**kwargs):
    print(kwargs)
    #通过关键字传入
print(show_Dict())
print(show_Dict(key1='abc',key2='123'))

    #通过字典形式传入
dt = {'key1':'abc','key':'123'}
print(show_Dict(**dt))
```

## 10  面向对象
面向对象将现实的事物抽象出来，然后抽象成 类 ( class )，给类定义属性和方法后，再将类实例化成 实 例 ( instance ) ，通过访问实例的属性和调用方法来进行使用。
- 类：通过定义的class + 类名
- 属性：类中的所有变量称为属性
- 类中所有的函数统称为方法
- 对象：创建的类并不能直接使用，只有通过类创建出的实例(又称对象)才能使用

```python
#类的语法格式：
class ClassName():
    # 属性 >= 0
    # 方法 >= 0

# 例: 抽象设计出一个电梯类
class Elevator():
    #  属性（变量）
    button = "开门"          # 1）按钮
    max_people_nums = 15    # 2） 荷载人数
    floor = 9               # 3） 层数

    # 方法（函数）
    def open(self):
        print("开门")       # 1.开门
    def close(self):
        print("关门")       # 2. 关门
    def run(self,nums):
        print("我要去{}层".format(nums))  # 3. 升降
#创建实例对象：et（实例可自定义）
et = Elevator()
#实例et（et，也使用其他实例）需要实现电梯的升降功能
et.run(6)
```

### 10.1  初始化数据：__init__(self,...)
- 初始化数据：将类中的部分属性设置为默认参数值
```python
"""
1. 初始化数据：将类中的部分属性设置为默认值
2. pthon的构造方法格式：
    def __init__(self,……):
        代码块
3. 优点：每次生实例成对象时会自动调用此方法
4. 特点：
    ① __init__方法的第一参数永远是self，表示创建的类实例本身
    ② 不能传入空的参数了，必须传入与__init__方法匹配的参数，其中self不需要传
"""
```
例：创建学生类，要求有属性：姓名和年级 ; 方法有：学习的方法，打印学生的上课情况
```python
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

# 5. 初始化对象：创建实例对象时确定参数值并入到构造方法__init__(self,name,grade)中

# 例1：此例中的对象实例（zhangsan）的属性值（name=张三，grade=3）
zhangsan = Students('张三',3)
zhangsan.study()
# 例2：此例中的对象实例（lisi）的属性值（name=李四，grade=6）
lisi = Students('李四',6)
lisi.study()
```
### 10.2  self作用

1. 不同的对象实例使用着相同的类（可理解为模板），但是不同的对象实例的属性以及方法不相同，所以python使用self来区分不同的对象实例。
2. python规定，类内的方法，至少要包括一个参数，这个参数名就是self.当然如果你改成其它的名称也不会报错，
- 举例如下
```python
#定义一个students类
class Students():
    #打印出不同的实例对象对应的内存地址值
    def show_self(self):
        print("当前对象的值：{}".format(self))

#创建第一个实例对象
zhangsan = Students()
'''zhangsan的实例对象值'''
zhangsan.show_self()

#创建第二个实例对象
lisi = Students()
'''zhangsan的实例对象值'''
lisi.show_self()
```
- 运行结果
```
当前对象的值：<__main__.Students object at 0x038A6310>
当前对象的值：<__main__.Students object at 0x03A07250>
```
## 11  变量：
```
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
```
### 11.1  定义类:students（）
```python
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
```
### 11.2  访问类变量: 
#### 11.2.1  使用实例对象
```python
lqh.name = '李桥红'
lzh.name = '李智慧'
lqh.grade = 6
lqh.Inst_var(25,90)
print("=="*30+"类的实例")
```
#### 11.2.2  使用类名：增删改查
```python
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
```
#### 11.2.3  使用pthon函数：增删改查
```python
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
```
### 11.3  访问实例变量：必须使用正确的实例对象
```python
lzh.Inst_var(20,80)
```
### 11.4  访问局部变量：仅在方法内使用
```python
lqh.local_var(2015)
lzh.local_var(2016)
```

```python

```

## 12  封装：公有/私有
```
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs

类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods

    注：
    __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。

    _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *

    __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
```

类的私有方法
```python
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
```
## 13  继承 / 多态：
```
1. 类的继承
    (1)特点
        ① 多个类有一定的关联关系
        ② 子类继承父类后，子类具备父类的所有功能
        ③ 子类可以继承多个父类
    (2)作用：代码的重用
    (3)语法格式：
        class 子类名(父类名1,父类名2,……)
        ...
2. 父类方法重写（多态）
    (1)存在多态的条件：
        ① 必须是继承关系
        ② 子类复写父类的方法
        ③ 子类的方法中调用父类的方法可使用关键词super.方法名
        ④ 注意：当子类复写父类中的方法时，优先调用子类的方法，
    (2)作用：对父类的方法进行优化和更新
```

```python
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
```
## 14  模块：后缀为 ：.py 的文件
### 14.1  导包方式
(1) 新建一个Modules_packages_calcs.py文件
```python
def add(a,b):
    c = a + b
    print(c)
```
(2) 创建一个新的python文件(Modules_packages)，将Modules_packages_calcs.py导入到Modules_packages.py文件并使用add方法
```python
#1.通过import 导入 ： import 文件名
from demo_01.模块和包 import Modules_packages_calcs

#使用导入文件（calc）：c1 = 文件名.类名
print(Modules_packages_calcs.add(4, 9))


#2. 通过from  ... import : from 包名 import 类名|函数|方法
from demo_01.模块和包.Modules_packages_calcs import add
#使用导入文件（calc）：c1 = 类名
print(add(3,4))
```
### 14.2  导入python系统提供
```python
'''
1. os模块
os.listdir(path)    返回指定的文件夹包含的文件或文件夹的名字的列表
os.path.isfile(path)	判断路径是否为文件
os.path.join(path1[, path2[, ...]])	把目录和文件名合成一个路径
os.path.split(path)	把路径分割成 dirname 和 basename，返回一个元组
'''
# 使用os模块中的一些常用方法
import os
# 查看当前路径下所有的文件和目录
print(os.listdir('.'))
# os.path.basename(path)	返回文件名
print(os.path.basename(r'e:\api_project\python_study02\demo_01\calc.py'))
# 分隔路径和文件名
print(os.path.split(r'e:\api_project\python_study02\demo_01\calc.py'))

'''
2.datetime模块
date 日期对象,常用的属性有year, month, day
time 时间对象
datetime 日期时间对象,常用的属性有hour, minute, second, microsecond
timedelta 时间间隔，即两个时间点之间的长度

'''

#导入datetime模块
from datetime import datetime
#strftime：对datetime对象进行格式化，生成需要时间格式的时间
now = datetime.now()
print(now)
df = now.strftime("%Y-%m-%d %H:%M:%S")
print(df)
dp1 = datetime.strptime(df, "%Y-%m-%d %H:%M:%S")
print(dp1)

print(datetime.strptime('2021-02-27 22:14:03',"%Y-%m-%d %H:%M:%S"))

'''
3. sys模块
sys模块提供了一系列有关Python运行环境的变量和函数。
sys.argv：可以用sys.argv获取当前正在执行的命令行参数的参数列表(list)。
sys.path:返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform:获取当前执行环境的平台，如win32表示是Windows系统，linux2表示是linux平台
'''

```
## 15  安装第三方软件
- (1) 下载第三方包：pip install 包名 
    - pip install requests
    - pip install pymysql

- (2) 查看软件包 : pip show 包名 
    - pip show pymysql
    - pip show requests

- (3) 有的包有时候下载慢或无法下载，可以指定国内镜像 
    - pip install 包名 -i http://pypi.douban.com/simple/

## 16  文件
Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError
```
1. 常用格式：open(file, mode='r')
2. 完整格式：open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    (1) 参数说明：
        file: 必需，文件路径（相对或者绝对路径）。
        mode: 可选，文件打开模式
        buffering: 设置缓冲
        encoding: 一般使用utf8
        errors: 报错级别
        newline: 区分换行符
        closefd: 传入的file参数类型
        opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。
    (2) 可选打开模式（mode）：
        r：以只读⽅式打开⽂件。 ⽂件的指针将会放在⽂件的开头， 这是默认模式。 如果⽂件不存在， 抛出异常
        w： 以只写⽅式打开⽂件。 如果⽂件存在会被覆盖。 如果⽂件不存在， 创建新⽂件
        a： 以追加⽅式打开⽂件。 如果该⽂件已存在， ⽂件指针将会放在⽂件的结尾。 如果⽂件不存在， 创建新 ⽂件进⾏写⼊
        r+： 以读写⽅式打开⽂件。 ⽂件的指针将会放在⽂件的开头。 如果⽂件不存在， 抛出异常
        w+： 以读写⽅式打开⽂件。 如果⽂件存在会被覆盖。 如果⽂件不存在， 创建新⽂件
        a+： 以读写⽅式打开⽂件。 如果该⽂件已存在， ⽂件指针将会放在⽂件的结尾。 如果⽂件不存在， 创建新 ⽂件进⾏写⼊
    (3) file 对象常用的函数：
        file.read([size])： 从文件读取指定的字节数，如果未给定或为负则读取所有。
        file.readline([size]) ：读取整行，包括 "\n" 字符。
        file.readlines([sizeint]) ：读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
        file.write(str) ：将字符串写入文件，返回的是写入的字符长度。
        file.writelines(sequence) ：向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
        file.close() ：关闭文件。关闭后文件不能再进行读写操作。
        file.seek(offset,[whence]) :方法用于移动文件读取指针到指定位置。
        file.tell() : 返回文件当前位置。

```
### 16.1  文件的读写步骤
```python
#1. 文件读写步骤：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
# (1) 读取文件：a.txt 内容
    # ①. 需要打开文件:open()
    # 生成一个对象：r
r = open('read.txt','r')
    # ②. 使用对象f读取read.txt文件并打印文件内容: f.read()
print("读取文件read.txt的内容:\n",r.read())
    # ③. 关闭文件 :close()
r.close()

# (2) 编辑write.txt文件
    # ①. 需要打开文件:open()
w = open('write.txt','w')
    # ②. 使用对象w编辑write.txt文件并打印文件内容: f.write()
w.write('python java')

# (3) 关闭文件 :close()
w.close()
```
### 16.2  File(文件)方法使用
```python
fileobject.readline()
"""
readline() 方法语法格式：
    fileObject.readline([size]); 
        size -- 从文件中读取的字节数。
    返回值：从字符串中读取的字节。
"""
# 打开文件
rl = open("readline.txt", "rb+")
print ("打开文件名为: ", rl.name)
i = 1
while i < 8:
    line = rl.readline()
    print("读取第{}行内容{}" .format(i,line))
    i = i + 1
```
fileobject.seek()
```python
"""
file.seek() 方法语法格式：
    fileObject.seek(offset,[ whence])
        offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
        whence：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。
    返回值: 如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。
"""
rl.seek(4, 0)  # 从头开始，偏移4个字节
position = rl.tell()
line = rl.readline(7)
print("当前位置{},读取内容{}".format(position,line))

rl.seek(4, 1)  # 从当前位置开始，偏移4个字节
line = rl.readline(5)
print("当前位置{},读取内容{}".format(position,line))

rl.seek(-4, 2)
line = rl.readline(3)
print("当前位置{},读取内容{}".format(position,line))
# 关闭文件
rl.close()
```
### 16.3  使用with as 变量
主要用于文件的读写操作，省去了关闭文件的麻烦，适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等
```python
# 使用with进行读取文件
# 格式 ： with open(f,'r') as 变量

#将捕获到的异常对象赋值给e
with open('a.txt','r') as f:
    all_lines = f.readlines()
    for x in all_lines:
        print(x)
```

## 17  异常处理
### 17.1  try except 语句及结构
- 首先执行 try 中的代码块，如果执行过程中出现异常，系统会自动生成一个异常类型，并将该异常提交给 Python 解释器，此过程称为捕获异常。
- 当 Python 解释器收到异常对象时，会寻找能处理该异常对象的 except 块，如果找到合适的 except 块，则把该异常对象交给该 except 块处理，这个过程被称为处理异常。如果 Python 解释器找不到处理异常的 except 块，则程序运行终止，Python 解释器也将退出。
- 语法结构如下：
```python
'''
try:
    可能产生异常的代码块
    raise [异常类名称 [(异常描述信息)]]
except [ (Error1, Error2, ... ) [as e] ]:
    处理异常的代码块1
except [ (Error3, Error4, ... ) [as e] ]:
    处理异常的代码块2
except  [Exception]:
    处理其它异常
else：
    代码处理块
finally :
    代码处理块
代码处理块
'''
```
#### 17.1.1  语法结构参数说明
- []括起来部分,可以使用，也可以省略。其中各部分的含义如下：

    - (Error1, Error2,...) 、(Error3, Error4,...): Error1、Error2、Error3 和 Error4 都是具体的异常类型。显然，一个 except 块可以同时处理多种异常。
    - [as e]: 作为可选参数，表示给异常类型起一个别名 e，这样做的好处是方便在 except 块中调用异常类型（后续会用到）。
    - [Exception]: 作为可选参数，可以代指程序可能发生的所有异常情况，其通常用在最后一个 except 块。
- else：
    - 使用 else 包裹的代码，只有当 try 块没有捕获到任何异常时，才会得到执行；反之，如果 try 块捕获到异常，即便调用对应的 except 处理完异常，else 块中的代码也不会得到执行
- finally：
    - 无论 try 块是否发生异常，该块中的代码都会被执行
- raise：
    - 程序中使用了 raise 语句引发异常，但程序的执行是正常的，手动抛出的异常并不会导致程序崩溃
### 17.2  不使用else
```python
'''
1. 无else：
try 块捕获到异常并通过 except 成功处理，后续所有程序都会依次被执行
'''
try:
    result1 = 20 / int(input('请输入除数:'))
    print(result1)
except ValueError as e1:
    print('必须输入整数',e1)
except ArithmeticError as e2:
    print('算术错误，除数不能为 0',e2)
print('没有出现异常')
print("="*20,"无else")
```
### 17.3  使用else
```python
'''
2. 有 else 
只有当 try 块没有捕获到任何异常时，才会得到执行；反之，如果 try 块捕获到异常，即便调用对应的 except 处理完异常，else 块中的代码也不会得到执行
'''
try:
    result = 20 / int(input('请输入除数:'))
    print(result)
except ValueError as e3:
    print('必须输入整数',e3)
except ArithmeticError as e4:
    print('算术错误，除数不能为 0')
else:
    print('没有出现异常')
print("继续执行")
print("="*20,"有else")
```
### 17.4  同时处理多种异常
```python
#3. 同时处理多种异常
try:
    result = 20 / int(input('请输入除数:'))
    print(result)
except (ValueError,ArithmeticError) as e5:
    print("输入整数或除数不能为0",e5)
else:
    print('没有出现异常')
print("继续执行")

print("="*20,"多个异常数据类型")
```
### 17.5  手动抛出的异常:raise
```python
"""
4. 手动抛出的异常:raise
发生异常：程序由于错误导致的运行异常，是需要程序员想办法解决
程序执行：程序正常运行的结果，使用raise
raise语法格式：
    raise [异常类名称 [(异常描述信息)]]
    注：用 [] 括起来的为可选参数，其作用是指定抛出的异常名称，以及异常信息的相关描述
raise使用情景：
    ① raise：语句引发当前上下文中捕获的异常（比如在 except 块中），或默认引发 RuntimeError 异常。
    ② raise [异常类名称]：表示引发执行类型的异常。
    raise [异常类名称(描述信息)]：在引发指定类型的异常的同时，附带异常的描述信息。
"""
# 定义函数
def mye(level):
    if level < 1:
        raise Exception("raise")
        # 触发异常后，后面的代码就不会再执行,else后的代码
for i in [-1,0,1,2]:
    try:
        #调用函数mye（level）
        mye(i)            # 触发异常
    except Exception as err:
        print(i,err)
    else:
        print(i)

print("="*20,"手动引发的异常：raise")
```




