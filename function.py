#函数
# 函数的定义
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


#return语句的3种返回

    # return返回none(默认)
def add_default(a1,b1):
    c1 = a1 +b1
print(add_default(3,8))
print('*'*60+'reurn值：none')
    # return返回表达式
        #方式1
def add_expression01(a2,b2):
    return a2+b2
print(add_expression01(5.4, 1))

        #方式2
def add_expression02(a3,b3):
    c3 = a3 + b3
    return c3
print(add_expression02(5.4,1))
print('*'*60+'reurn值：表达式')
    #return返回多个值
def calc(a4,b4):
    add = a4 + b4
    min = a4 - b4
    cf = a4 * b4
    div = a4 / b4
    return add,min,cf,div
print(calc(4,8))
print('*'*60+'reurn值：多个值')



    #有return 与 无return 的区别：
        # 无return返回的是none
print("无return语句函数add（）返回：",add(3,7))

        # 有return返回的是函数运行结果
result = add_expression01(4,2)
print("有return语句函数add1（）返回：",result)
print('*'*60+'有/无return的区别')


