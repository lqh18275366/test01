
# 无默认参数的函数
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


#4.有默认参数的函数：
''''查找学生信息'''
def check_stu_msg(name,sno,school="tjcu"):

    student_information = ("学生信息表 \n姓名：{} \t学号：{} \t学校：{}".format(name,sno,school))
    return student_information
print(check_stu_msg(input("姓 名："),int(input("学 号："))))

#优化程序
print('*'*20+"对姓名和学号进行判断过滤")
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
print(check_stu_filter_msg(name1=input("姓 名："),sno1=int(input("学 号："))))


#5.可变化参数：列表形式
#语法格式：
def 函数名(位置参数1,位置参数2,*列表):
    print(type(列表))
    print(列表)  #列表名为元组
    for x in 列表:
        print(x,end=' ')  #end=' ':输出显示在同一行
print(函数名(1,2,3,4,5))

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

#6.可变参数：字典形式
def show_Dict(**kwargs):
    print(kwargs)
    #通过关键字传入
print(show_Dict())
print(show_Dict(key1='abc',key2='123'))

    #通过字典形式传入
dt = {'key1':'abc','key':'123'}
print(show_Dict(**dt))