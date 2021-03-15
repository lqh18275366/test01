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